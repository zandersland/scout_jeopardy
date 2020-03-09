#! ../venv/bin/python3
import os
import time
from datetime import datetime

import RPi.GPIO as GPIO
import generate_game as gg
import generate_game_json as ggj
import update_game_json as ug
from flask import Flask, render_template, request, redirect, url_for
from rpi_ws281x import PixelStrip, Color

game_stats = gg.GenerateGame()
app = Flask(__name__)


class jsonVar:
    game_json_file = ''
    answer = 'Program restarted'
    json_file_def_var = False
    question = 'Program restarted'


def return_list_of_files_in_games():
    games = ['None']
    for line in os.listdir('games'):
        games.append(line)
    return games


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    jsonVar.answer = 'Game start, waiting for game select...'
    jsonVar.question = 'Game start, waiting for game select...'
    games = return_list_of_files_in_games()
    return render_template('index.html', games=games)


# TODO work on adding scores after final
# TODO make team color brighter on board
# TODO "aterisk" box on admin page
# TODO make clock bigger
# TODO show final jeopardy image/text before category
# TODO see final answers on admin page after reload
# TODO final jeopardy click to advance through 'slides'
# TODO see if i can put an image instead of text as a question
# TODO come up with more questions

# lower score

# TODO NICETOHAVE make log
# TODO NICETOHAVE use javascript to switch between dropdown and textbox for game selection


@app.route('/generate_game', methods=['POST'])
def generate_game():
    print('|' + str(request.form.get('dropdown-option')) + '|')
    if "None" == str(request.form.get('dropdown-option')):
        print('generate true')
        jsonVar.game_json_file = request.form.get('file_name') + '.json'
        ggj.generate_game_4(jsonVar.game_json_file)
    else:
        print('generate false')
        jsonVar.game_json_file = request.form.get('dropdown-option')
    jsonVar.answer = 'Waiting for question...'
    jsonVar.question = 'Waiting for question...'
    return redirect(url_for('game'))


@app.route('/game')
def game():
    if ug.read_current_round(jsonVar.game_json_file) == 3:
        jsonVar.answer = 'On Final Round...'
        jsonVar.question = 'On Final Round...'
        return redirect('/final')
    return render_template('game.html', game_json=ug.return_full_json(jsonVar.game_json_file),
                           team_one_points=ug.read_team_score('Team1', jsonVar.game_json_file),
                           team_two_points=ug.read_team_score('Team2', jsonVar.game_json_file),
                           team_three_points=ug.read_team_score('Team3', jsonVar.game_json_file),
                           current_round=ug.read_current_round(jsonVar.game_json_file),
                           game_json_file=jsonVar.game_json_file,
                           current_team_highlight=ug.read_current_team_highlight(jsonVar.game_json_file))


def set_json_variable(set_var):
    if jsonVar.json_file_def_var:
        try:
            if '.json' in set_var:
                jsonVar.game_json_file = str(set_var)
                return jsonVar.game_json_file
            else:
                return None
        except:
            return None


def turn_off_strip_and_leds():
    LED_COUNT = 60
    LED_PIN = 12
    LED_FREQ_HZ = 800000
    LED_DMA = 10
    LED_BRIGHTNESS = 200
    LED_INVERT = False
    LED_CHANNEL = 0

    led1 = 5
    led2 = 6
    led3 = 13
    led_white = 16

    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    GPIO.setup(led3, GPIO.OUT)
    GPIO.setup(led_white, GPIO.OUT)

    for x in range(strip.numPixels()):
        strip.setPixelColor(x, Color(0, 0, 0))
    strip.show()

    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(led3, GPIO.LOW)
    GPIO.output(led_white, GPIO.LOW)
    GPIO.cleanup()


