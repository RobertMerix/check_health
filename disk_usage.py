#!/usr/bin/env python3

import sys
import shutil


def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if thre is enough free disk space, false otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    print(f"FREE Gigabytes: {gigabytes_free} GB available")
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True


# Check for at least 2 GB and 10% free
if not check_disk_usage("/", 2, 10):
    print("Error: Not enough disk space")
    sys.exit(1)


print("Everything ok")
sys.exit(0)


