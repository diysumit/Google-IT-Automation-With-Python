#!/bin/bash
os_family=$(cat /etc/os-release| grep ID_LIKE | cut -d '=' -f 2)


if [ $os_family = arch ]; then
  $(sudo pacman -Syyu puppet)
elif [ $os_family = debian ]; then
  $(sudo apt-get install puppet)
fi
