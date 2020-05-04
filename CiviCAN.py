from threading import Thread
from c2e import c2e
import RPi.GPIO as GPIO
import time
import can
import logging
import constants
import cantools

# initialize modules
c2e = c2e.C2E(pin=constants.C2E_RELAY_PIN)

# initialize CAN bus
bus = can.Bus(
    can_filters=[{"can_id": 0x1A6, "can_mask": 0xFFF, "extended": False}])

# load DBC (CAN decoding database) file
db = cantools.database.load_file(constants.DBC_FILE_PATH)

lastBtnPress = False
btnPress = False
lastPressedTime = time.time()

for msg in bus:
    decodedMsg = db.decode_message(msg.arbitration_id, msg.data)
    # print(decodedMsg)

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
            logging.debug("C2E triggered")

        # stamp this time as the last activated time
        lastPressedTime = currentTime

    lastBtnPress = btnPress
