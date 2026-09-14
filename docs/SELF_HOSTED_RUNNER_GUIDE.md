# Rain OS — Self-Hosted Runner & Local Builder Guide

This guide details how to set up a **Self-Hosted GitHub Actions Runner** on your local machine, WSL2, or a dedicated Linux server to build Rain OS without the limitations of GitHub-hosted runners.

---

## Why Use a Self-Hosted Runner?

| Feature | Standard GitHub Runner (`ubuntu-latest`) | Self-Hosted Runner (`self-hosted`) |
| :--- | :--- | :--- |
| **Asset Size Limit** | 2.0 GiB API hard limit | **Unlimited** (Local disk / direct mirror) |
| **Build Time** | 15–25 minutes | **2–4 minutes** (uses all host CPU cores) |
| **Disk Space** | ~14 GB scratch (causes disk errors) | **Full Host Disk** (Hundreds of GBs) |
| **Monthly Cost** | 2,000–3,000 minutes quota | **100% Free & Unlimited** |
| **Download Time** | Must download ~2GB ISO after CI | **Instant** (ISO already on your local drive) |

---

## Method 1: Running on Windows via WSL2 (Recommended for This PC)

### Step 1: Install WSL2 (One Command)
Open an Administrator PowerShell on Windows and run:
```powershell
wsl.exe --install -d Ubuntu
```
Restart your computer if prompted.

### Step 2: Install Docker inside Ubuntu
Open the newly created Ubuntu terminal and run:
```bash
sudo apt-get update && sudo apt-get install -y docker.io curl tar
sudo usermod -aG docker $USER
sudo systemctl enable --now docker
```

### Step 3: Run the Automated Setup Script
Navigate to the Rain OS repository and run:
```bash
cd "/mnt/e/rain os"
chmod +x scripts/setup-self-hosted-runner.sh
./scripts/setup-self-hosted-runner.sh
```

### Step 4: Enter GitHub Registration Token
1. In your browser, open: [GitHub Actions Runners Settings](https://github.com/is-it-raining-now/rain-os/settings/actions/runners/new)
2. Copy the token generated on that page.
3. Paste it into the script prompt.

The runner will connect and listen for build jobs immediately!

---

## Method 2: Running on a Dedicated Linux PC or Free Cloud VM

If you have a spare PC, laptop, or a free cloud VM (e.g. Oracle Cloud 4-core Ampere with 24GB RAM):

```bash
git clone https://github.com/is-it-raining-now/rain-os.git
cd rain-os
chmod +x scripts/setup-self-hosted-runner.sh
./scripts/setup-self-hosted-runner.sh
```

To configure it to start automatically in the background on boot:
```bash
cd ~/actions-runner
sudo ./svc.sh install
sudo ./svc.sh start
```

---

## How to Trigger Builds on the Self-Hosted Runner

### Via GitHub Actions Web Interface (`workflow_dispatch`):
1. Navigate to **Actions** -> **Build Rain OS ISO** (or **Release Rain OS**).
2. Click **Run workflow**.
3. Under **Runner environment**, select:
   * `self-hosted`: Builds on your local fast machine.
   * `ubuntu-latest`: Builds in the standard GitHub cloud.

### On-Demand Execution (Conserving Compute):
All workflows are configured for manual execution (`workflow_dispatch`) to ensure compute is only used when deliberately requested. To run:
1. Navigate to **Actions** -> select the workflow.
2. Click **Run workflow** -> choose runner -> execute.
