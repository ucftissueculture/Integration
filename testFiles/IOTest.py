import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(17, gpio.OUT)
gpio.setup(27, gpio.IN)

while True:
    if (gpio.input(27)):
        #do a thing
	gpio.output(17, 1)
        #print 'pressed'
    else:
	gpio.output(17, 0)