@app.route('/update_game', methods=['POST'])
def update_game():
    game_json_file = set_json_variable(request.args.get('game_json_file', None))
    if request.form.get('team_one') is not None and request.form.get('team_one') != '':
        if ug.read_team_score('Team1', jsonVar.game_json_file) < int(request.form.get('team_one')) + ug.read_team_score(
                'Team1', jsonVar.game_json_file):
            ug.update_current_team_highlight(jsonVar.game_json_file, 1)
        ug.update_team_scores('Team1', int(request.form.get('team_one', 0)), jsonVar.game_json_file)

    if request.form.get('team_two') is not None and request.form.get('team_two') != '':
        if ug.read_team_score('Team2', jsonVar.game_json_file) < int(request.form.get('team_two')) + ug.read_team_score(
                'Team2', jsonVar.game_json_file):
            ug.update_current_team_highlight(jsonVar.game_json_file, 2)
        ug.update_team_scores('Team2', int(request.form.get('team_two', 0)), jsonVar.game_json_file)

    if request.form.get('team_three') is not None and request.form.get('team_three') != '':
        if ug.read_team_score('Team3', jsonVar.game_json_file) < int(
                request.form.get('team_three')) + ug.read_team_score('Team3', jsonVar.game_json_file):
            ug.update_current_team_highlight(jsonVar.game_json_file, 3)
        ug.update_team_scores('Team3', int(request.form.get('team_three', 0)), jsonVar.game_json_file)

    ug.update_display_question(int(request.args.get('column_position')), int(request.args.get('row_position')),
                               False, jsonVar.game_json_file)

    ug.add_line_to_log(jsonVar.game_json_file,
                       f'Updating team scores: Team1={ug.read_team_score("Team1", jsonVar.game_json_file)}, '
                       f'Team2={ug.read_team_score("Team2", jsonVar.game_json_file)}, '
                       f'Team3={ug.read_team_score("Team3", jsonVar.game_json_file)}')
    ug.add_line_to_log(jsonVar.game_json_file,
                       f'Updating game: column_position={request.args.get("column_position")}, '
                       f'row_position={request.args.get("row_position")}, set_to=False')

    jsonVar.answer = 'Waiting for question...'
    jsonVar.question = 'Waiting for question...'

    turn_off_strip_and_leds()

    if ug.check_for_round_end(jsonVar.game_json_file):
        ug.change_current_round(ug.read_current_round(jsonVar.game_json_file) + 1, jsonVar.game_json_file)

    return redirect(url_for('game', game_json_file=game_json_file))


class player:
    first_player = 'TeamNone'


def button_functions():
    LED_COUNT = 60
    LED_PIN = 12
    LED_FREQ_HZ = 800000
    LED_DMA = 10
    LED_BRIGHTNESS = 200
    LED_INVERT = False
    LED_CHANNEL = 0
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    player_list = ug.read_team_guesses(jsonVar.game_json_file)
    timer = 10

    led1 = 5
    led2 = 6
    led3 = 13
    led_white = 16
    button1 = 17
    button2 = 27
    button3 = 22

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    GPIO.setup(led3, GPIO.OUT)
    GPIO.setup(led_white, GPIO.OUT)

    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    GPIO.output(led3, GPIO.LOW)
    GPIO.output(led_white, GPIO.LOW)

    def set_strip_to_color(strip_color):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, strip_color)
        strip.show()

    def end():
        print('\ncleaning up...')
        GPIO.cleanup()

    def button_callback1(channel):
        print('button1 was pushed at: ', datetime.utcnow())
        player.first_player = 'Team1'
        GPIO.output(led1, GPIO.HIGH)
        set_strip_to_color(Color(255, 0, 0))

    def button_callback2(channel):
        print('button2 was pushed at: ', datetime.utcnow())
        player.first_player = 'Team2'
        GPIO.output(led2, GPIO.HIGH)
        set_strip_to_color(Color(0, 255, 0))

    def button_callback3(channel):
        print('button3 was pushed at: ', datetime.utcnow())
        player.first_player = 'Team3'
        GPIO.output(led3, GPIO.HIGH)
        set_strip_to_color(Color(0, 0, 255))

    if player_list[0]:
        GPIO.add_event_detect(button1, GPIO.RISING, callback=button_callback1)
    if player_list[1]:
        GPIO.add_event_detect(button2, GPIO.RISING, callback=button_callback2)
    if player_list[2]:
        GPIO.add_event_detect(button3, GPIO.RISING, callback=button_callback3)
    player.first_player = 'TeamNone'
    set_strip_to_color(Color(100, 100, 100))
    GPIO.output(led_white, GPIO.HIGH)
    for x in range(timer * 100):
        if player.first_player != 'TeamNone':
            GPIO.output(led_white, GPIO.LOW)
            end()
            break
        else:
            time.sleep(0.01)
    print('ending...')
    if player.first_player == 'TeamNone':
        set_strip_to_color(Color(0, 0, 0))
        strip.show()
    end()
    print(player.first_player)
    ug.update_first_player(jsonVar.game_json_file, player.first_player)
    return player.first_player


