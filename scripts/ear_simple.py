#!/usr/bin/env python

import os
import signal
import subprocess
import sys

p = subprocess.Popen(['pocketsphinx_continuous', 
    '-adcdev', 'plughw:1',
    '-lm', '/home/pi/catkin_ws/src/pishu_ear/8362.lm', 
    '-dict', '/home/pi/catkin_ws/src/pishu_ear/8362.dic', 
    '-inmic', 'yes', 
    '-logfn', '/dev/null'], stdout=subprocess.PIPE)
while True:
    line = p.stdout.readline()
    
    print len(line)

    if len(line) > 0:
        print line

    if 'MAYBE' in line:
        break

p.kill()

