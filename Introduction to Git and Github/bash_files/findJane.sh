#!/bin/bash

files=$(grep ' jane ' ../data/list.txt | cut -d' ' -f3)
for file in $files; do
  if [ $HOME$file ]; then
    echo $HOME$file
  fi
done
