#!/usr/bin/env python3
from multiprocessing import Pool
import os
from PIL import Image

dr = "./fixed/"
if not os.path.exists(dr):
    os.mkdir(dr)

tasks = [i for i in os.walk(".")]
tasks = tasks[0][2] # Try printing output of os.walk to understand

def run(task):
    try:
        if not task.endswith(".jpeg"): return None
        im = Image.open(task)
        im = im.rotate(270).resize((128,128)).convert("RGB")
        im.save(dr + task, "jpeg")
    except OSError as e:
        print(task, e)

p = Pool(len(tasks))
p.map(run, tasks)
#./lab_week1.py  0.17s user 0.05s system 99% cpu 0.220 total
#./lab_week1_multiprocessing.py  0.07s user 0.03s system 112% cpu 0.086 total