#!/bin/bash

REPO_URL="https://github.com/OWAIS-KHAWAJA-789/AI_TicTacToe.git"
PROJECT_DIR="AI_TicTacToe"

# Function to check and install Python
install_python() {
    echo "🔍 Checking for Python 3..."
    if command -v python3 &>/dev/null; then
        echo "✅ Python 3 is installed."
    else
        echo "❌ Python 3 is not installed!"
        echo "🔄 Installing Python 3..."

        if [[ "$OSTYPE" == "linux-gnu"* ]]; then
            sudo apt update && sudo apt install -y python3 python3-pip
        elif [[ "$OSTYPE" == "darwin"* ]]; then
            echo "🍏 macOS detected. Installing Python via Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            brew install python3
        else
            echo "❌ Unsupported OS. Please install Python manually."
            exit 1
        fi
    fi
}

# Function to clone and run the game
clone_and_run() {
    echo "🚀 Cloning the repository..."
    git clone "$REPO_URL"

    if [[ -d "$PROJECT_DIR" ]]; then
        cd "$PROJECT_DIR" || exit
        echo "🎮 Starting Tic-Tac-Toe..."
        python3 tic_tac_toe.py
    else
        echo "❌ Failed to clone repository!"
        exit 1
    fi
}

# Main execution
echo "🎯 Setting up AI-Powered Tic-Tac-Toe..."
install_python
clone_and_run\
