#!/usr/bin/env python3
"""
Minimal setup script for Frigate on Windows
"""

import subprocess
import sys

REQUIRED_PACKAGES = [
    "slowapi",
    "aiofiles", 
    "pyzmq",
    "paho-mqtt",
    "psutil",
    "opencv-python-headless",
    "numpy",
    "scipy",
    "pandas",
    "pathvalidate",
    "titlecase",
    "unidecode",
    "setproctitle",
    "ws4py",
    "prometheus-client",
    "requests",
    "types-requests",
    "pytz",
    "tzlocal",
]

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Installed {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package}: {e}")
        return False

def main():
    print("🚀 Installing minimal Frigate dependencies...")
    
    failed = []
    for package in REQUIRED_PACKAGES:
        if not install_package(package):
            failed.append(package)
    
    if failed:
        print(f"\n❌ Failed to install: {failed}")
        return 1
    else:
        print("\n✅ All dependencies installed successfully!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
