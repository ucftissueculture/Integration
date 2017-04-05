## mcRecovered.py ##

import wiringpi
import time

#setting up the GPIO settings for the pwm
# setting up the GPIO settings for the pwm
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
@@ -12,26 +12,25 @@ wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(10)
wiringpi.pwmSetRange(1000)

#sets gpio to BCM pinout, followed by setting I/O pins
# sets gpio to BCM pinout, followed by setting I/O pins
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)

#ledOn = gpio.output(17, 1)      #led on
#ledOff = gpio.output(17, 0)     #led off
#swc = gpio.input(27)
# ledOn = gpio.output(17, 1)      # led on
# ledOff = gpio.output(17, 0)     # led off
# swc = gpio.input(27)

while 1:
    if gpio.input(27):        #switch is pressed
        gpio.output(17,0)      #led off
        wiringpi.pwmWrite(18, 0)    #motor off

  #if input_state == False:
        #  print('Button Pressed')
    #print '\r'       #carriage return, not really needed
    if gpio.input(27):                 # switch is pressed
        gpio.output(17,0)             # led off
        wiringpi.pwmWrite(18, 0)       # motor off

  # if input_state == False:
          # print('Button Pressed')
        # print '\r'              # carriage return, not really needed
    else:
        gpio.output(17, 1)      #led on
        wiringpi.pwmWrite(18, 600)    #motor on

wiringpi.pwmWrite(18,0)
        gpio.output(17, 1)             # led on
        wiringpi.pwmWrite(18, 600)         # motor on

wiringpi.pwmWrite(18,0)
WIP on master
