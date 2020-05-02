import RPi.GPIO as GPIO
import time
import os
import constants
import logging

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

logging.basicConfig(level = logging.DEBUG)

def shutdown():
    logging.debug("shutting down")
    os.system("sudo shutdown now")


lastCarOff = False
startTime = 0.0

logging.debug("running shutdown script")

while(1):
    isCarOff = GPIO.input(5)

    if (isCarOff):
        if (not lastCarOff):
            # start timer
            startTime = time.time()
            logging.debug("Car is off. Shutdown timer started.")
        else:
            # compare
            et = time.time() - startTime
            logging.debug("elapsed: %d of %d seconds" % (et, constants.SHUTDOWN_TIMER))
            if (et > constants.SHUTDOWN_TIMER):
                shutdown()

    if (not isCarOff and lastCarOff):
        logging.debug("shutdown canceled")

    lastCarOff = isCarOff
    time.sleep(1)
