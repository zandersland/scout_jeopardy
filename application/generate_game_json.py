import csv
import json
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


def create_questions(question_count, category, questions_json):
    questions = []
    for x in range(question_count):
        question = {
            'question': questions_json[category][x]['question'],
            'answer': questions_json[category][x]['answer'],
            'position': x + 1,
            'daily_double': False,
            'display': True
        }
        questions.append(question)
    return questions


def create_columns(column_count, categories, questions_json):
    columns = []
    for x in range(column_count):
        col = {
            'title': categories[x],
            'position': x + 1,
            'questions': create_questions(5, categories[x], questions_json)
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
    game = {'scores': create_scores(), 'board': create_board()}

    game['board']['round1'] = create_columns(6, round_1_category, question_json)

    game['board']['round2'] = create_columns(6, round_2_category, question_json)

    game = json.dumps(game, indent=2)
    return game


def convert_csv_to_json():
    with open("questions.csv", 'r') as f:
        reader = csv.reader(f)
        csv_list = list(reader)
        verify_list(csv_list)
        keys = []
        result_json = {}
        for pos, val in enumerate(csv_list):
            if val[0] not in result_json.keys():
                result_json[val[0]] = [{'question': val[1], 'answer': val[2]}]
            else:
                list_item = result_json.get(val[0])
                list_item.append({'question': val[1], 'answer': val[2]})
                result_json[val[0]] = list_item

        # print(json.dumps(result_json, indent=2))
    # return reader
    category_ids = random.sample(result_json.keys(), 12)
    list1 = category_ids[0:6]
    list2 = category_ids[6:12]
    return list1, list2, result_json


if __name__ == '__main__':
    # json_test()
    # print(generate_game_3())
    json_tuple = convert_csv_to_json()
    with open('json_text_file.json', 'w') as f:
        f.write(generate_game_3(json_tuple[0], json_tuple[1], json_tuple[2]))
