#!/bin/bash

python manage.py allmodels 2> middle_file.dat

grep error middle_file.dat >> $(date +"%Y-%m-%d").dat
