#!/bin/bash

sudo apt update
sudo apt install -y python3 python3-pip python3-venv

if [ ! -d "venv" ]; then
    echo "Creating virtual environment and installing packages..."
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install numpy cupy sympy matplotlib statistics
else
    echo "Virtual environment already exists. Activating..."
    source venv/bin/activate
fi          