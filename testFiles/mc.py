import RPi.GPIO as gpio
import wiringpi
import time

#setting up the GPIO settings for the pwm 
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# pwm frequency in Hz: 19,200,000 / pwmSetClock / pwmSetRange
# 19,200,000 / 10 / 1000 = 1920
wiringpi.pwmSetClock(10)
wiringpi.pwmSetRange(1000)

#sets gpio to BCM pinout, followed by setting I/O pins
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(27, gpio.IN)

#ledOn = gpio.output(17, 1)      #led on
#ledOff = gpio.output(17, 0)     #led off
#swc = gpio.input(27)

while 1:
    if gpio.input(27):
        gpio.output(17,0)
        wiringpi.pwmWrite(18, 0)
	#wiringpi.pwmWrite(18, -10)
	print 'switch pressed'
	print '\r'
    else:
        gpio.output(17, 1)
        wiringpi.pwmWrite(18, 600)
    
wiringpi.pwmWrite(18,0)

