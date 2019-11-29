class Common:

    @staticmethod
    def get_answer(game_list, button5, button6, button7, button8, *args, **kwargs):
        print('buttons 5-8', button5, button6, button7, button8)
        if button5 is not None and button5 > 0:
            return [game_list[0][2]]
        if button6 is not None and button6 > 0:
            return [game_list[1][2]]
        if button7 is not None and button7 > 0:
            return [game_list[2][2]]
        if button8 is not None and button8 > 0:
            return [game_list[3][2]]
        return ['']

    @staticmethod
    def reset_buttons():
        return 0, 0, 0, 0
