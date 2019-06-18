import RPi.GPIO as GPIO 
from time import sleep 

#importing the Adafruit library
import Adafruit_DHT


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)

# create an instance of the sensor type
sensor = Adafruit_DHT.AM2302

print (‘Getting data from the sensor’)

#humidity and temperature are 2 variables that store the values received from the sensor

humidity, temperature = Adafruit_DHT.read_retry(sensor,17)
print ('Temp={0:0.1f}*C humidity={1:0.1f}%'.format(temperature, humidity))


#Set the GPIO pin connected with the relay’s input pin as output in the sketch
GPIO.setup(13,GPIO.OUT)
#Set the relay pin high when the temperature is greater than 30 
if temperature > 30:
  GPIO.output(13,0) # Relay is active low
  print(‘Relay is on')
  sleep(5)
  GPIO.output(13,1) # Relay is turned off after delay of 5 seconds
