import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin_to_circuit=17
led_pin=23
GPIO.setup(led_pin, GPIO.OUT)
pwm_led=GPIO.PWM(led_pin, 500)

pwm_led.start(0)
def led ():
    duty=100

    pwm_led.ChangeDutyCycle(duty)
def oled ():
    duty=0

    pwm_led.ChangeDutyCycle(duty) 
    
def rc_time (pin_to_circuit):
    count=0                                       
    GPIO.setup(pin_to_circuit,GPIO.OUT)
    GPIO.output(pin_to_circuit,GPIO.LOW)
    time.sleep(0.1)                                 
    GPIO.setup(pin_to_circuit,GPIO.IN)             
    while (GPIO.input(pin_to_circuit)==GPIO.LOW):
        count+= 1
    return count                                   
try:                                                
    while True:
        print(rc_time(pin_to_circuit))
        if ((rc_time(pin_to_circuit))>=1000):
            led()
        if ((rc_time(pin_to_circuit))<1000):
            oled()
            
        
        
        
        
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

