#!/bin/bash
# script takes URL as argument, sends a GET request to the URL, display response
curl -sH "X-School-User-Id: 98" "$1"
