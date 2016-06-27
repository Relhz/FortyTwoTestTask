#!/bin/bash

python manage.py allmodels 2>&1 >/dev/null | grep 'error' >> $(date +"%Y-%m-%d").dat
