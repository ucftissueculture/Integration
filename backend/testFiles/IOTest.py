import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(17, gpio.OUT)
gpio.setup(27, gpio.IN)

while True:
    if (gpio.input(27)):			#if switch is pressed
        #do a thing
	gpio.output(17, 1)			#turn on the LED
        #print 'pressed'
    else:
	gpio.output(17, 0)
