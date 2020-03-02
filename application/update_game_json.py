import json


def update_team_scores(team_name, amount_to_add, game_json_file):
    """
    Updates a team's score in
    """
    with open(f'games/{game_json_file}', 'r') as f:
        game_json = f.read()
        game_json = json.loads(game_json)
    game_json['scores'][team_name] += amount_to_add
    with open(f'games/{game_json_file}', 'w') as f:
        f.write(json.dumps(game_json, indent=2))


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

    with open(f'games/{game_json_file}', 'w') as f:
        f.write(json.dumps(game_json, indent=2))


def change_current_round(_round, game_json_file):
    with open(f'games/{game_json_file}', 'r')as _f:
        game_json = json.loads(_f.read())
    game_json['current_round'] = int(_round)
    with open(f'games/{game_json_file}', 'w') as _f:
        _f.write(json.dumps(game_json, indent=2))


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


def check_for_round_end(game_json_file):
    game_json = return_full_json(game_json_file)
    round_end = True
    for x in game_json['board'][f'round{game_json["current_round"]}']['columns']:
        for y in x['questions']:
            if y['display'] == True:
                round_end = False
    return round_end


def manage_game_file(file_name, create):
    # with open('game_json.json', 'w') as f:
    #     with open(f'games/{file_name}.json', 'r') as _f:
    #         f.write(_f.read())
    # with open('game_json.json', 'r') as f2:
    #     cur_json = json.loads(f2.read())
    # cur_json['current_file'] = str(file_name) + '.json'
    # with open('game_json.json', 'w') as f3:
    #     f3.write(json.dumps(cur_json, indent=2))
    curr_file = ''
    if create == True:
        pass
    return curr_file


if __name__ == '__main__':
    # update_team_scores(str(input('team: ')), int(input('amount: ')))
    # update_display_question(int(input('round: ')), int(input('column: ')), int(input('question: ')), False)
    # update_display_question(1, 1, False)
    # change_current_round(2)
    pass
