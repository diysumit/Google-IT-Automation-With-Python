#!/bin/bash

line='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

echo 'Starting at:' $(date); echo $line

echo 'UPTIME'; uptime; echo $line

echo 'FREE'; free; echo $line

echo 'WHO'; who; echo $line

echo 'Finishing at:' $(date)