@app.route('/answer', methods=['POST'])
def answer():
    game_json_file = set_json_variable(request.args.get('game_json_file', None))
    points = request.args.get('points')
    _answer = request.args.get('answer')
    question = request.args.get('question')
    jsonVar.answer = _answer
    jsonVar.question = question
    column_position = request.args.get('column_position')
    row_position = request.args.get('row_position')
    display = request.args.get('display')
    daily_double = request.args.get('daily_double')
    ug.add_line_to_log(jsonVar.game_json_file,
                       f"points={points}, column_position={column_position}, row_position={row_position}, daily_double={daily_double}")
    ug.reset_team_guesses(jsonVar.game_json_file)
    # first_player = button_functions()
    # time.sleep(15)
    return render_template('answer.html', points=points, answer=_answer, question=question,
                           column_position=column_position,
                           display=display, row_position=row_position, daily_double=daily_double,
                           game_json_file=game_json_file,
                           current_team_highlight=ug.read_current_team_highlight(jsonVar.game_json_file))


@app.route('/final')
def final():
    game_json_file = set_json_variable(request.args.get('game_json_file', None))
    _final = ug.get_final_jeopardy(jsonVar.game_json_file)
    one = ug.read_team_score('Team1', jsonVar.game_json_file)
    two = ug.read_team_score('Team2', jsonVar.game_json_file)
    three = ug.read_team_score('Team3', jsonVar.game_json_file)
    return render_template('final.html', final=_final, one=one, two=two, three=three, game_json_file=game_json_file)


# @app.route('/game_result', methods=['POST'])
# def game_result():
#     game_json_file = set_json_variable(request.args.get('game_json_file', None))
#     _final = ug.get_final_jeopardy(jsonVar.game_json_file)
#     one = ug.read_team_score('Team1', jsonVar.game_json_file)
#     two = ug.read_team_score('Team2', jsonVar.game_json_file)
#     three = ug.read_team_score('Team3', jsonVar.game_json_file)

#     one_answer = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_one_answer')
#     one_wager = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_one_wager')
#     two_answer = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_two_answer')
#     two_wager = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_two_wager')
#     three_answer = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_three_answer')
#     three_wager = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_three_wager')
#     return render_template('game_result.html', final=_final, one=one, two=two, three=three, one_answer=one_answer,
#                            one_wager=one_wager, two_answer=two_answer, two_wager=two_wager, three_answer=three_answer,
#                            three_wager=three_wager, game_json_file=game_json_file)


@app.route('/game_result', methods=['POST'])
def game_result():
    game_json_file = set_json_variable(request.args.get('game_json_file', None))
    _final = ug.get_final_jeopardy(jsonVar.game_json_file)
    one = ug.read_team_score('Team1', jsonVar.game_json_file)
    two = ug.read_team_score('Team2', jsonVar.game_json_file)
    three = ug.read_team_score('Team3', jsonVar.game_json_file)

    one_answer = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_one_answer')
    one_wager = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_one_wager')
    two_answer = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_two_answer')
    two_wager = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_two_wager')
    three_answer = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_three_answer')
    three_wager = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_three_wager')

    dict1 = {'one': one, 'two': two, 'three': three}
    st1 = str(min(dict1, key=dict1.get))
    del dict1[f'{min(dict1, key=dict1.get)}']
    st2 = str(min(dict1, key=dict1.get))
    del dict1[f'{min(dict1, key=dict1.get)}']
    st3 = str(min(dict1, key=dict1.get))

    dict1['one'] = {'score': one, 'answer': 'Team 1 answer: ' + one_answer, 'wager': 'Team 1 wager: ' + one_wager}
    dict1['two'] = {'score': two, 'answer': 'Team 2 answer: ' + two_answer, 'wager': 'Team 2 wager: ' + two_wager}
    dict1['three'] = {'score': three, 'answer': 'Team 3 answer: ' + three_answer, 'wager': 'Team 3 wager: ' + three_wager}
    dict1['order'] = [st1, st2, st3]
    return_list = [dict1[st1]['answer'], dict1[st1]['wager'], dict1[st2]['answer'], dict1[st2]['wager'],
                   dict1[st3]['answer'], dict1[st3]['wager']]

    return render_template('game_result_2.html', final=_final, one=one, two=two, three=three, one_answer=one_answer,
                           one_wager=one_wager, two_answer=two_answer, two_wager=two_wager, three_answer=three_answer,
                           three_wager=three_wager, game_json_file=game_json_file, game_list=return_list, zip=zip)


