import time
import json

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setwarnings(False)   
def readPort(port):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(port, GPIO.OUT)
    result = {}
    result['port'] = port
    result['status'] = GPIO.input(port)
    #GPIO.cleanup()
    return result

def readPorts(ports):
    portStatusList = []
    for port in ports :
        portStatusList.append(readPort(port))
    result = {}
    result['data'] = portStatusList
    return  result

def setPortOutput(port, status):
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(port, GPIO.OUT)
     if status == 0:
         GPIO.output(port, GPIO.LOW)
     else:
         GPIO.output(port, GPIO.HIGH)
     #GPIO.cleanup()

#ports = [18, 19]
#setPortOutput(18, 1)
#print readPorts(ports)



    
    
