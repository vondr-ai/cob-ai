#!/usr/bin/env python3
"""
Script to build and upload the cob-ai package to PyPI.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main build and upload process."""
    print("🚀 Building and uploading cob-ai package to PyPI")
    
    # Clean previous builds
    if not run_command("rmdir /s /q dist build cob_ai.egg-info 2>nul || echo Cleaned", "Cleaning previous builds"):
        pass  # It's okay if cleanup fails
    
    # Build the package
    if not run_command("python -m build", "Building package"):
        sys.exit(1)
    
    # Check the package
    if not run_command("python -m twine check dist/*", "Checking package"):
        sys.exit(1)
    
    # Upload to PyPI (you'll need to authenticate)
    print("\n📤 Ready to upload to PyPI!")
    print("Run the following command to upload:")
    print("python -m twine upload dist/*")
    print("\nOr for test PyPI first:")
    print("python -m twine upload --repository testpypi dist/*")

if __name__ == "__main__":
    main()