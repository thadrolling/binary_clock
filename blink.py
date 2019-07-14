# Simple program that does this:
#   1) turns ON all 6 LEDs one at a time
#   2) turns OFF all 6 LEDs one at a time
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Make a list of the GPIO numbers to use in the code
my_GPIO = [17, 18, 23, 24, 25, 27]

# set up each GPIO as OUT type
for x in my_GPIO:
	GPIO.setup(x,GPIO.OUT)

print "Turn on all LED one at a time (and don't turn off)"
for x in my_GPIO:
	GPIO.output(x,GPIO.HIGH)
	time.sleep(1)

print "Now, turn the off one at a time"
for x in my_GPIO:
	GPIO.output(x,GPIO.LOW)
	time.sleep(1)

GPIO.cleanup()




