import RPi.GPIO as GPIO
import os
import time
import simpleaudio as sa

soundChannel = 10
movementChannel = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(soundChannel, GPIO.IN)
GPIO.setup(movementChannel, GPIO.IN)

filename = 'relaxingMusic.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)


def detectSound(channel):
    if GPIO.input(channel):
        print("Sound not Detected")
    else:
        print("Sound detected")
        os.system("curl -X POST https://maker.ifttt.com/trigger/SoundDetected/with/key/F0UrVFSWYTuvTzy-A7yT6")
        print("playing music")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print("song finished. Listening for more crying")
        time.sleep(3)
        if not GPIO.input(channel):
            print("Sound continued")
            os.system("curl -X POST https://maker.ifttt.com/trigger/SoundContinued/with/key/F0UrVFSWYTuvTzy-A7yT6")
        else:
            print("Sound has ceased")
            os.system("curl -X POST https://maker.ifttt.com/trigger/BackToSleep/with/key/F0UrVFSWYTuvTzy-A7yT6")
            
        
def detectMovement(channel):
    if GPIO.input(channel):
        print("Movement Detected:")
        time.sleep(5)
        os.system("curl -X POST https://maker.ifttt.com/trigger/MovementDetected/with/key/F0UrVFSWYTuvTzy-A7yT6")
        time.sleep(5)
    else:
        print("Movement not Detected")

        
while True:
    detectSound(soundChannel)
    detectMovement(movementChannel)
    time.sleep(1)
    
