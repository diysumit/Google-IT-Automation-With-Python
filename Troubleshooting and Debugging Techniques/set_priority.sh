#/bin/bash

for pid in $(pidof chrome); do
  renice 19 #lowest priority is 19, highest 1
done
