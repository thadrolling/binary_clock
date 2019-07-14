import RPi.GPIO as GPIO
import time
from decimal import Decimal
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

#print "LED on"
#GPIO.output(18,GPIO.HIGH)
#print "LED off"
#GPIO.output(18,GPIO.LOW)

our_time = time.localtime()
new_time = time.strftime("%H%M", our_time)
#print(new_time)
#print('\n')

print("Here are the current ten seconds:")

for i in range(1,10):
    our_time = time.localtime()
    new_time_sec = time.strftime("%S", our_time)
    new_time_sec_integer = int(new_time_sec)
    new_time_sec_binary = bin(new_time_sec_integer)
    new_time_sec_binstring = str(new_time_sec_binary)
    print(new_time_sec_integer)
    print(new_time_sec_binary)
    print('\n')
    #print (new_time_sec)
    time.sleep(1)

GPIO.cleanup()




