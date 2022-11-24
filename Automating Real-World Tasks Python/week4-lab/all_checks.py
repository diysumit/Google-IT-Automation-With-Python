#!/usr/bin/env python3

import os
import sys
import shutil
import psutil
import socket

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100*du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def check_cpu_usage(percent):
    """Returns True if cpu usage is below certain percentage"""
    usage = psutil.cpu_percent(1)
    print(f"DEBUG: usage: {usage}")
    return usage > percent

def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise"""
    try:
        socket.gethostbyname("localhost")
        return False
    except:
        return True

def check_cpu_load():
    """Returns Ture if the load on CPU is more than 80%"""
    return check_cpu_usage(80)


def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_gb=2, min_percent=20)

def check_memory():
    psutil.virtual_memory() # check virtual memory
    pass

def health_checks():
    everything_ok = True
    try:
        checks = [
            (check_reboot, "Pending Reboot."),
            (check_root_full, "Root partition full."),
            (check_cpu_load, "ERROR! CPU is overloaded"),
            (check_no_network, "No working network"),
            (check_memory, "")
        ]
        for check, msg in checks:
            if check():
                print(msg)
                everything_ok = False
        if not everything_ok:
            print('Everything not ok :(')
        print("Everything ok.")
    except Exception as e:
        print(f'Exception Ocuured: {e}')
    return everything_ok

def main():
    everything_ok = health_checks()
    print(everything_ok)

if __name__ == "__main__":
    sys.exit(main())