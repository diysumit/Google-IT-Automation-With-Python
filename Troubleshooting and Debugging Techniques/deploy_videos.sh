#!/bin/bash

#converts webm video to mp4

echo "Starting video conversion"
for video in *.webm; do
  mp4_video="$(echo "$video" | sed 's/\.webm$/.mp4/')"
  #daemonizes the process
  #daemonize -c $PWD
  /usr/bin/ffmpeg -nostats -nostdin -i "$video" "$mp4_video"
done
