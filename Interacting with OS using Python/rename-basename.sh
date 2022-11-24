#!/bin/bash

for file in *.py; do
  name=$(basename "$file" .py)
  # remove echo below to actually make script work
  echo mkdir -p "renamed"
  echo cp "$file" "./renamed/$name.txt"
done
