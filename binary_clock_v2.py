# TGR's binary clock code 10/18/2021
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# GPIO 11-15 is for "hours"
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
# GPIO 16-21 is for "minutes"
GPIO.setup(16,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
# GPIO 22-27 is for "seconds"
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
for x in range(0,31):

    # get the current hours/min/secs and convert to binary strings
    current_time_hr = bin(int(time.strftime("%H")))
    current_time_min = bin(int(time.strftime("%M")))
    current_time_sec = bin(int(time.strftime("%S")))
    # strip the leading "0b" from the strings and force to 6 digits
    current_time_hr = current_time_hr[2:].zfill(6)
    current_time_min = current_time_min[2:].zfill(6)
    current_time_sec = current_time_sec[2:].zfill(6)
    # create the 18 digit binary time string
    current_time_bin = current_time_hr + current_time_min + current_time_sec

    print(time.strftime("%H%M%S"))
    #print(current_time_hr)
    #print(current_time_min)
    #print(current_time_sec)
    #print(current_time_bin)
    #print("\n")

    # start at GPIO_PIN = 11 and go thru GPIO_PIN 27
    gpio_pin = 11
    # starting at the SECOND bit in current_time_bin
    # (remember, we set hours to 6 bits above but it will only
    # be 5 bits max...23 hrs is 10111)
    # loop through and set GPIO to high/low as appropriate
    for y in range(1,18):
        print(gpio_pin)
        if current_time_bin[y] == '1':
            print('1')
            GPIO.output(gpio_pin,GPIO.HIGH)
        else:
            print('0')
            GPIO.output(gpio_pin,GPIO.LOW)
        gpio_pin = gpio_pin + 1
        y = y + 1

    time.sleep(1)
GPIO.cleanup()
