#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

# this script will clear any LEDs left in the 'on' state that a 
#diffrent script may have left on

sense.clear()
