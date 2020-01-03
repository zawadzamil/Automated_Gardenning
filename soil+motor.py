import RPi.GPIO as GPIO
import time

channel = 21
soilpin = 18

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)
GPIO.setup(soilpin,GPIO.IN)


def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off
    


if __name__ == '__main__':
    while True:
        try:
            if(GPIO.input(soilpin)==GPIO.LOW):
                print("watery soil")
                motor_off(channel)
                print("Motor off")
                time.sleep(5)
            else:
                print("Dry Soil")
                motor_on(channel)
                print("Motor on")
                time.sleep(5)
            time.sleep(1)
            
        except KeyboardInterrupt:
            GPIO.cleanup()
		
    
    

