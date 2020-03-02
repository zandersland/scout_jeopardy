import RPi.GPIO as GPIO
from datetime import datetime
import time

led1 = 5
led2 = 6
led3 = 13
led_white = 12
button1 = 17
button2 = 27
button3 = 22
button_ready = 23


GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_ready, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led_white, GPIO.OUT)


def current_timestamp():
    # now = datetime.now()
    # timestamp = datetime.timestamp(now)
    timestamp = datetime.utcnow()
    return timestamp


def button_callback1(channel):
    print('button1 was pushed at: ', current_timestamp())


def button_callback2(channel):
    print('button2 was pushed at: ', current_timestamp())


def button_callback3(channel):
    print('button3 was pushed at: ', current_timestamp())


def button_callbackr(channel):
    print('ready button was pushed at: ', current_timestamp())


# for x in range(1000000000):
#    if GPIO.input(22) == GPIO.HIGH:
#        print('button was pushed!', x)
try:
    for x in range(1000000000000):
        print_list = []
        if GPIO.input(button_ready) == GPIO.HIGH:
            print_list.append('buttonr ')
            GPIO.output(led_white, GPIO.HIGH)
        else:
            print_list.append('        ')
        if GPIO.input(button3) == GPIO.HIGH:
            print_list.append('button3 ')
            GPIO.output(led3, GPIO.HIGH)
        else:
            print_list.append('        ')
        if GPIO.input(button2) == GPIO.HIGH:
            print_list.append('button2 ')
            GPIO.output(led2, GPIO.HIGH)
        else:
            print_list.append('        ')
        if GPIO.input(button1) == GPIO.HIGH:
            print_list.append('button1 ')
            GPIO.output(led1, GPIO.HIGH)
        else:
            print_list.append('        ')
        print(print_list)
        time.sleep(0.05)
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(led_white, GPIO.LOW)
    # GPIO.add_event_detect(button1, GPIO.RISING, callback=button_callback1)
    # GPIO.add_event_detect(button2, GPIO.RISING, callback=button_callback2)
    # GPIO.add_event_detect(button3, GPIO.RISING, callback=button_callback3)
    # GPIO.add_event_detect(button_ready, GPIO.RISING, callback=button_callbackr)
except KeyboardInterrupt:
    print('\ncleaning up...')
    GPIO.cleanup()

# GPIO.add_event_detect(22, GPIO.RISING, callback=button_callback1)
# GPIO.add_event_detect(22, GPIO.FALLING, callback=button_callback2)


# message = input('press enter to quit')
