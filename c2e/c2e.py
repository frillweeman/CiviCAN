import os
from time import sleep
import threading
import RPi.GPIO as GPIO
from pydub import AudioSegment
from pydub.playback import play


class C2E:
    audioFile = AudioSegment.from_wav(os.path.join(
        os.path.dirname(__file__), "activating-gate.wav"))

    def _playAudioAsync(self):
        threading.Thread(target=play, args=(self.audioFile,)).start()

    def __init__(self, pin):
        self.pin = pin

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)

        # initialize relay to off (active high)
        GPIO.output(pin, GPIO.LOW)

    def trigger(self):
        # play gate message in a new thread
        self._playAudioAsync()

        # activate relay several times
        for i in range(4):
            GPIO.output(self.pin, GPIO.HIGH)
            sleep(2)
            GPIO.output(self.pin, GPIO.LOW)
            sleep(0.5)
