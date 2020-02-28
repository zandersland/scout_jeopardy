import csv
import json
import os
import random


def verify_list(_list):
    for x in _list:
        if len(x) != 3:
            print('\n\n+++++ERROR+++++\n\nThis line in the list is not equal to 3 items\n', len(x), x)
            exit(1)


def create_scores():
    scores = {
        'Team1': 0,
        'Team2': 0,
        'Team3': 0
    }
    return scores


def create_questions(question_count, category, questions_json, round_num):
    questions = []
    for x in range(question_count):
        try:
            daily_double = questions_json[category][x]['daily_double']
        except KeyError:
            daily_double = False
        question = {
            'question': questions_json[category][x]['question'],
            'answer': questions_json[category][x]['answer'],
            'position': x + 1,
            'daily_double': daily_double,
            'display': True,
            'score_amount': (x + 1) * (round_num * 100)
        }
        questions.append(question)
    return questions


def create_columns(column_count: int, categories: list, questions_json: dict, round_num: int) -> dict:
    """

    :rtype: dict
    """
    columns = []
    for x in range(column_count):
        col = {
            'title': categories[x],
            'position': x + 1,
            'questions': create_questions(5, categories[x], questions_json, round_num)
        }
        columns.append(col)

    return {'columns': columns}


def create_board():
    board = {
        'round1': {},
        'round2': {}
    }
    return board


def generate_game_3(round_1_category, round_2_category, question_json):
    game = {'current_round': 1, 'scores': create_scores(), 'board': create_board()}

    game['board']['round1'] = create_columns(6, round_1_category, question_json, 1)

    game['board']['round2'] = create_columns(6, round_2_category, question_json, 2)

    game = json.dumps(game, indent=2)
    return game


def add_daily_double(list1, list2, question_json):
    # abbreviations mean double jeopardy category
    round_1_dj_cat = random.sample(list1, 1)
    round_2_dj_cat1 = random.sample(list2, 1)
    round_2_dj_cat2 = random.sample(list2, 1)
    rand_1 = random.randint(0, 4)
    rand_2 = random.randint(0, 4)
    if round_2_dj_cat1 == round_2_dj_cat1 and rand_1 == rand_2:
        print('fyi, the initial two random daily doubles was the same for round two. fixing the problem now...')
        if rand_2 != 4:
            rand_2 += 1
        else:
            rand_2 -= 1
    question_json[round_1_dj_cat[0]][random.randint(0, 4)]['daily_double'] = True
    question_json[round_2_dj_cat1[0]][rand_1]['daily_double'] = True
    question_json[round_2_dj_cat2[0]][rand_2]['daily_double'] = True
    return question_json


def convert_csv_to_json():
    with open("questions.csv", 'r') as _f:
        reader = csv.reader(_f)
        csv_list = list(reader)
        verify_list(csv_list)
        question_json = {}
        for pos, val in enumerate(csv_list):
            if val[0] not in question_json.keys():
                question_json[val[0]] = [{'question': val[1], 'answer': val[2]}]
            else:
                list_item = question_json.get(val[0])
                list_item.append({'question': val[1], 'answer': val[2]})
                question_json[val[0]] = list_item

    category_ids = random.sample(question_json.keys(), 12)
    list1 = category_ids[0:6]
    list2 = category_ids[6:12]
    question_json = add_daily_double(list1, list2, question_json)
    return list1, list2, question_json


def generate_game_4(file_name):
    json_tuple = convert_csv_to_json()
    if os.path.exists(file_name):
        assert True == False
        # TODO fix file being overwritten
    with open(f'games/{file_name}.json', 'w') as f:
        f.write(generate_game_3(json_tuple[0], json_tuple[1], json_tuple[2]))
    print(os.listdir('games'))


if __name__ == '__main__':
    json_tuple = convert_csv_to_json()
    with open('game_json.json', 'w') as f:
        f.write(generate_game_3(json_tuple[0], json_tuple[1], json_tuple[2]))
