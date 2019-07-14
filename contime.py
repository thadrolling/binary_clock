# contime.py is the main (working) program that outputs the binary time in seconds
# to the 6 LED board
# the main modification needed to this program is the use of a list as
# demonstrated in blink.py -> which will greatly simplify the code
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

for x in range(0,59):
	decimal = time.strftime("%H%M%S")
	decimal_list = list(decimal)
	# print(decimal_list)
	seconds_ones = decimal_list.pop()
	seconds_tens = decimal_list.pop()
	#print('Seconds Ones in Decimal = '+ seconds_ones)
	#print("Seconds Tens in Decimal = " + seconds_tens)
	seconds_total = int(seconds_ones) + (10 * int(seconds_tens))
	# now, let's remove the 0b in front of the binary number
	seconds_total_bin = bin(seconds_total)[2:]
	# then, we need to force it to a 6 bit number (e.g. 0 = 000000)
	seconds_total_bin = seconds_total_bin.zfill(6)
	print('Total seconds = ' + str(seconds_total) + ' Binary = ' + seconds_total_bin)
	# this is where the code gets ugly
	# ideally, I would be able to spin through 'seconds_total_bin' using the index
	# from '0' to '5' and then set the LEDs in a single statement
	# the problem I have is the GPIO output numbers are all 
	# over the board (and not sequential)
	if seconds_total_bin[5] == '0':
		GPIO.output(17,GPIO.LOW)
	else:
		GPIO.output(17,GPIO.HIGH)

	if seconds_total_bin[4] == '0':
		GPIO.output(18,GPIO.LOW)
	else:
		GPIO.output(18,GPIO.HIGH)
		
	if seconds_total_bin[3] == '0':
		GPIO.output(23,GPIO.LOW)
	else:
		GPIO.output(23,GPIO.HIGH)
	
	if seconds_total_bin[2] == '0':
		GPIO.output(24,GPIO.LOW)
	else:
		GPIO.output(24,GPIO.HIGH)

	if seconds_total_bin[1] == '0':
		GPIO.output(25,GPIO.LOW)
	else:
		GPIO.output(25,GPIO.HIGH)
		
	if seconds_total_bin[0] == '0':
		GPIO.output(27,GPIO.LOW)
	else:
		GPIO.output(27,GPIO.HIGH)

	time.sleep(1)
GPIO.cleanup()