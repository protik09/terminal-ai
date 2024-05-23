#!/bin/bash

# Set the folder to the directory where the script is running from
FOLDER=$(dirname "$0")
echo "Folder set to $FOLDER"

# # Enable dotglob to include hidden files/directories in glob patterns
# shopt -s dotglob

# # Recursively iterate through all folders in the project to find the venv
# for folder in "$FOLDER"/*; do
#     echo "Checking $folder for Python venv..."
#     if [ -f "$folder/activate.bat" ]; then
#         echo "Python venv found in $folder"
#         cd "$folder" || exit
#         # Check if running in Bash or PowerShell
#         if [ "$SHELL" = "/bin/bash" ]; then
#             # Running in Bash
#             source activate
#         else
#             echo "Running in Cygwin or something. Not supported."
#         fi
#         exit
#     fi
# done

# # If no venv found, create a new one and install requirements
# if [ ! -d "$FOLDER/.venv" ]; then
#     echo "No Python venv found. Creating a new one..."
#     python -m venv .venv
#     source .venv/Scripts/activate
#     echo "Installing Python requirements..."
#     pip install -r requirements.txt
#     echo "Python venv created and requirements installed."
# fi

# Use find to recursively search for a Python venv
VENV_FOUND=$(find "$FOLDER" -type d \( -name ".venv" -o -name "venv" \))

if [ -z "$VENV_FOUND" ]; then
    echo "No Python venv found. Creating a new one..."
    sudo apt install python3-venv -y
    python -m venv .venv
    source .venv/bin/activate
    echo "Installing Python requirements..."
    pip install -r requirements.txt
    echo "Python venv created and requirements installed."
else
    echo "Python venv found at $VENV_FOUND"
    # Activate the venv
    if [ "$SHELL" = "/bin/bash" ]; then
        # Running in Bash
        source "$VENV_FOUND"/bin/activate
    elif [ "$SHELL" = "/bin/csh" ] || [ "$SHELL" = "/bin/zsh" ]; then
        # For csh or zsh, use the appropriate activation script
        source "$VENV_FOUND"/bin/activate.csh
    elif [ "$SHELL" = "/bin/fish" ]; then
        # For csh or zsh, use the appropriate activation script
        source "$VENV_FOUND"/bin/activate.fish
    else
        echo "Unsupported shell. Please use Bash or Zsh."
    fi
fi
cd "$FOLDER" || exit