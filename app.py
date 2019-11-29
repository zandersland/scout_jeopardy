import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

external_stylesheets = ''
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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


temp_button_boxes_test = [(100, 'banana', 'what is yellow', False),
                          (200, 'bv rgtsb', 'rstnbhf tb', True),
                          (300, 'rtdeghnbfgbhn', 'drtgntgn', False),
                          (400, 'drtgn rt', 'drtnjxf', False)]


create_buttons()


app.layout = html.Div([
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Tab one', children=[
            html.Button('Submit1', id='button1'),
            html.P(),
            html.Button('Submit2', id='button2')
        ]),


        dcc.Tab(label='Tab two', children=[
            html.Button('Submit3', id='button3'),
            html.P(),
            html.Button('Submit4', id='button4')
        ]),


        dcc.Tab(label='Tab three', children=[
            html.Button('Submit5', id='button5'),
            html.P(),
            html.Button('Submit6', id='button6')
        ]),

        # ----------------------------------------------

    ]),
    html.Div(id='tabs-content')
])

class stuff:
    click_test = 0

    def click_num():
        stuff.click_test += 1
        return str(stuff.click_test)


@app.callback(Output('Tab three', 'children'),
              [Input('test_Submit0')])
def create_buttons():
    completed_buttons = ''
    for x in range(4):
        print(temp_button_boxes_test[x])
        completed_buttons += f"html.Button('test_Submit{str(x)}', id='test_button{str(x)}'), "
    print(completed_buttons)
    return completed_buttons

@app.callback(
    dash.dependencies.Output('button1', 'children'),
    [dash.dependencies.Input('button1', 'n_clicks')])
def update_output(n_clicks):
    return 'The button1 has been clicked {} times'.format(n_clicks)


@app.callback(
    dash.dependencies.Output('button2', 'children'),
    [dash.dependencies.Input('button2', 'n_clicks')])
def update_output(n_clicks):
    return 'The special button2 has been clicked {} times'.format(stuff.click_num())


@app.callback(
    dash.dependencies.Output('button3', 'children'),
    [dash.dependencies.Input('button3', 'n_clicks'),
     dash.dependencies.Input('button4', 'n_clicks')])
def update_output(button3, button4):
    if button3 is not None and button3 > 0:
        print('button 3 is more than 0')
        button3 = 0
    elif button4 is not None and button4 > 0:
        print('button 4 is more than 0')
    else:
        print('all buttons none or 0')
    print(f'Button 3: {button3}, Button 4: {button4}')
    return 'The button3 has been clicked {} times'.format(button3)


@app.callback(
    dash.dependencies.Output('button5', 'children'),
    [dash.dependencies.Input('button5', 'n_clicks')])
def update_output(n_clicks):
    return 'The button5 has been clicked {} times'.format(n_clicks)


@app.callback(
    dash.dependencies.Output('button6', 'children'),
    [dash.dependencies.Input('button6', 'n_clicks')])
def update_output(n_clicks):
    return 'The button6 has been clicked {} times'.format(n_clicks)


#
# @app.callback(
#     dash.dependencies.Output('button4', 'children'),
#     [dash.dependencies.Input('button4', 'n_clicks')])
# def update_output(n_clicks):
#     return 'The button4 has been clicked {} times'.format(n_clicks)


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')

























