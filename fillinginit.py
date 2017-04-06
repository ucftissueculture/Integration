import mraa
import time

ON = 0
OFF = 1

wand1 = mraa.Gpio(xxxx)
wand2 = mraa.Gpio(xxxx)
wand3 = mraa.Gpio(xxxx)
wand4 = mraa.Gpio(xxxx)
wand5 = mraa.Gpio(xxxx)

wand1.dir(mraa.DIR_OUT)
wand2.dir(mraa.DIR_OUT)
wand3.dir(mraa.DIR_OUT)
wand4.dir(mraa.DIR_OUT)
wand5.dir(mraa.DIR_OUT)

wand1.write(OFF)
wand2.write(OFF)
wand3.write(OFF)
wand4.write(OFF)
wand5.write(OFF)