import RPi.GPIO as GPIO
import Adafruit_DHT
import time

GPIO.setmode(GPIO.BCM)

 
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
led_pin_red=18
led_pin_yallow=24

GPIO.setup(led_pin_red, GPIO.OUT)
GPIO.setup(led_pin_yallow, GPIO.OUT)


pwm_led_r=GPIO.PWM(led_pin_red, 500)
pwm_led_y=GPIO.PWM(led_pin_yallow, 500)

pwm_led_r.start(100)
pwm_led_y.start(100)

def red_led():
    duty=100
    
    pwm_led_r.ChangeDutyCycle(duty)
    pwm_led_y.ChangeDutyCycle(0)
    
def y_led():
    duty=100
    
    pwm_led_y.ChangeDutyCycle(duty)
    pwm_led_r.ChangeDutyCycle(0)

 
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        if(temperature>20):
            red_led()
        else:
            y_led()
            
        
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(3)



