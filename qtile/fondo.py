#!/bin/python
import subprocess
import random
import sys


wallpapers = [
    31,40,42,46,51,56,
    58,78,95,107,125,140,
    199,205,213,240,253,
    256,277,290,305,
    ]

try:
    wallpaper = sys.argv[1]
except IndexError:
    wallpaper = random.choice(wallpapers)
    
zero = '0' * (4 - len(str(wallpaper)))

subprocess.run(['feh' ,'--bg-scale',f'/home/espai422/.config/qtile/wallpapers/{zero}{wallpaper}.jpg'])



