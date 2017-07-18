import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
print("Module import success")

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while(True):
    GPIO.output(18, GPIO.LOW)
    time.sleep(2)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(2)
