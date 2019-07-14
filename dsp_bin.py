# This program takes user input number between 1 and 127 and then
# displays the number in binary on the LEDs

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Make a list of the GPIO numbers to use in the code
my_GPIO = [17, 18, 23, 24, 25, 27]

# set up each GPIO as OUT type
for x in my_GPIO:
	GPIO.setup(x,GPIO.OUT)
	GPIO.output(x,GPIO.LOW)

user_input = input('Enter # between 1 and 127: ')
# Need to check if user_input is an int between 1 and 127

# Next line does a lot of stuff. First, it converts 'user_input' to an int,
# then to binary and then back to string. Then, '[2:0]' strips off the leading
# '0b' and zfill(6) makes it a 6 bit number. Format of output will look like
# 000000, 000001, 000010, etc.
user_input_modified = str(bin(int(user_input)))[2:].zfill(6)
print(user_input_modified)

# Now turn on the proper LED to match user_input_modified
# the only problem with the code below is that I am going through the LEDs from
# 2^0, 2^1, 2^2, etc...but I am going through user_input_modified from
# 2^5, 2^4, 2^3, etc...need to reverse one of them!!!
y = 0
for x in my_GPIO:
	print(user_input_modified[y])
	if user_input_modified[y] == "1":
		print('light me up')
		GPIO.output(x,GPIO.HIGH)
		print('did you light up?')
	else:
		print('turn me off')
		GPIO.output(x,GPIO.LOW)
	y = y + 1

time.sleep(3)
GPIO.cleanup()