@app.route('/record_final_answers', methods=['POST'])
def record_final_answers():
    ug.update_final_jeopardy(jsonVar.game_json_file, 'team_one_wager', request.form.get('team_one_wager'))
    ug.update_final_jeopardy(jsonVar.game_json_file, 'team_two_wager', request.form.get('team_two_wager'))
    ug.update_final_jeopardy(jsonVar.game_json_file, 'team_three_wager', request.form.get('team_three_wager'))

    ug.update_final_jeopardy(jsonVar.game_json_file, 'team_one_answer', request.form.get('team_one_answer'))
    ug.update_final_jeopardy(jsonVar.game_json_file, 'team_two_answer', request.form.get('team_two_answer'))
    ug.update_final_jeopardy(jsonVar.game_json_file, 'team_three_answer', request.form.get('team_three_answer'))

    ug.add_line_to_log(jsonVar.game_json_file,
                       f"Final wager/answers: {request.form.get('team_one_wager')} {request.form.get('team_one_answer')}, "
                       f"{request.form.get('team_two_wager')} {request.form.get('team_two_answer')}, "
                       f"{request.form.get('team_three_wager')} {request.form.get('team_three_answer')}")

    return redirect(url_for('main_admin_page_post'))


@app.route('/record_final')
def record_final():
    game_json_file = set_json_variable(request.args.get('game_json_file', None))
    return render_template('record_final.html', game_json_file=game_json_file)


# @app.route('/log')
# def log():
#     return render_template('log.html', log=game_stats.log)


# @app.route('/update_scores_post', methods=['POST'])
# def update_scores_post():
#     with open('game_json.json', 'r') as _f:
#         _game_json = json.loads(_f.read())
#     game_stats.team_one_points = int(request.form.get('team_one_amount'))
#     _game_json['scores']['Team1'] = int(request.form.get('team_one_amount'))
#     game_stats.team_two_points = int(request.form.get('team_two_amount'))
#     _game_json['scores']['Team2'] = int(request.form.get('team_two_amount'))
#     game_stats.team_three_points = int(request.form.get('team_three_amount'))
#     _game_json['scores']['Team3'] = int(request.form.get('team_three_amount'))
#     with open('game_json.json', 'w') as _f:
#         _f.write(json.dumps(_game_json, indent=2))
#     game_stats.log_game(f"Updated team scores: "
#                         f"team one:   {game_stats.team_one_points}"
#                         f"team two:   {game_stats.team_two_points}"
#                         f"team three: {game_stats.team_three_points}")
#     return redirect(url_for('log'))
#
#
# @app.route('/update_scores')
# def update_scores():
#     one = ug.read_team_score('Team1', jsonVar.game_json_file)
#     two = ug.read_team_score('Team2', jsonVar.game_json_file)
#     three = ug.read_team_score('Team3', jsonVar.game_json_file)
#     return render_template('update_scores.html', one=one, two=two, three=three)


@app.route('/main_admin_page')
def main_admin_page():
    return render_template('main_admin.html')


