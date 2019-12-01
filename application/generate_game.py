class GenerateGame:
    def __init__(self):
        self.team_one_points = 0
        self.team_two_points = 0
        self.team_three_points = 0
        self.game_data = []

    def generate_game(self, _game):
        print('game', _game)
        if _game == '1':
            self.game_data = [('Category1', '', '', False, 'white'),
                              ('Category2', '', '', False, 'white'),
                              ('Category3', '', '', False, 'white'),
                              ('Category4', '', '', False, 'white'),
                              ('Category5', '', '', False, 'white'),
                              ('Category6', '', '', False, 'white'),
                              (100, 'answer1', 'question1', False, 'white'),
                              (100, 'answer21', 'question1', False, 'white'),
                              (100, 'answer31', 'question1', False, 'white'),
                              (100, 'answer41', 'question1', False, 'white'),
                              (100, 'answer51', 'question1', False, 'white'),
                              (100, 'answer61', 'question1', False, 'white'),

                              (200, 'answer2', 'question2', False, 'white'),
                              (200, 'answer22', 'question2', False, 'white'),
                              (200, 'answer32', 'question2', False, 'white'),
                              (200, 'answer42', 'question2', False, 'white'),
                              (200, 'answer52', 'question2', False, 'white'),
                              (200, 'answer62', 'question2', False, 'white'),

                              (300, 'answer3', 'question3', False, 'white'),
                              (300, 'answer23', 'question3', False, 'white'),
                              (300, 'answer33', 'question3', False, 'white'),
                              (300, 'answer43', 'question3', False, 'white'),
                              (300, 'answer53', 'question3', False, 'white'),
                              (300, 'answer63', 'question3', False, 'white'),

                              (400, 'answer4', 'question4', False, 'white'),
                              (400, 'answer24', 'question4', False, 'white'),
                              (400, 'answer34', 'question4', False, 'white'),
                              (400, 'answer44', 'question4', False, 'white'),
                              (400, 'answer54', 'question4', False, 'white'),
                              (400, 'answer64', 'question4', False, 'white'),

                              (500, 'answer5', 'question5', False, 'white'),
                              (500, 'answer25', 'question5', False, 'white'),
                              (500, 'answer35', 'question5', False, 'white'),
                              (500, 'answer45', 'question5', False, 'white'),
                              (500, 'answer55', 'question5', False, 'white'),
                              (500, 'answer65', 'question5', False, 'white')
                              ]
        else:
            self.game_data = [('Category7', '', '', False, 'white'),
                              ('Category8', '', '', False, 'white'),
                              ('Category9', '', '', False, 'white'),
                              ('Category10', '', '', False, 'white'),
                              ('Category11', '', '', False, 'white'),
                              ('Category12', '', '', False, 'white'),
                              (200, 'answer1', 'question1', False, 'white'),
                              (200, 'answer21', 'question1', False, 'white'),
                              (200, 'answer31', 'question1', False, 'white'),
                              (200, 'answer41', 'question1', False, 'white'),
                              (200, 'answer51', 'question1', False, 'white'),
                              (200, 'answer61', 'question1', False, 'white'),

                              (400, 'answer2', 'question2', False, 'white'),
                              (400, 'answer22', 'question2', False, 'white'),
                              (400, 'answer32', 'question2', False, 'white'),
                              (400, 'answer42', 'question2', False, 'white'),
                              (400, 'answer52', 'question2', False, 'white'),
                              (400, 'answer62', 'question2', False, 'white'),

                              (600, 'answer3', 'question3', False, 'white'),
                              (600, 'answer23', 'question3', False, 'white'),
                              (600, 'answer33', 'question3', False, 'white'),
                              (600, 'answer43', 'question3', False, 'white'),
                              (600, 'answer53', 'question3', False, 'white'),
                              (600, 'answer63', 'question3', False, 'white'),

                              (800, 'answer4', 'question4', False, 'white'),
                              (800, 'answer24', 'question4', False, 'white'),
                              (800, 'answer34', 'question4', False, 'white'),
                              (800, 'answer44', 'question4', False, 'white'),
                              (800, 'answer54', 'question4', False, 'white'),
                              (800, 'answer64', 'question4', False, 'white'),

                              (1000, 'answer5', 'question5', False, 'white'),
                              (1000, 'answer25', 'question5', False, 'white'),
                              (1000, 'answer35', 'question5', False, 'white'),
                              (1000, 'answer45', 'question5', False, 'white'),
                              (1000, 'answer55', 'question5', False, 'white'),
                              (1000, 'answer65', 'question5', False, 'white')
                              ]
