from application import app
from flask import render_template, request, redirect, url_for

from application import generate_game as gg

game_stats = gg.GenerateGame()


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template('index.html')


@app.route('/generate_game', methods=['POST'])
def generate_game():
    game_stats.log_game('Creating game')
    game_stats.generate_game(request.form.get('dropdown-option', ''))
    game_stats.log_game(f'Round {game_stats.round}')
    return render_template('game.html', gameData=game_stats.game_data,
                           team_one_points=game_stats.team_one_points,
                           team_two_points=game_stats.team_two_points, team_three_points=game_stats.team_three_points)


@app.route('/game')
def game():
    return render_template('game.html', gameData=game_stats.game_data,
                           team_one_points=game_stats.team_one_points,
                           team_two_points=game_stats.team_two_points, team_three_points=game_stats.team_three_points)


@app.route('/update_game', methods=['POST'])
def update_game():
    _index = int(request.args.get('index')) - 1
    if request.form.get('team_one') is not None and request.form.get('team_one') != '':
        game_stats.team_one_points += int(request.form.get('team_one', 0))

    if request.form.get('team_two') is not None and request.form.get('team_two') != '':
        game_stats.team_two_points += int(request.form.get('team_two', 0))
    if request.form.get('team_three') is not None and request.form.get('team_three') != '':
        game_stats.team_three_points += int(request.form.get('team_three', 0))

    game_stats.log_game(
        f"  Points:   One: {request.form.get('team_one')}, "
        f"  Two: {request.form.get('team_two')}, "
        f"  Three: {request.form.get('team_three')}")
    game_stats.log_game(f"  Scores:   One: {game_stats.team_one_points}, "
                        f"  Two: {game_stats.team_two_points}, "
                        f"  Three: {game_stats.team_three_points}")
    clear_question = (
        game_stats.game_data[_index][0], game_stats.game_data[_index][1], game_stats.game_data[_index][2],
        game_stats.game_data[_index][3], '#0047b8')
    game_stats.game_data[_index] = clear_question

    round_complete = True
    for stat in game_stats.game_data:
        if stat[4] == 'white':
            round_complete = False

    if round_complete is True:
        game_stats.round += 1
        game_stats.game_data = game_stats.round_two
        game_stats.log_game(f'Round {game_stats.round}')

    if game_stats.round == 3:
        return redirect(url_for('final'))
    else:
        return redirect(url_for('game'))


@app.route('/answer', methods=['POST'])
def answer():
    points = request.args.get('points')
    _answer = request.args.get('answer')
    question = request.args.get('question')
    _index = request.args.get('index')
    color = request.args.get('color')
    game_stats.log_game("")
    game_stats.log_game(f"{points}, {_answer}, {question}, {_index}, {color}")
    return render_template('answer.html', points=points, answer=_answer, question=question, index=_index, color=color)


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
