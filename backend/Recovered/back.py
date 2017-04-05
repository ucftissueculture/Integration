## backend/back.py

# Backend Implementation Class
# UCF Senior Design Project - Blue Agave
# Application written by Erik Kantrowitz for Agri-Starts

    ##!!## SSH: pi@127.0.0.1  blue agave ##!!##

# these imports are for controlling the GPIO pins and pwm
import RPi.GPIO as GPIO
import wiringpi
from time import sleep

class Back(object):

    def __init__(self):

        ## not 100% sure if everything that needs self
        ## currently has it

        # setting up the GPIO settings for the pwm
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

        # pwm frequency in Hz: 19,200,000 / pwmSetClock / pwmSetRange
        # 19,200,000 / 10 / 1000 = 1920
        wiringpi.pwmSetClock(10)
        wiringpi.pwmSetRange(1000)

        ## there is a better way to do this, most likely thowing up a
        ## dict or a list that automates all of this


        ## sets gpio to BCM pinout, followed by setting I/O pins
        ## self.gpio.setmode(gpio.BCM)
        ## self.gpio.setup(17, gpio.OUT, pull_up_down=gpio.PUD_UP)
        ## self.gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)
        ## self.gpio.setup(22, gpio.OUT, pull_up_down=gpio.PUD_UP)
        ## self.gpio.setup(0, gpio.IN, pull_up_down=gpio.PUD_UP)
        ## self.gpio.setup(5, gpio.IN, pull_up_down=gpio.PUD_UP)

        ## the above coment block should do the same as the initPins
        ## function, but I like the function idea better so when it
        ## definitely works get rid of all of this



        # this variable is for making sure only one press is logged
        # when a switch is pressed
        switchState = 0
        swc = gpio.input(27)

        # these are mostly testing functions, but can be used to
        # create status LEDs
        ledOn = gpio.output(26, 1)      # led on
        ledOff = gpio.output(26, 0)     # led off

    # a few motor controll functions that might be usefull

    ## when you finally get multiple pins going remember to add
    ## a second argument to them all letting them know which pin

    # turns motor on instantly at 60%
    def motorOn(self):
        wiringpi.pwmWrite(18, 600)

    # stops motor on instantly
    def motorOff(self):
        wiringpi.pwmWrite(18, 0)

    # ramps motor down from 60% to off with 10% increments
    def motorRampDown(self):
        for i in range(600, 0, 10):
            wiringpi.pwmWrite(18, i)

WIP on master
