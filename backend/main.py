# Main Backend program for Agri-Starts Senior Design Project

# GPIO pin values for limit switches Last one is LED
#   S1   S2   S3   S4   S5  LED
# | 11 | 13 | 15 | 27 | 29 | 37 |   Board Val
# | 17 | 27 | 22 | 00 | 05 | 26 |   BCM Val

pins = [17, 27, 22, 0, 5]

init(pins)
