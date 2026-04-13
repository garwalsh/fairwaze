#!/usr/bin/env python3
"""
Setup script for FairWaze Evaluation Harness
"""

import os
import subprocess
import sys
from pathlib import Path

def check_python_version():
    """Check if Python version is adequate"""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✓ Python version: {sys.version.split()[0]}")

def install_requirements():
    """Install required packages"""
    print("Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        sys.exit(1)

def setup_environment():
    """Set up environment configuration"""
    env_example = Path(".env.example")
    env_file = Path(".env")

    if env_example.exists() and not env_file.exists():
        print("Setting up environment file...")
        env_file.write_text(env_example.read_text())
        print("✓ Created .env file from .env.example")
        print("  Please edit .env and add your ANTHROPIC_API_KEY")
    elif env_file.exists():
        print("✓ Environment file already exists")
    else:
        print("Warning: .env.example not found")

def create_directories():
    """Create necessary directories"""
    dirs = ["eval_results", "example_results"]
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
    print(f"✓ Created directories: {', '.join(dirs)}")

def test_installation():
    """Test if the installation works"""
    print("Testing installation...")
    try:
        import anthropic
        print("✓ Anthropic library imported successfully")

        # Test if the harness can be imported
        from eval_harness import EvalHarness, EvalPrompt
        print("✓ EvalHarness imported successfully")

        print("✓ Installation test passed")
    except ImportError as e:
        print(f"✗ Installation test failed: {e}")
        sys.exit(1)

def main():
    """Main setup function"""
    print("FairWaze Evaluation Harness Setup")
    print("=" * 40)

    check_python_version()
    install_requirements()
    setup_environment()
    create_directories()
    test_installation()

    print("\n" + "=" * 40)
    print("Setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit .env file and add your ANTHROPIC_API_KEY")
    print("2. Run a test: python eval_harness.py --prompts sample_prompts.json")
    print("3. Or try examples: python example_usage.py")
    print("\nSee USAGE.md for detailed documentation.")

if __name__ == "__main__":
    main()