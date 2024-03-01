#!/bin/bash
# Sc esponse
curl -so /dev/null -w "%{http_code}" "$1"
