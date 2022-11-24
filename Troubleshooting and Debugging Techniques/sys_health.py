#!/usr/bin/env python3
import shutil
import psutil

# du = shutil.disk_usage("/")
#
# print(f"Disk(/) {du}")
# print(f"CPU % (0.5 sec interval) {psutil.cpu_percent(0.5)}")

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return  usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
     print("Alert! High Disk and CPU usage, close some processes.")
else:
    print("Disk and CPU functioning normally")
