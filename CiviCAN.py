from threading import Thread
from c2e import c2e
import RPi.GPIO as GPIO
import time
import can

# initialize modules
c2e = c2e.C2E(pin=12)

# initialize CAN bus
bus = can.Bus(can_filters=[{"can_id": 0x1A6, "can_mask": 0xFFF, "extended": False}])

# GPIO to control relay
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

# initialize to OFF (active HIGH)
GPIO.output(12, GPIO.LOW)

lastBtnPress = False
btnPress = False
lastPressedTime = time.time()

for msg in bus:
    byte = msg.data[0]

    # bit test the cancel button bit
    btnPress = (byte & 0x40 == 0x40)

    # rising edge
    if (btnPress and not lastBtnPress):

        # get current timestamp
        currentTime = time.time()

        # pres btn twice within 2 seconds
        if (currentTime - lastPressedTime < 0.75):
            # double press the Cancel button
            c2e.trigger()

        # stamp this time as the last activated time
        lastPressedTime = currentTime

    lastBtnPress = btnPress
