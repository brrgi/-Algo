from microbit import *

uart.init(115200)

while 1:
    uart.write("Hello")
    sleep(1000)
