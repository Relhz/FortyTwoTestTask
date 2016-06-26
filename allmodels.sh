#!/bin/bash

python manage.py allmodels 2>> $(date +"%Y-%m-%d").dat
