import mraa
import time

ON = 0
OFF = 1

duration = 4

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

wand1.write(ON)
wand2.write(ON)
wand3.write(ON)
wand4.write(ON)
wand5.write(ON)

time.sleep(duration)

wand1.write(OFF)
wand2.write(OFF)
wand3.write(OFF)
wand4.write(OFF)
wand5.write(OFF)