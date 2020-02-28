import json
import os

from flask import render_template, request, redirect, url_for

from application import app
from application import generate_game as gg
from application import generate_game_json as ggj
from application import update_game_json as ug

game_stats = gg.GenerateGame()


def return_list_of_files_in_games():
    games = ['None']
    for line in os.listdir('games'):
        games.append(line)
    return games


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    games = return_list_of_files_in_games()
    return render_template('index.html', games=games)


# TODO make log
# TODO add a drop down on main page to recover a game
# TODO make team color light up after they answer correctly
# TODO fix the words from going off screen when there is a daily_double
# TODO work on final jeopardy


# @app.route('/generate_game', methods=['POST'])
# def generate_game():
#     game_stats.log_game('Creating game')
#     game_stats.generate_game(request.form.get('dropdown-option', ''))
#     game_stats.log_game(f'Round {game_stats.round}')
#     return render_template('game.html', gameData=game_stats.game_data,
#                            team_one_points=game_stats.team_one_points,
#                            team_two_points=game_stats.team_two_points, team_three_points=game_stats.team_three_points)


@app.route('/generate_game', methods=['POST'])
def generate_game():
    print(request.form.get('dropdown-option'))
    if request.form.get('dropdown-option') == 'None':
        ggj.generate_game_4(request.form.get('file_name'))
        ug.move_archived_game_to_current_state(request.form.get('file_name'))
    else:
        ug.move_archived_game_to_current_state(request.form.get('dropdown_option'))
    # TODO fix this
    return redirect(url_for('game'))


# @app.route('/game')
# def game():
#     return render_template('game.html', gameData=game_stats.game_data,
#                            team_one_points=game_stats.team_one_points,
#                            team_two_points=game_stats.team_two_points, team_three_points=game_stats.team_three_points)


@app.route('/game')
def game():
    return render_template('game.html', game_json=ug.return_full_json(),
                           team_one_points=ug.read_team_score('Team1'),
                           team_two_points=ug.read_team_score('Team2'), team_three_points=ug.read_team_score('Team3'),
                           current_round=ug.read_current_round())


# @app.route('/update_game', methods=['POST'])
# def update_game():
#     _index = int(request.args.get('index')) - 1
#     if request.form.get('team_one') is not None and request.form.get('team_one') != '':
#         game_stats.team_one_points += int(request.form.get('team_one', 0))
#     if request.form.get('team_two') is not None and request.form.get('team_two') != '':
#         game_stats.team_two_points += int(request.form.get('team_two', 0))
#     if request.form.get('team_three') is not None and request.form.get('team_three') != '':
#         game_stats.team_three_points += int(request.form.get('team_three', 0))
#
#     game_stats.log_game(
#         f"  Points:   One: {request.form.get('team_one')}, "
#         f"  Two: {request.form.get('team_two')}, "
#         f"  Three: {request.form.get('team_three')}")
#     game_stats.log_game(f"  Scores:   One: {game_stats.team_one_points}, "
#                         f"  Two: {game_stats.team_two_points}, "
#                         f"  Three: {game_stats.team_three_points}")
#     clear_question = (
#         game_stats.game_data[_index][0], game_stats.game_data[_index][1], game_stats.game_data[_index][2],
#         game_stats.game_data[_index][3], '#0047b8')
#     game_stats.game_data[_index] = clear_question
#
#     round_complete = True
#     for stat in game_stats.game_data:
#         if stat[4] == 'white':
#             round_complete = False
#
#     if round_complete is True:
#         game_stats.round += 1
#         game_stats.game_data = game_stats.round_two
#         game_stats.log_game(f'Round {game_stats.round}')
#
#     if game_stats.round == 3:
#         return redirect(url_for('final'))
#     else:
#         return redirect(url_for('game'))


@app.route('/update_game', methods=['POST'])
def update_game():
    # _index = int(request.args.get('index')) - 1
    if request.form.get('team_one') is not None and request.form.get('team_one') != '':
        ug.update_team_scores('Team1', int(request.form.get('team_one', 0)))
    if request.form.get('team_two') is not None and request.form.get('team_two') != '':
        ug.update_team_scores('Team2', int(request.form.get('team_two', 0)))
    if request.form.get('team_three') is not None and request.form.get('team_three') != '':
        ug.update_team_scores('Team3', int(request.form.get('team_three', 0)))

    # TODO figure out if I want to log the game
    game_stats.log_game(
        f"  Points:   One: {request.form.get('team_one')}, "
        f"  Two: {request.form.get('team_two')}, "
        f"  Three: {request.form.get('team_three')}")
    game_stats.log_game(f"  Scores:   One: {game_stats.team_one_points}, "
                        f"  Two: {game_stats.team_two_points}, "
                        f"  Three: {game_stats.team_three_points}")
    # clear_question = (
    #     game_stats.game_data[_index][0], game_stats.game_data[_index][1], game_stats.game_data[_index][2],
    #     game_stats.game_data[_index][3], '#0047b8')
    # game_stats.game_data[_index] = clear_question
    #
    ug.update_display_question(int(request.args.get('column_position')), int(request.args.get('row_position')),
                               False)
    #
    # round_complete = True
    # for stat in game_stats.game_data:
    #     if stat[4] == 'white':
    #         round_complete = False
    #
    # if round_complete is True:
    #     game_stats.round += 1
    #     game_stats.game_data = game_stats.round_two
    #     game_stats.log_game(f'Round {game_stats.round}')
    #
    # if game_stats.round == 3:
    #     return redirect(url_for('final'))
    # else:
    #     return redirect(url_for('game'))
    if ug.check_for_round_end() == True:
        ug.change_current_round(ug.read_current_round() + 1)

    return redirect(url_for('game'))


