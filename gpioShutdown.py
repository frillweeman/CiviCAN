import RPI.GPIO as GPIO
import time
import os
import constants

GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def shutdown():
    print("shutting down")
    os.system("shutdown now")


lastCarOff = False
startTime = 0.0


def loop():
    while(1):
        isCarOff = GPIO.input(5)

        if (isCarOff):
            if (not lastCarOff):
                # start timer
                startTime = time.time()
                print("Car is off. Shutdown timer started.")
            else:
                # compare
                et = time.time() - startTime
                print(f"elapsed: {et}s")
                if (et > constants.SHUTDOWN_TIMER):
                    shutdown()

        lastCarOff = isCarOff
        time.sleep(1)
