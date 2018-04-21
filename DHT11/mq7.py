import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(21, GPIO.OUT)
 
try:
    while True:
        if GPIO.input(17):
            print(''Pas de detection'')
            time.sleep(0.2)
        if GPIO.input(17)!=1:
            print(''Detection de GAS'')
            GPIO.output(21, False)
            time.sleep(0.1)
            GPIO.output(21, True)

except KeyboardInterrupt:
    GPIO.cleanup()