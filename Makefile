# Rain OS Build and Test Makefile

.PHONY: all help validate build clean checksums

all: validate

help:
	@echo "Rain OS Build Automation"
	@echo "========================"
	@echo "  make validate   - Validate spec artifacts, manifests, and scripts"
	@echo "  make build      - Build live Archiso ISO (requires root & Arch Linux)"
	@echo "  make checksums  - Compute SHA256 checksums for built ISOs"
	@echo "  make clean      - Clean up build output and temporary work directories"

validate:
	@bash ./scripts/validate-spec.sh

build:
	@sudo ./scripts/build-iso.sh

checksums:
	@if [ -d out ]; then \
		cd out && sha256sum *.iso > SHA256SUMS 2>/dev/null || echo "No ISOs found in out/"; \
	fi

clean:
	@rm -rf out/work/
	@echo "Cleaned temporary build cache."
