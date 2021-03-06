import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from services import train

from app import app

layout = html.Div([
    html.H3('Admin Window'),
    dcc.Dropdown(
        id='admin_window-dropdown_aw',
        options=[
            {'label': 'Logs - {}'.format(i[:-4]), 'value': i} for i in os.listdir('data/logs/')
        ]
    ),
    html.Div(id='admin_window-display-value_aw'),

    html.Button('Train model', id='train_mdl_aw', n_clicks=0),

    html.Div(id='admin_window-hit_rate_aw'),
])


@app.callback(
    Output('admin_window-display-value_aw', 'children'),
    Input('admin_window-dropdown_aw', 'value'))
def display_value(value):
    print(r'{}/../data/logs/{}'.format(os.path.dirname(__file__), value))
    os.system(r'{}/data/logs/{}'.format(os.path.dirname(__file__), value))
    return 'You have selected "{}"'.format(value)


@app.callback(
    Output('admin_window-hit_rate_aw', 'children'),
    Input('train_mdl_aw', 'n_clicks'))
def update_output(n_clicks):
    k, hr = train.run()
    return 'hit_rate@{} = {}'.format(k, round(hr * 100, 2))
