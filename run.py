#!/usr/bin/env python3
"""
CPU Scheduling Simulator - Entry Point
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from app import main

if __name__ == "__main__":
    main()