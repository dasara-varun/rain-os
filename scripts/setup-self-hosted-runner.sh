#!/usr/bin/env bash
# Rain OS - GitHub Actions Self-Hosted Runner Installer & Daemon
# Use this script to turn any Linux PC, laptop, WSL2 instance, or cloud VM into a dedicated Rain OS builder.
set -euo pipefail

RUNNER_VERSION="2.321.0"
RUNNER_DIR="$HOME/actions-runner"
REPO_URL="https://github.com/dasara-varun/rain-os"

echo "=========================================================="
echo "    Rain OS - GitHub Actions Self-Hosted Runner Setup"
echo "=========================================================="

# Check if Docker is installed and running
if ! command -v docker >/dev/null 2>&1; then
    echo "Notice: Docker is required to run the Archiso build container."
    echo "Installing Docker..."
    if command -v apt-get >/dev/null 2>&1; then
        sudo apt-get update && sudo apt-get install -y docker.io curl tar
        sudo usermod -aG docker "$USER" || true
        sudo systemctl enable --now docker || true
    elif command -v pacman >/dev/null 2>&1; then
        sudo pacman -Syu --noconfirm docker curl tar
        sudo usermod -aG docker "$USER" || true
        sudo systemctl enable --now docker || true
    else
        echo "Error: Please install docker manually." >&2
        exit 1
    fi
fi

# Create runner directory
mkdir -p "$RUNNER_DIR"
cd "$RUNNER_DIR"

# Download runner package if not already downloaded
if [ ! -f "config.sh" ]; then
    echo "Downloading GitHub Actions Runner v${RUNNER_VERSION}..."
    curl -o actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz -L \
        "https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz"
    
    echo "Extracting installer..."
    tar xzf "./actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz"
    rm -f "./actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz"
fi

echo ""
echo "----------------------------------------------------------"
echo "To register this runner with your repository:"
echo "1. Go to: https://github.com/dasara-varun/rain-os/settings/actions/runners/new"
echo "2. Copy the token provided on that page."
echo "----------------------------------------------------------"
echo ""

if [ -f ".runner" ]; then
    echo "Runner is already configured."
else
    read -r -p "Enter your GitHub Actions registration TOKEN: " RUNNER_TOKEN
    if [ -z "$RUNNER_TOKEN" ]; then
        echo "Error: Token cannot be empty." >&2
        exit 1
    fi
    ./config.sh --url "$REPO_URL" --token "$RUNNER_TOKEN" --name "rain-builder-$(hostname)" --labels "self-hosted,linux,x64,rain-os" --unattended
fi

echo ""
echo "Starting GitHub Actions Runner..."
echo "Press Ctrl+C to stop, or run 'sudo ./svc.sh install && sudo ./svc.sh start' to run as a system service."
./run.sh
