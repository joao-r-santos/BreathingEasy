#!/bin/bash

gunicorn app:app -D

# pkill gunicorn
