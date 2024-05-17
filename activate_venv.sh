#!/bin/bash

# Set the folder to the directory where the script is running from
FOLDER=$(dirname "$0")
echo "Folder set to $FOLDER"

# Recursively iterate through all folders in the project to find the venv
for folder in "$FOLDER"/*; do
    if [ -f "$folder/activate" ]; then
        echo "Python venv found in $folder"
        cd "$folder" || exit
        # Check if running in Bash or PowerShell
        if [ "$SHELL" = "/bin/bash" ]; then
            # Running in Bash
            source activate
        else
            echo "Running in Cygwin or something. Not supported."
        fi
        exit
    fi
done

# If no venv found, create a new one and install requirements
if [ ! -d "$FOLDER/.venv" ]; then
    echo "No Python venv found. Creating a new one..."
    python -m venv .venv
    source .venv/Scripts/activate
    echo "Installing Python requirements..."
    pip install -r requirements.txt
    echo "Python venv created and requirements installed."
fi