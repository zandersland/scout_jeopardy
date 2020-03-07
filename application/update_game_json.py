import json
from datetime import datetime


def update_team_scores(team_name, amount_to_add, game_json_file):
    """
    Updates a team's score in
    """
    with open(f'games/{game_json_file}', 'r') as f:
        game_json = f.read()
        game_json = json.loads(game_json)
    game_json['scores'][team_name] += amount_to_add
    write_to_json_file(game_json_file, game_json)


def set_team_score(game_json_file, team_name, amount_to_set_to):
    game_json = return_full_json(game_json_file)
    game_json['scores'][team_name] = amount_to_set_to
    write_to_json_file(game_json_file, game_json)


def update_display_question(q_column, q_num, q_display_t_or_f, game_json_file):
    """
    Finds a question and updates the json file called 'game_json.json' to mark that question read
    :param q_column: An int between 1-6 relating to the game column
    :param q_num: An int between 1-5 relating to the game question
    :param q_display_t_or_f: A boolean representing whether to display a question
    :return:
    """
    q_column -= 1
    q_num -= 1
    with open(f'games/{game_json_file}', 'r') as f:
        game_json = json.loads(f.read())

    _round = f'round{game_json["current_round"]}'

    game_json['board'][_round]['columns'][q_column]['questions'][q_num]['display'] = q_display_t_or_f

    write_to_json_file(game_json_file, game_json)


def change_current_round(_round, game_json_file):
    with open(f'games/{game_json_file}', 'r')as _f:
        game_json = json.loads(_f.read())
    game_json['current_round'] = int(_round)
    write_to_json_file(game_json_file, game_json)


def read_team_score(_team_name, game_json_file):
    with open(f'games/{game_json_file}', 'r') as _f:
        _team_score = json.loads(_f.read())['scores'][_team_name]
    return _team_score


def read_current_round(game_json_file):
    with open(f'games/{game_json_file}', 'r') as _f:
        return json.loads(_f.read())['current_round']


def return_full_json(game_json_file):
    with open(f'games/{game_json_file}', 'r') as _f:
        return json.loads(_f.read())


def write_to_json_file(game_json_file, game_json):
    with open(f'games/{game_json_file}', 'w') as f1:
        f1.write(json.dumps(game_json, indent=2))


def check_for_round_end(game_json_file):
    game_json = return_full_json(game_json_file)
    round_end = True
    for x in game_json['board'][f'round{game_json["current_round"]}']['columns']:
        for y in x['questions']:
            if y['display'] == True:
                round_end = False
    return round_end


def read_team_guesses(game_json_file):
    game_json = return_full_json(game_json_file)
    try:
        return game_json['buzzer_positions']
    except:
        game_json['buzzer_positions'] = (True, True, True)
        write_to_json_file(game_json_file, game_json)
        return game_json['buzzer_positions']


def update_team_guesses(game_json_file, wrong_team_answer):
    game_json = return_full_json(game_json_file)
    try:
        print(game_json['buzzer_positions'])
    except KeyError:
        game_json['buzzer_positions'] = (True, True, True)

    game_json['buzzer_positions'][int(wrong_team_answer)] = False

    write_to_json_file(game_json_file, game_json)
    return game_json['buzzer_positions']


def reset_team_guesses(game_json_file):
    game_json = return_full_json(game_json_file)

    game_json['buzzer_positions'] = (True, True, True)

    write_to_json_file(game_json_file, game_json)


def update_first_player(game_json_file, first_player):
    game_json = return_full_json(game_json_file)
    game_json['first_player'] = first_player
    write_to_json_file(game_json_file, game_json)


def add_line_to_log(game_json_file, log_line):
    game_json = return_full_json(game_json_file)
    try:
        game_json['log'].append(f'{datetime.utcnow()} - ' + log_line)
    except:
        game_json['log'] = [f'{datetime.utcnow()} - ' + log_line]
    write_to_json_file(game_json_file, game_json)


def read_log(game_json_file):
    game_json = return_full_json(game_json_file)
    try:
        return game_json['log']
    except:
        game_json['log'] = []
        write_to_json_file(game_json_file, game_json)
        return game_json['log']


def get_final_jeopardy(game_json_file):
    game_json = return_full_json(game_json_file)
    try:
        return_statement = game_json['final_jeopardy']
    except:
        import generate_game_json as ggj
        print(ggj.create_final_jeopardy)
        game_json['final_jeopardy'] = ggj.create_final_jeopardy()
        return_statement = game_json['final_jeopardy']
        write_to_json_file(game_json_file, game_json)
    return return_statement


def get_entry_in_final_jeopardy(game_json_file, line):
    game_json = return_full_json(game_json_file)
    try:
        return game_json['final_jeopardy'][line]
    except:
        import generate_game_json as ggj
        game_json['final_jeopardy'] = ggj.create_final_jeopardy()
        write_to_json_file(game_json_file, game_json)
        return game_json['final_jeopardy'][line]


def update_final_jeopardy(game_json_file, field_to_update, value):
    game_json = return_full_json(game_json_file)
    game_json['final_jeopardy'][field_to_update] = value
    write_to_json_file(game_json_file, game_json)


if __name__ == '__main__':
    # update_team_scores(str(input('team: ')), int(input('amount: ')))
    # update_display_question(int(input('round: ')), int(input('column: ')), int(input('question: ')), False)
    # update_display_question(1, 1, False)
    # change_current_round(2)
    pass
