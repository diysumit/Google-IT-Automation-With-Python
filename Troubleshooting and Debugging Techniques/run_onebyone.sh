#!/bin/bash

name=$1

killall -STOP $name

for pid in $(pidof $name); do
  while kill -CONT $pid; do
    sleep 10
  done
done
