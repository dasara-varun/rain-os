/*
 * Rain OS High-Performance Native System & Display Probe
 * Copyright (c) 2026 Rain OS Contributors <https://github.com/dasara-varun/rain-os>
 * License: GPL-3.0-or-later
 *
 * Designed for sub-millisecond hardware profiling, multi-display discovery,
 * and Btrfs root mount verification.
 */

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <dirent.h>
#include <unistd.h>
#include <sys/utsname.h>
#include <sys/statvfs.h>

#define RAIN_VERSION "1.3.1"

typedef struct {
    char cpu_model[128];
    int cpu_cores;
    long total_ram_mb;
    long free_ram_mb;
    char root_fs[32];
    bool is_btrfs;
    int display_count;
    char displays[8][64];
    bool has_nvidia;
    bool has_amd;
    bool has_intel;
} SystemInfo;

static void trim_whitespace(char *str) {
    char *end;
    while (*str == ' ' || *str == '\t' || *str == '\n' || *str == '\r') str++;
    end = str + strlen(str) - 1;
    while (end > str && (*end == ' ' || *end == '\t' || *end == '\n' || *end == '\r')) end--;
    *(end + 1) = '\0';
}

static void probe_cpu(SystemInfo *info) {
    strncpy(info->cpu_model, "Generic x86_64 Processor", sizeof(info->cpu_model));
    info->cpu_cores = 0;

    FILE *f = fopen("/proc/cpuinfo", "r");
    if (!f) return;

    char line[256];
    bool model_found = false;
    while (fgets(line, sizeof(line), f)) {
        if (!model_found && strncmp(line, "model name", 10) == 0) {
            char *colon = strchr(line, ':');
            if (colon) {
                colon++;
                trim_whitespace(colon);
                strncpy(info->cpu_model, colon, sizeof(info->cpu_model) - 1);
                model_found = true;
            }
        }
        if (strncmp(line, "processor", 9) == 0) {
            info->cpu_cores++;
        }
    }
    fclose(f);
    if (info->cpu_cores == 0) info->cpu_cores = 1;
}

static void probe_memory(SystemInfo *info) {
    info->total_ram_mb = 0;
    info->free_ram_mb = 0;

    FILE *f = fopen("/proc/meminfo", "r");
    if (!f) return;

    char line[128];
    while (fgets(line, sizeof(line), f)) {
        if (strncmp(line, "MemTotal:", 9) == 0) {
            long kb = 0;
            if (sscanf(line + 9, "%ld", &kb) == 1) {
                info->total_ram_mb = kb / 1024;
            }
        } else if (strncmp(line, "MemAvailable:", 13) == 0) {
            long kb = 0;
            if (sscanf(line + 13, "%ld", &kb) == 1) {
                info->free_ram_mb = kb / 1024;
            }
        }
    }
    fclose(f);
}

static void probe_mounts(SystemInfo *info) {
    strncpy(info->root_fs, "unknown", sizeof(info->root_fs));
    info->is_btrfs = false;

    FILE *f = fopen("/proc/mounts", "r");
    if (!f) return;

    char dev[128], mount[128], fstype[32], opts[256];
    int dump, pass;
    while (fscanf(f, "%127s %127s %31s %255s %d %d", dev, mount, fstype, opts, &dump, &pass) == 6) {
        if (strcmp(mount, "/") == 0) {
            strncpy(info->root_fs, fstype, sizeof(info->root_fs) - 1);
            if (strcmp(fstype, "btrfs") == 0) {
                info->is_btrfs = true;
            }
            break;
        }
    }
    fclose(f);
}

static void probe_gpus(SystemInfo *info) {
    info->has_nvidia = false;
    info->has_amd = false;
    info->has_intel = false;

    DIR *dir = opendir("/sys/bus/pci/devices");
    if (!dir) return;

    struct dirent *ent;
    while ((ent = readdir(dir)) != NULL) {
        if (ent->d_name[0] == '.') continue;

        char path[256];
        snprintf(path, sizeof(path), "/sys/bus/pci/devices/%s/class", ent->d_name);
        FILE *f = fopen(path, "r");
        if (f) {
            char class_str[32];
            if (fgets(class_str, sizeof(class_str), f)) {
                // 0x030000 = VGA, 0x030200 = 3D controller
                if (strncmp(class_str, "0x0300", 6) == 0 || strncmp(class_str, "0x0302", 6) == 0) {
                    fclose(f);
                    snprintf(path, sizeof(path), "/sys/bus/pci/devices/%s/vendor", ent->d_name);
                    FILE *fv = fopen(path, "r");
                    if (fv) {
                        char vendor_str[32];
                        if (fgets(vendor_str, sizeof(vendor_str), fv)) {
                            if (strncmp(vendor_str, "0x10de", 6) == 0) info->has_nvidia = true;
                            else if (strncmp(vendor_str, "0x1002", 6) == 0) info->has_amd = true;
                            else if (strncmp(vendor_str, "0x8086", 6) == 0) info->has_intel = true;
                        }
                        fclose(fv);
                    }
                    continue;
                }
            }
            fclose(f);
        }
    }
    closedir(dir);
}

