import json


def update_team_scores(team_name, amount_to_add):
    """
    Updates a team's score in
    """
    with open('game_json.json', 'r') as f:
        game_json = f.read()
        game_json = json.loads(game_json)
    game_json['scores'][team_name] += amount_to_add
    with open('game_json.json', 'w') as f:
        f.write(json.dumps(game_json, indent=2))


def update_display_question(q_column, q_num, q_display_t_or_f):
    """
    Finds a question and updates the json file called 'game_json.json' to mark that question read
    :param q_column: An int between 1-6 relating to the game column
    :param q_num: An int between 1-5 relating to the game question
    :param q_display_t_or_f: A boolean representing whether to display a question
    :return:
    """
    q_column -= 1
    q_num -= 1
    with open('game_json.json', 'r') as f:
        game_json = json.loads(f.read())

    _round = f'round{game_json["current_round"]}'

    game_json['board'][_round]['columns'][q_column]['questions'][q_num]['display'] = q_display_t_or_f

    with open('game_json.json', 'w') as f:
        f.write(json.dumps(game_json, indent=2))


def change_current_round(_round):
    with open('game_json.json', 'r')as _f:
        game_json = json.loads(_f.read())
    game_json['current_round'] = int(_round)
    with open('game_json.json', 'w') as _f:
        _f.write(json.dumps(game_json, indent=2))


if __name__ == '__main__':
    # update_team_scores(str(input('team: ')), int(input('amount: ')))
    # update_display_question(int(input('round: ')), int(input('column: ')), int(input('question: ')), False)
    # update_display_question(1, 1, False)
    change_current_round(2)
