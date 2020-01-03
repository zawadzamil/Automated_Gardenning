import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(21,GPIO.IN)
while True:
	if(GPIO.input(21)==GPIO.LOW):
	    print("watery soil")
	else:
	    print("Dry Soil")
	time.sleep(1)
		