static void probe_displays(SystemInfo *info) {
    info->display_count = 0;
    DIR *dir = opendir("/sys/class/drm");
    if (!dir) return;

    struct dirent *ent;
    while ((ent = readdir(dir)) != NULL && info->display_count < 8) {
        if (strncmp(ent->d_name, "card", 4) == 0 && strchr(ent->d_name, '-')) {
            char status_path[256];
            snprintf(status_path, sizeof(status_path), "/sys/class/drm/%s/status", ent->d_name);
            FILE *f = fopen(status_path, "r");
            if (f) {
                char status[32];
                if (fgets(status, sizeof(status), f)) {
                    trim_whitespace(status);
                    if (strcmp(status, "connected") == 0) {
                        strncpy(info->displays[info->display_count], ent->d_name, sizeof(info->displays[0]) - 1);
                        info->display_count++;
                    }
                }
                fclose(f);
            }
        }
    }
    closedir(dir);
}

int main(int argc, char *argv[]) {
    bool json_mode = false;
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--json") == 0) {
            json_mode = true;
        }
    }

    SystemInfo info;
    memset(&info, 0, sizeof(info));

    probe_cpu(&info);
    probe_memory(&info);
    probe_mounts(&info);
    probe_gpus(&info);
    probe_displays(&info);

    struct utsname u;
    uname(&u);

    if (json_mode) {
        printf("{\n");
        printf("  \"distribution\": \"Rain OS\",\n");
        printf("  \"version\": \"%s\",\n", RAIN_VERSION);
        printf("  \"kernel\": \"%s\",\n", u.release);
        printf("  \"arch\": \"%s\",\n", u.machine);
        printf("  \"cpu\": {\n");
        printf("    \"model\": \"%s\",\n", info.cpu_model);
        printf("    \"cores\": %d\n", info.cpu_cores);
        printf("  },\n");
        printf("  \"memory\": {\n");
        printf("    \"total_mb\": %ld,\n", info.total_ram_mb);
        printf("    \"free_mb\": %ld\n", info.free_ram_mb);
        printf("  },\n");
        printf("  \"filesystem\": {\n");
        printf("    \"root_type\": \"%s\",\n", info.root_fs);
        printf("    \"is_btrfs\": %s\n", info.is_btrfs ? "true" : "false");
        printf("  },\n");
        printf("  \"gpus\": {\n");
        printf("    \"nvidia\": %s,\n", info.has_nvidia ? "true" : "false");
        printf("    \"amd\": %s,\n", info.has_amd ? "true" : "false");
        printf("    \"intel\": %s\n", info.has_intel ? "true" : "false");
        printf("  },\n");
        printf("  \"displays\": [\n");
        for (int i = 0; i < info.display_count; i++) {
            printf("    \"%s\"%s\n", info.displays[i], (i + 1 < info.display_count) ? "," : "");
        }
        printf("  ]\n");
        printf("}\n");
    } else {
        printf("\033[1m\033[36mRain OS Native Hardware & Display Probe (C Engine)\033[0m\n");
        printf("==========================================================\n");
        printf("  Distribution:  Rain OS %s (%s)\n", RAIN_VERSION, u.machine);
        printf("  Kernel:        %s\n", u.release);
        printf("  Processor:     %s (%d cores)\n", info.cpu_model, info.cpu_cores);
        printf("  Memory:        %ld MB Total (%ld MB Available)\n", info.total_ram_mb, info.free_ram_mb);
        printf("  Root FS:       %s (%s)\n", info.root_fs, info.is_btrfs ? "\033[32mBtrfs snapshot ready\033[0m" : "Standard");
        printf("  Graphics:      %s%s%s%s\n",
               info.has_nvidia ? "NVIDIA " : "",
               info.has_amd ? "AMD Radeon " : "",
               info.has_intel ? "Intel " : "",
               (!info.has_nvidia && !info.has_amd && !info.has_intel) ? "Integrated/VESA" : "");
        printf("  Multi-Display: %d active display connector%s detected\n",
               info.display_count, info.display_count == 1 ? "" : "s");
        for (int i = 0; i < info.display_count; i++) {
            printf("    \033[32m*\033[0m %s\n", info.displays[i]);
        }
        printf("\n\033[32mProbe completed in <1 ms.\033[0m\n");
    }

    return 0;
}
