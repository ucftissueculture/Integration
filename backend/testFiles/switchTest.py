#              Switch Maintenance Test program for                   #
#               Agri-Starts Senior Design Project                    #
#              UCF Senior Design Project - Blue Agave                #
#        Application written by Erik Kantrowitz for Agri-Starts      #

# Control GPIO pins
#   M1 | S0 | S1 | S2 | S3 | S4 |
# | 12 | 07 | 11 | 13 | 15 | 16 |  Board Val
# | 18 | 04 | 17 | 22 | 23 | 27 |  BCM Val

# filling GPIO pins
# | W0 | W1 | W2 | W3 | W4 |
# | 22 | 29 | 31 | 36 | 37 |  Board Val
# | 05 | 06 | 16 | 25 | 26 |  BCM Val

# possible LED indicator
# | L0 |
# | 18 |
# | 24 |


import signal
import sys
import RPi.GPIO as gpio
import math
from back import Back
from time import sleep

back = Back()

swc = {0:gpio.input(4), 1:gpio.input(17), 2:gpio.input(22)
, 3:gpio.input(23), 4:gpio.input(27)}



def run_program():
	print " .   .   .   .    .###.. .   .   .   . "
	time.sleep(0.25)
	print " .   .   . ..... .#####..... .   .   . "
	time.sleep(0.25)
	print " .   .   . ..##~.?#####Z..##...  .   . "
	time.sleep(0.25)
	print " .   .   ....###O.#####.####:..  .   . "
	time.sleep(0.25)
	print " .   .   . ..#####,###.#####=..  .   . "
	time.sleep(0.25)
	print " .   ........######.#.######.......  . "
	time.sleep(0.25)
	print " .   ..I####D,.#####~#####~.D####O.  . "
	time.sleep(0.25)
	print " .   ...########.###.###.O#######... . "
	time.sleep(0.25)
	print " .   ...+#######O~I#,#Z~########7..  . "
	time.sleep(0.25)
	print " .   ....=#########,O=O########?..   . "
	time.sleep(0.25)
	print " .   ......########D.O########....   . "
	time.sleep(0.25)
	print " .   .   ... =#############+...  .   . "
	time.sleep(0.25)
	print " .   .   .   .....#####.......   .   . "
	time.sleep(0.25)
	print " .   .   .     ....###....   .   .   . "
	time.sleep(0.25)
	print " .   .   .   .   ..###....   .   .   . "
	time.sleep(0.25)
	print " .   .   .   .   ..### ...   .   .   . "
	time.sleep(0.25)
	print " .   .   .   .   ..### ...   .   .   . "
	time.sleep(0.25)
	print " .   .   .   .   ..### ...   .   .   . "
	time.sleep(0.25)
	print " .   .   .   .   ..### ...   .   .   . "
	time.sleep(0.25)
	print " .   .   .   .   ..###....   .   .   . "
	time.sleep(0.25)
	print " .   .   .   .   ..###....   .   .   . "
	time.sleep(0.25)
	print " .   .   .   .   #######..   .   .   . "
	time.sleep(0.25)
	print " .   .   .   ......?#$....   .   .   . "
	time.sleep(0.25)
	print " .   .   .   . .....#.....   .   .   . "
	time.sleep(0.25)
	print " .   .   .   .   .  O.   .   .   .   . "
	time.sleep(0.25)
	print "               Agri-Starts             "
	print "\n"
	time.sleep(0.5)

	print("       Switch Testing Program is running.          ")
	print(" ------------------------------------------------  ")
	print(" To check if a switch is working correctly please  ")
	print(" manually press the two switches in simultaneously ")
	print(" ------------------------------------------------  ")
    print("    To exit the program press control-c or 'q'     ")

    print "Switch Testing Program is running. \n "
    print "Please"
    while 1:

        x=sys.stdin.read(1)

        if swc[0]:
            print "Switch 1 is connected and working properly."
        if swc[1]:
            print "Switch 2 is connected and working properly."
        if swc[2]:
            print "Switch 3 is connected and working properly."
        if swc[3]:
            print "Switch 4 is connected and working properly."
        if swc[4]:
            print "Switch 5 is connected and working properly."

        if x == 'q':
            exit_gracefully()

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n) ").lower().startswith('y'):
            gpio.cleanup()
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        back.motorOff()
        sys.exit(1)

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    run_program()
