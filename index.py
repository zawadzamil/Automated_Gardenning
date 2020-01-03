import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import urllib2
import sys
from time import sleep

WRITE_API = "7ROX59Y9F5UGC5HQ" # Replace your ThingSpeak API key here
BASEURL = 'https://api.thingspeak.com/update?api_key=%s' % WRITE_API 



SensorPrevSec = 0
SensorInterval = 2 # 2 seconds
ThingSpeakPrevSec = 0
ThingSpeakInterval = 20 # 20 seconds


channel = 21
soilpin = 18

# DHT PIN Setup
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

# LDR +LED PIN
pin_to_circuit=17
led_pin=23





# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)
GPIO.setup(soilpin,GPIO.IN)
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


def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off
    
def thingspeakth(humidity,temperature):
    if isinstance(humidity, float) and isinstance(temperature, float):
        # Formatting to two decimal places
        humi = '%.2f' % humidity                       
        temp = '%.2f' % temperature
            
        # Sending the data to thingspeak
        conn = urllib2.urlopen(BASEURL + '&field1=%s&field2=%s' % (temp, humi))
        print (conn.read())
        # Closing the connection
        conn.close()
    else:
        print ('Error')
        # DHT22 requires 2 seconds to give a reading, so make sure to add delay of above 2 seconds.
        sleep(1)
    
def thingspeakmt(pera):
         
    # Sending the data to thingspeak
    conn = urllib2.urlopen(BASEURL + '&field3=%s' % (pera))
    
    # Closing the connection
    conn.close()
    
    sleep(1)
    
    
def temp():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        if(temperature > 35):
            print("Temparature is too high")
        thingspeakth(humidity,temperature)
            
        
                    
    else:
        print("Sensor failure. Check wiring.")
        
    
    
    


if __name__ == '__main__':
    while True:
        try:
            if ((rc_time(pin_to_circuit))>=1000):
                led()
            if ((rc_time(pin_to_circuit))<1000):
                oled()
            temp()
            
            if(GPIO.input(soilpin)==GPIO.LOW):
                print("watery soil")
                motor_on(channel)
                print("Motor off")
               
                
                
                time.sleep(5)
                thingspeakmt(0)
            else:
                print("Dry Soil")
                motor_off(channel)
                print("Motor on")
               
                
                
                time.sleep(3)
                thingspeakmt(1)
            
            
            
        except KeyboardInterrupt:
            GPIO.cleanup()
          
          