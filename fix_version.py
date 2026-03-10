#!/usr/bin/env python3

# Create the version file with correct syntax
with open('frigate/version.py', 'w') as f:
    f.write('VERSION = "0.18.0-dev"\n')

print("Version file created successfully!")
