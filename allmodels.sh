#!/bin/bash

python manage.py allmodels >> $(date +"%Y-%m-%d").dat
