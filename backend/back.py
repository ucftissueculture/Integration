#                  Backend Implementation Class                      #
#              UCF Senior Design Project - Blue Agave                #
#        Application written by Erik Kantrowitz for Agri-Starts      #


# Control GPIO pins
#   M1 | S0 | S1 | S2 | S3 | S4 |
# | 12 | 07 | 11 | 13 | 15 | 16 |  Board Val
# | 18 | 04 | 17 | 27 | 22 | 23 |  BCM Val

# filling GPIO pins
# | W0 | W1 | W2 | W3 | W4 |
# | 22 | 29 | 31 | 36 | 37 |  Board Val
# | 05 | 06 | 16 | 25 | 26 |  BCM Val

# possible LED indicator
# | L0 |
# | 18 |
# | 24 |



# these imports are for controlling the GPIO pins and pwm
import RPi.GPIO as GPIO
import wiringpi
from time import sleep

class Back(object):

    def __init__(self):



        # setting up the GPIO settings for the pwm
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

        # pwm frequency in Hz: 19,200,000 / pwmSetClock / pwmSetRange
        # 19,200,000 / 10 / 1000 = 1920
        wiringpi.pwmSetClock(10)
        wiringpi.pwmSetRange(1000)

        # sets gpio to BCM pinout
        gpio.setmode(gpio.BCM)

        ## there is a better way to do this, most likely thowing up a
        ## dict or a list that automates all of this

        # swc = {
        # 1:gpio.setup(0, gpio.IN, pull_up_down=gpio.PUD_UP),
        # 2:gpio.setup(5, gpio.IN, pull_up_down=gpio.PUD_UP),
        # 3:gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP),
        # 4:gpio.setup(22, gpio.IN, pull_up_down=gpio.PUD_UP),
        # 5:gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)
        # }


        # gpio.setup(0, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(4, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(22, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(23, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)
        ## the above coment block should do the same as the initPins
        ## function, but I like the function idea better so when it
        ## definitely works get rid of all of this

        # this variable is for making sure only one press is logged
        # when a switch is pressed
        switchState = 0
        motorState = 1          #Motor on initially

        # initialization for filling
        wand1 = gpio.setup(5, gpio.OUT)
        wand2 = gpio.setup(6, gpio.OUT)
        wand3 = gpio.setup(16,gpio.OUT)
        wand4 = gpio.setup(25,gpio.OUT)
        wand5 = gpio.setup(26, gpio.OUT)

########################END OF __INIT__########################

    # a few motor controll functions that might be usefull

    # currently all of these motor functions are set to only run
    # the motor connected to pin 18, for final deployment
    # this can be made better by allowing a second argument
    # that takes in an int and replaces 18 in all the motor
    # methods with that int
    # ex:    def motorOn(self, n):
    #           wiringpi.pwmWrite(n, 600)

    # turns motor on instantly at 60%
    def motorOn(self):
        wiringpi.pwmWrite(18, 600)
        motorState = 1

    # stops motor on instantly
    def motorOff(self):
        wiringpi.pwmWrite(18, 0)
        motorState = 0

    ## for whatever reason the motorRampDown function was not
    ## working when trying to ramp down on exit.

    ## during testing the motor stop function didn't seem as
    ## abrupt as I worried it might be so the ramp up & down
    ## methods might not be worth having

    # ramps motor down from 60% to off with 10% increments
    def motorRampDown(self):
        for i in range(600, 0, 10):
            wiringpi.pwmWrite(18, i)

    # ramps motor up from off to 60% with 10% increments
    def motorRampUp(self):
        for i in range(o, 600, 10):
            wiringpi.pwmWrite(18, i

    # takes in argument n for speed control 0 <= n <= 1000
    def motorSpeed(self, n):
        wiringpi.pwmWrite(18, n)

    # CUrrently how this is, it is pretty useless
    def swc(self):
        gpio.input(27)
        # maybe some logic here about if lastState != Current State
        # print Button pressed
    def test(self):
        print "this test worked"

    # def initPins(self, pins):
    #     swc = {
    #     1:gpio.setup(0, gpio.IN, pull_up_down=gpio.PUD_UP),
    #     2:gpio.setup(5, gpio.IN, pull_up_down=gpio.PUD_UP),
    #     3:gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP),
    #     4:gpio.setup(22, gpio.IN, pull_up_down=gpio.PUD_UP),
    #     5:gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)
    #     }


    ## this is mostly for testing, but an indicator LED can be used
    ## in final release
    # function to control an LED, it takes in the state to change
    # the LED to for example ledState(on), turns the LED on
    def ledState(self, state):
        state = state.lower()
        if state == "on":
            ledOn = gpio.output(24, 1)      # led on
        if state == "off"
            ledOff = gpio.output(24, 0)     # led off

    def ledBlink(self):
        gpio.output(24, 0)
        sleep(1/10)
        gpio.output(24, 1)
        gpio.output(24, 0)
        sleep(1/10)
        gpio.output(24, 1)

    def filling(self):
        ON = 0
        OFF = 1

        duration = 4

        wand1.write(ON)
        wand2.write(ON)
        wand3.write(ON)
        wand4.write(ON)
        wand5.write(ON)

        sleep(duration)

        wand1.write(OFF)
        wand2.write(OFF)
        wand3.write(OFF)
        wand4.write(OFF)
        wand5.write(OFF)

    def switchFill(self):
        motorOff
        filling
        motorOn

    def switchBlock(self):
        ledBlink
        sleep(5)
        if swc[1]:
            motorOff
        if swc[1] != 1 and motorState = 0
            motorOn

    def trayError(self, filled, complete):
        if filled != complete:
            if filled > complete:
                error = 1
                errorStatus = filled - complete
                errorLog = "More trays were filled than were logged \
                as complete, the trays might have been removed before \
                reaching the end of the line"
            if complete > filled:
                error = 2
                errorStatus = complete - filled
                errorLog = "Trays that were not logged as filled \
                were logged as complete"
        else:
            error = 0
            errorStatus = ""
            errorLog = "No errors were detected logging trays"
