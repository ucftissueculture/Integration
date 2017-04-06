## Backend/main.py
# Main Backend program for Agri-Starts Senior Design Project

# GPIO pin values

#   S1   S2   S3   S4   S5   LED
# | 11 | 13 | 15 | 27 | 29 | 37 |   Board Val
# | 17 | 27 | 22 | 00 | 05 | 26 |   BCM Val

# filling gpio pins
#   W1   W2   W3   W4   W5
# | xx | XX | xx | xx | xx |    Board Val
# | xx | XX | xx | xx | xx |    BCM Val

pins = [17, 27, 22, 0, 5]

init(pins)

def run_program():
    ## main program will go here

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
