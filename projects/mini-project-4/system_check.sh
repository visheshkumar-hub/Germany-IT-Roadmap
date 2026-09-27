#!/bin/bash

echo "===== System Check ====="

echo "Hostname:"
hostname

echo "Current User:"
whoami

echo "Disk Usage:"
df -h

echo "Memory:"
free -h

echo "IP Address:"
hostname -I
