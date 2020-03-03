import RPi.GPIO as GPIO
from datetime import datetime
import time


# led1 = 5
# led2 = 6
# led3 = 13
# led_white = 12
button1 = 17
button2 = 27
button3 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(led1, GPIO.OUT)
# GPIO.setup(led2, GPIO.OUT)
# GPIO.setup(led3, GPIO.OUT)
# GPIO.setup(led_white, GPIO.OUT)


def button_callbacks(player_list=(False, False, False), timer=10):
    def end():
        print('\ncleaning up...')
        GPIO.cleanup()

    class player:
        first_player = ''

    def button_callback1(channel):
        print('button1 was pushed at: ', datetime.utcnow())
        player.first_player = 'Team1'
        end()

    def button_callback2(channel):
        print('button2 was pushed at: ', datetime.utcnow())
        player.first_player = 'Team2'
        end()

    def button_callback3(channel):
        print('button3 was pushed at: ', datetime.utcnow())
        player.first_player = 'Team3'
        end()


    if player_list[0]:
        GPIO.add_event_detect(button1, GPIO.RISING, callback=button_callback1)
    if player_list[1]:
        GPIO.add_event_detect(button2, GPIO.RISING, callback=button_callback2)
    if player_list[2]:
        GPIO.add_event_detect(button3, GPIO.RISING, callback=button_callback3)

    for x in range(timer * 100):
        if player.first_player != '':
            end()
            break
        else:
            time.sleep(0.01)
    print('ending...')
    end()
    return player.first_player


if __name__ == '__main__':
    button_callbacks((True, True, False))
