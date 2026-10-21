#!/bin/bash

# give permission: 
# chmod +x python3_packages_install.sh
# run the reinstall
# ./python3_packages_install.sh

# Update package lists
sudo apt update
sudo apt install -y python3 python3-pip python3-venv python3-full

# Check if venv already exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv

    echo "Installing packages in venv..."
    source venv/bin/activate

    # Explicitly activate pip from venv to avoid system warnings
    venv/bin/pip install --upgrade pip
    pip install cupy-cuda12x
else
    echo "Virtual environment already exists. Upgrading..."
fi

source venv/bin/activate
# Install required packages using the correct pip path
venv/bin/pip install numpy sympy matplotlib statistics # cupy
pip install cupy-cuda12x

echo "Installation complete!"