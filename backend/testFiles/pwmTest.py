# pwm test for motor control

# inputs for easy control
import tty
import sys
import termios

# imports for pwm use
import wiringpi
import time

# setting up the GPIO pin for pwm and seting the frequency
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# pwm frequency in Hz: 19,200,000 / pwmSetClock / pwmSetRange
# 19,200,000 / 10 / 1000 = 1920
wiringpi.pwmSetClock(10)
wiringpi.pwmSetRange(1000)

# loop-de-loop input into stdin 'r' to run the motor 's' to stop it
while 1:
    x=sys.stdin.read(1)
    if x == 'r':
        #motor on
        wiringpi.pwmWrite(18, 600)
    if x == 's':
        #motor off
        wiringpi.pwmWrite(18, 0)
