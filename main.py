import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from flask import Flask

from application import common

external_stylesheets = ''
server = Flask(__name__)

app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)

cmn = common.Common()

# # Main
# app.layout = html.Div([
#     # Header
#     html.Div([
#         html.H1('Scout Jeopardy')
#     ], id='Header'),
#
#     # Game board
#     html.Div([
#         # a single box
#         html.Div([html.H3('banana', id='something_h'),
#                   html.H2('hi')], id='something')
#     ], id='Game board'),
#
#     # footer
#     html.Div([
#         # team 1
#         html.Div([
#             html.H3('team 1'),
#             html.H3('$300', id='team_1_amount', className='team_amount')
#         ], id='team_1', className='team_box'),
#
#         # team 2
#         html.Div([
#             html.H3('team 2'),
#             html.H3('$500', id='team_2_amount', className='team_amount')
#         ], id='team_2', className='team_box'),
#
#         # team 3
#         html.Div([
#             html.H3('team 3'),
#             html.H3('$700', id='team_3_amount', className='team_amount')
#         ], id='team_3', className='team_box')
#
#     ], id='footer')
# ])


game_list = [(100, 'answer1', 'question1', False),
             (200, 'answer2', 'question2', True),
             (300, 'answer3', 'question3', False),
             (400, 'answer4', 'question4', False)]

app.layout = html.Div([
    dcc.Tabs(id='tabs', value='tab-1', children=[
        # dcc.Tab(label='Tab one', children=[
        #     html.Button('Submit1', id='button1'),
        #     html.P(),
        #     html.Button('Submit2', id='button2')
        # ]),
        #
        # dcc.Tab(label='Tab two', children=[
        #     html.Button('Submit3', id='button3'),
        #     html.P(),
        #     html.Button('Submit4', id='button4')
        # ]),

        dcc.Tab(label='Game Board', children=[
            html.Button('Submit5', id='button5'),
            html.P(),
            html.Button('Submit6', id='button6'),
            html.P(),
            html.Button('Submit7', id='button7'),
            html.P(),
            html.Button('Submit8', id='button8')
        ]),
        dcc.Tab(label='Answer', children=[
            html.H1('TEST', id='answer'),
            html.Button('Submit', id='submit')
        ])
        # ----------------------------------------------

    ]),
    html.Div(id='tabs-content')
])


# @app.callback(Output('Tab three', 'children'),
#               [Input('test_Submit0')])
# def create_buttons():
#     completed_buttons = ''
#     for x in range(4):
#         print(temp_button_boxes_test[x])
#         completed_buttons += f"html.Button('test_Submit{str(x)}', id='test_button{str(x)}'), "
#     print(completed_buttons)
#     return completed_buttons


# @app.callback(
#     dash.dependencies.Output('button1', 'children'),
#     [dash.dependencies.Input('button1', 'n_clicks')])
# def update_output(n_clicks):
#     return 'The button1 has been clicked {} times'.format(n_clicks)
#
#
# @app.callback(
#     dash.dependencies.Output('button2', 'children'),
#     [dash.dependencies.Input('button2', 'n_clicks')])
# def update_output(n_clicks):
#     return 'The special button2 has been clicked {} times'.format(n_clicks)


# @app.callback(
#     dash.dependencies.Output('button3', 'children'),
#     [dash.dependencies.Input('button3', 'n_clicks'),
#      dash.dependencies.Input('button4', 'n_clicks')])
# def update_output(button3, button4):
#     if button3 is not None and button3 > 0:
#         print('button 3 is more than 0')
#         button3 = 0
#     elif button4 is not None and button4 > 0:
#         print('button 4 is more than 0')
#     else:
#         print('all buttons none or 0')
#     print(f'Button 3: {button3}, Button 4: {button4}')
#     return 'The button3 has been clicked {} times'.format(button3)


@app.callback(
    [dash.dependencies.Output('answer', 'children')],
    [dash.dependencies.Input('button5', 'n_clicks'),
     dash.dependencies.Input('button6', 'n_clicks'),
     dash.dependencies.Input('button7', 'n_clicks'),
     dash.dependencies.Input('button8', 'n_clicks')])
def update_output(button5, button6, button7, button8):
    answer = cmn.get_answer(game_list, button5, button6, button7, button8)
    button5, button6, button7, button8 = cmn.reset_buttons()
    return answer


#
# @app.callback(
#     dash.dependencies.Output('button4', 'children'),
#     [dash.dependencies.Input('button4', 'n_clicks')])
# def update_output(n_clicks):
#     return 'The button4 has been clicked {} times'.format(n_clicks)


if __name__ == '__main__':
    app.run_server(debug=True)
