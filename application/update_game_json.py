# TODO update team scores
# TODO set a question to display or not
# TODO advance to round 2

import json


def update_team_scores(team_1_total=None, team_2_total=None, team_3_total=None, team_1_add=None, team_2_add=None,
                       team_3_add=None):
    """
    Update the team scores in the local file called 'game_json.json'
    Must use either all 3 team_#_total or team_#_add parameters
    """
    # check which set of params to use
    if team_1_total and team_2_total and team_3_total is not None:
        score_set = 'total'
    elif team_1_add and team_2_add and team_3_add is not None:
        score_set = 'add'
    else:
        raise ValueError('Please use one set of parameters')

    with open('game_json.json', 'r') as f:
        game_json = f.read()
        game_json = json.loads(game_json)

    if score_set is 'total':
        game_json['scores']['Team1'] = team_1_total
        game_json['scores']['Team2'] = team_2_total
        game_json['scores']['Team3'] = team_3_total
    elif score_set is 'add':
        game_json['scores']['Team1'] += team_1_add
        game_json['scores']['Team2'] += team_2_add
        game_json['scores']['Team3'] += team_3_add
    else:
        raise ValueError('The variable \'score_set\' is not equal to \'total\' or \'add\'')

    with open('game_json.json', 'w') as f:
        f.write(json.dumps(game_json, indent=2))


def update_display_question(question_tuple):
    """
    Finds a question and updates the json file called 'game_json.json' to mark that question read
    :param question_tuple: A tuple that needs to be in the format (column number, question number)
    :return:
    """
    with open('game_json.json', 'r') as f:
        game_json = f.read()
        game_json = json.loads(game_json)
    # TODO finish function


if __name__ == '__main__':
    update_team_scores(team_1_add=3, team_2_add=23, team_3_add=-324)
