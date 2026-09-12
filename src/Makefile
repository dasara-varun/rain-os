CC ?= gcc
CFLAGS ?= -O3 -Wall -Wextra -std=c99 -march=x86-64-v2
PREFIX ?= /usr/local

all: rain-probe

rain-probe: rain-probe.c
	$(CC) $(CFLAGS) -o rain-probe rain-probe.c

install: rain-probe
	install -Dm755 rain-probe $(DESTDIR)$(PREFIX)/bin/rain-probe

clean:
	rm -f rain-probe

.PHONY: all install clean
