#!/usr/bin/python3
# -*- coding: utf-8 -*-
# example gpiozero code that could be used to have a reboot
#  and a shutdown function on one GPIO button
# scruss - 2017-10

use_button=27                       # lowest button on PiTFT+

import os
from gpiozero import Button
from signal import pause
from subprocess import check_call
from pygame import mixer

print('Started')
path=os.path.dirname(os.path.realpath(__file__))

mixer.init()
resetSound = mixer.Sound(path+'/reset.wav')
shutdownSound = mixer.Sound(path+'/shutdown.wav')
clickSound = mixer.Sound(path+'/click.wav')

held_for=0.0
resetAt=5
shutdownAt=10

def rls():
        global held_for
        if (held_for > shutdownAt):
                check_call(['/sbin/poweroff'])
        elif (held_for > resetAt):
                check_call(['/sbin/reboot'])
        else:
        	held_for = 0.0

def hld():
        # callback for when button is held
        #  is called every hold_time seconds
        global held_for
        # need to use max() as held_time resets to zero on last callback
        held_for = max(held_for, button.held_time + button.hold_time)
        if (held_for > resetAt and held_for < resetAt+1):
            resetSound.play(0,800)
        elif (held_for > shutdownAt and held_for < shutdownAt+1):
            shutdownSound.play()
        elif (held_for < shutdownAt):
            clickSound.play()

button=Button(use_button, hold_time=1.0, hold_repeat=True)
button.when_held = hld
button.when_released = rls

pause() # wait forever
