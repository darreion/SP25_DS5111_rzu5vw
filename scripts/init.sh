#!/bin/bash

set -e # Exit if a command exits with a non-zero

echo "Updating system packages..."
sudo apt update

echo "Installing required packages..."
sudo apt install -y make python3.12-venv tree

echo "Done...!"
