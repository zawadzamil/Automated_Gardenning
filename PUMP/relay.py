import RPi.GPIO as GPIO
import time

channel = 21

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off


if __name__ == '__main__':
    while(True):
        try:
            motor_on(channel)
            print("Motor off")
            time.sleep(5)
            motor_off(channel)
            print("Motor on")
            time.sleep(5)
           
        except KeyboardInterrupt:
            GPIO.cleanup()
