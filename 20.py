import radio
from microbit import *
radio.on()

while True:
    if button_a.was_pressed():
        radio.send('flash')  
    incoming = radio.receive()
    if incoming == 'flash':
        display.scroll("Hi")
