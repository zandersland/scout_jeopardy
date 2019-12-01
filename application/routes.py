from application import app
from flask import render_template, request

from application import generate_game as gg

game_stats = gg.GenerateGame()


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template('index.html')


@app.route('/generate_game', methods=['POST'])
def generate_game():
    game_stats.generate_game(request.form.get('dropdown-option', ''))
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
    if request.form.get('teamOne') is not None and request.form.get('teamOne') != '':
        game_stats.team_one_points += int(request.form.get('teamOne', 0))
    if request.form.get('teamTwo') is not None and request.form.get('teamTwo') != '':
        game_stats.team_two_points += int(request.form.get('teamTwo', 0))
    if request.form.get('teamThree') is not None and request.form.get('teamThree') != '':
        game_stats.team_three_points += int(request.form.get('teamThree', 0))

    clear_question = (
        game_stats.game_data[_index][0], game_stats.game_data[_index][1], game_stats.game_data[_index][2],
        game_stats.game_data[_index][3], 'blue')
    print(clear_question)
    game_stats.game_data[_index] = clear_question
    print(game_stats.game_data[_index])
    return render_template('game.html', gameData=game_stats.game_data, team_one_points=game_stats.team_one_points,
                           team_two_points=game_stats.team_two_points,
                           team_three_points=game_stats.team_three_points)


@app.route('/answer', methods=['POST'])
def answer():
    print(game_stats.game_data[1][4])
    points = request.args.get('points')
    _answer = request.args.get('answer')
    question = request.args.get('question')
    _index = request.args.get('index')
    color = request.args.get('color')
    return render_template('answer.html', points=points, answer=_answer, question=question, index=_index, color=color)


@app.route('/final')
def final():
    return render_template('final.html')
