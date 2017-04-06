# basic Logic for backend mostly thinking probably wont actually
# use this file for anything other than working out the followed

# GPIO pin values

#   S1   S2   S3   S4   S5   LED
# | 11 | 13 | 15 | 27 | 29 | 37 |   Board Val
# | 17 | 27 | 22 | 00 | 05 | 26 |   BCM Val

# filling gpio pins
#   W1   W2   W3   W4   W5
# | xx | XX | xx | xx | xx |    Board Val
# | xx | XX | xx | xx | xx |    BCM Val


# imports that will be needed
import back

# class tray(object):
#     self.isFilled = False
#     self.isCapped = False
#     self.endLine = False


# if switches 1 & 2 on pin x is pressed:
    # back.motorOff()
    # tray++
    # instantiate new tray
    # secondary placement check?
    # begin filling
    # set isFilled = True
    # motorRampUp




# if switches 3 & 4:
    # set flag for current tray at position
    # if this was capping set isCapped to True

# if final switches pressed:
    # motorRampDown
    # set endLine = True
    # trayCount++
WIP on master
