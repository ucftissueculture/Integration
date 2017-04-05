# this is a test file it is a clone of mc.py but using
# the backend.py for function and initialization
# and a few more things I want to test out
import signal
import time
import sys
#custom made backend functions class (that probably won't work)
from back import Back

back = Back()
pins = [17, 27, 22, 0, 5]
back.initPins(pins)

def run_program():
    while 1:
        if swc:
            back.motorOff()
            back.ledOff

        else:
            back.motorOn()
            back.ledOn

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n)> ").lower().startswith('y'):
            motorRampDown()
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        motorRampDown()
        sys.exit(1)

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    run_program()
