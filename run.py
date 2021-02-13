# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

def y_prima(t,y):
    return 2*y-5*np.sin(t)

T=np.pi/2 
N=100        
dt=T/N
t_exact = np.arange(0,T,dt)
y_exact = 2*np.sin(t_exact) + np.cos(t_exact)
y = [1]   
t = [0]
while t[-1] <= T:
    y_new = y[-1] + y_prima(t[-1],y[-1])*dt
    t_new =  t[-1] + dt
    y.append(y_new)
    t.append(t_new)

fig1 = px.line(x=t,y=y,labels={'x':'t', 'y':'Euler'})
fig2=px.scatter(x=t_exact,y=y_exact,labels={'x':'t', 'y':'Exacta'})
fig1.show()

fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Label(
        'Dropdown',
        style={
            'width': '49%',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph-2',
        figure=fig1
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)