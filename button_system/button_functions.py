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


def end():
    print('\ncleaning up...')
    GPIO.cleanup()


def button_callback1(channel):
    print('button1 was pushed at: ', datetime.utcnow())
    GPIO.cleanup()


def button_callback2(channel):
    print('button2 was pushed at: ', datetime.utcnow())


def button_callback3(channel):
    print('button3 was pushed at: ', datetime.utcnow())


def button_callbackr(channel):
    print('ready button was pushed at: ', datetime.utcnow())


def button_callbacks():
    GPIO.add_event_detect(button1, GPIO.RISING, callback=button_callback1)
    GPIO.add_event_detect(button2, GPIO.RISING, callback=button_callback2)
    GPIO.add_event_detect(button3, GPIO.RISING, callback=button_callback3)
    GPIO.add_event_detect(button_ready, GPIO.RISING, callback=button_callbackr)
    time.sleep(15)
    end()


button_callbacks()
