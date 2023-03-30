#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL
curl -s -o /dev/null -w "%{size_download}\n"  "$1" 