@app.route('/answer', methods=['POST'])
def answer():
    points = request.args.get('points')
    _answer = request.args.get('answer')
    question = request.args.get('question')
    column_position = request.args.get('column_position')
    row_position = request.args.get('row_position')
    display = request.args.get('display')
    daily_double = request.args.get('daily_double')
    game_stats.log_game("")
    game_stats.log_game(f"{points}, {_answer}, {question}, {column_position}, {display}")
    return render_template('answer.html', points=points, answer=_answer, question=question,
                           column_position=column_position,
                           display=display, row_position=row_position, daily_double=daily_double)


@app.route('/final')
def final():
    _final = game_stats.final_jeopardy
    one = game_stats.team_one_points
    two = game_stats.team_two_points
    three = game_stats.team_three_points
    return render_template('final.html', final=_final, one=one, two=two, three=three)


@app.route('/game_result', methods=['POST'])
def game_result():
    _final = game_stats.final_jeopardy
    one = game_stats.team_one_points
    two = game_stats.team_two_points
    three = game_stats.team_three_points

    # one_answer = 'abc'
    # one_wager = 100
    # two_answer = 'def'
    # two_wager = 200
    # three_answer = 'ghi'
    # three_wager = 300
    one_answer = game_stats.team_one_answer
    one_wager = game_stats.team_one_wager
    two_answer = game_stats.team_two_answer
    two_wager = game_stats.team_two_wager
    three_answer = game_stats.team_three_answer
    three_wager = game_stats.team_three_wager
    return render_template('game_result.html', final=_final, one=one, two=two, three=three, one_answer=one_answer,
                           one_wager=one_wager, two_answer=two_answer, two_wager=two_wager, three_answer=three_answer,
                           three_wager=three_wager)


@app.route('/record_final_answers', methods=['POST'])
def record_final_answers():
    game_stats.team_one_wager = request.form.get('team_one_wager')
    game_stats.team_two_wager = request.form.get('team_two_wager')
    game_stats.team_three_wager = request.form.get('team_three_wager')

    game_stats.team_one_answer = request.form.get('team_one_answer')
    game_stats.team_two_answer = request.form.get('team_two_answer')
    game_stats.team_three_answer = request.form.get('team_three_answer')

    print(request.form.get('team_one_wager'), request.form.get('team_two_wager'))
    game_stats.log_game(
        f"Final wager/answers: {request.form.get('team_one_wager')} {request.form.get('team_one_answer')}, "
        f"{request.form.get('team_two_wager')} {request.form.get('team_two_answer')}, "
        f"{request.form.get('team_three_wager')} {request.form.get('team_three_answer')}")

    return redirect(url_for('log'))


@app.route('/record_final')
def record_final():
    return render_template('record_final.html')


@app.route('/log')
def log():
    return render_template('log.html', log=game_stats.log)


@app.route('/update_scores_post', methods=['POST'])
def update_scores_post():
    with open('game_json.json', 'r') as _f:
        _game_json = json.loads(_f.read())
    game_stats.team_one_points = int(request.form.get('team_one_amount'))
    _game_json['scores']['Team1'] = int(request.form.get('team_one_amount'))
    game_stats.team_two_points = int(request.form.get('team_two_amount'))
    _game_json['scores']['Team2'] = int(request.form.get('team_two_amount'))
    game_stats.team_three_points = int(request.form.get('team_three_amount'))
    _game_json['scores']['Team3'] = int(request.form.get('team_three_amount'))
    with open('game_json.json', 'w') as _f:
        _f.write(json.dumps(_game_json, indent=2))
    game_stats.log_game(f"Updated team scores: "
                        f"team one:   {game_stats.team_one_points}"
                        f"team two:   {game_stats.team_two_points}"
                        f"team three: {game_stats.team_three_points}")
    return redirect(url_for('log'))


@app.route('/update_scores')
def update_scores():
    one = ug.read_team_score('Team1')
    two = ug.read_team_score('Team2')
    three = ug.read_team_score('Team3')

    return render_template('update_scores.html', one=one, two=two, three=three)
