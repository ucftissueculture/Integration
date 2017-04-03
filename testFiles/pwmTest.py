#pwm test for motor control

#inputs for easy control
import tty
import sys
import termios

#imports for pwm use
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


# comented block is for setting the terminal to accept stdin without 
# the need for escape char

# # saves standard input settings so that it can fix the 
# # terminal after it is done
# orig_settings = termios.tcgetattr(sys.stdin)
# # sets the terminal to a mode that does not require an 
# # escape key to accept input from stdin
# tty.setraw(sys.stdin)



# while x != chr(27): #

while 1:
    x=sys.stdin.read(1)
    if x == 'r':
        #motor on
        wiringpi.pwmWrite(18, 600)
    if x == 's':
        #motor off
        wiringpi.pwmWrite(18, 0)

    
    
    
# # fixes the terminal
# termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
