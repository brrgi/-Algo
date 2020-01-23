from microbit import *

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "face up":
        display.show(Image.HAPPY)
    elif gesture == "face down":
        display.show(Image.HEART)
    elif gesture == "up":
        display.show(Image.HEART_SMALL)
    elif gesture == "left":
        display.show(Image.SAD)
    elif gesture == "right":
        display.show(Image.ANGRY)
    else:
        display.show(Image.SILLY)
