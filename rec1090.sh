#!/usr/bin/env bash
# record dump1090 data
# example usage: ./rec1090.sh data.txt

nc 127.0.0.1 30003 >> "$1"