@app.route('/main_admin_page_post', methods=['GET', 'POST'])
def main_admin_page_post():
    if request.method == 'POST':
        ug.set_team_score(jsonVar.game_json_file, 'Team1', int(request.form.get('team_one_amount')))
        ug.set_team_score(jsonVar.game_json_file, 'Team2', int(request.form.get('team_two_amount')))
        ug.set_team_score(jsonVar.game_json_file, 'Team3', int(request.form.get('team_three_amount')))
        ug.change_current_round(int(request.form.get('current_round')), jsonVar.game_json_file)
        ug.add_line_to_log(jsonVar.game_json_file,
                           f'Admin Override: Team1 new score={request.form.get("team_one_amount")}, '
                           f'Team2 new score={request.form.get("team_two_amount")}, '
                           f'Team3 new score={request.form.get("team_three_amount")}, '
                           f'New Round number={request.form.get("current_round")}')
    if jsonVar.game_json_file is not '':
        one = ug.read_team_score('Team1', jsonVar.game_json_file)
        two = ug.read_team_score('Team2', jsonVar.game_json_file)
        three = ug.read_team_score('Team3', jsonVar.game_json_file)
        round_num = ug.read_current_round(jsonVar.game_json_file)
    else:
        one = None
        two = None
        three = None
        round_num = None
    if jsonVar.game_json_file is not '':
        one_answer = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_one_answer')
        one_wager = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_one_wager')
        two_answer = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_two_answer')
        two_wager = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_two_wager')
        three_answer = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_three_answer')
        three_wager = ug.get_entry_in_final_jeopardy(jsonVar.game_json_file, 'team_three_wager')
    else:
        one_answer = None
        one_wager = None
        two_answer = None
        two_wager = None
        three_answer = None
        three_wager = None

    return render_template('includes/main_admin_page_controls_ping.html', one=one, two=two, three=three,
                           round_num=round_num, one_answer=one_answer, one_wager=one_wager, two_answer=two_answer,
                           two_wager=two_wager, three_answer=three_answer,
                           three_wager=three_wager)


@app.route('/main_admin_page_log_ping', methods=['GET', 'POST'])
def main_admin_page_log_ping():
    if jsonVar.game_json_file is not '':
        log_list = ug.read_log(jsonVar.game_json_file)
    else:
        log_list = []
    if jsonVar.game_json_file == '':
        _game_json_file = 'No file selected'
    else:
        _game_json_file = 'Current file: ' + jsonVar.game_json_file
    return render_template('includes/main_admin_page_log_ping.html', log_list=reversed(log_list),
                           game_json_file=_game_json_file)


@app.route('/main_admin_page_answer_ping', methods=['GET', 'POST'])
def main_admin_page_answer_ping():
    return render_template('includes/main_admin_page_answer_ping.html', answer=jsonVar.answer)


@app.route('/main_admin_page_question_ping', methods=['GET', 'POST'])
def main_admin_page_question_ping():
    return render_template('includes/main_admin_page_question_ping.html', question=jsonVar.question)


@app.route('/pingtest', methods=['GET', 'POST'])
def pingtest():
    print('ping test was pinged')
    return render_template('button_status_iframe.html', first_player=player.first_player)


@app.route('/start_buttons_ping', methods=['GET', 'POST'])
def start_buttons_ping():
    # TODO start reading the buttons without a certain team
    # TODO test <iframe> to see if I can have a reloading element
    if request.args.get('team_id') is not None:
        ug.update_team_guesses(jsonVar.game_json_file, request.args.get('team_id'))
    print(f'Team {request.args.get("team_id")} got the answer wrong. Now allowing '
          f'{ug.read_team_guesses(jsonVar.game_json_file)} another chance to buzz in.')
    player.first_player = button_functions()
    return render_template('button_status_iframe.html', first_player=player.first_player)


@app.route('/reset_buttons', methods=['GET', 'POST'])
def reset_buttons():
    ug.reset_team_guesses(jsonVar.game_json_file)
    player.first_player = button_functions()
    return redirect(url_for('main_admin_page_post'))


@app.route('/turn_off_leds', methods=['GET', 'POST'])
def turn_off_leds():
    turn_off_strip_and_leds()
    return redirect(url_for('main_admin_page_post'))


@app.route('/admin_aterisk_page', methods=['GET', 'POST'])
def admin_aterisk_page():
    if jsonVar.game_json_file is not '':
        current_player = ug.read_current_team_highlight(jsonVar.game_json_file)
    else:
        current_player = 0
    return render_template('admin_aterisk_page.html', current_player=current_player)


@app.route('/fireworks', methods=['GET', 'POST'])
def fireworks():
    print('\n\n\n++++++++++++++++++++++++++++++\n+++                        +++\n+++     FIREWORKS!!!!!     +++\n'
          '+++                        +++\n++++++++++++++++++++++++++++++\n\n')
    return '<br>++++++++++++++++++++++++++++++<br>+++<br>+++     FIREWORKS!!!!!     ' \
           '+++<br>+++<br>++++++++++++++++++++++++++++++ '


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)
