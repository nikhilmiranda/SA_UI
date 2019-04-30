# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:32:28 2019

@author: Ganesh Srinivas
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
#from classify import *
import Classification as c

app = dash.Dash()
vh1=[50.26, 56.22, 66.11, 35.69, 68.3, 56.61, 81.51, 60.28, 36.85, 33.24, 0.15]
vh2=[24.87, 3.98, 60.84, 53.67, 52.32, 57.82, 65.16, 56.17, 69.05, 40.19, -5.65]
vh3=[30.45, 12.27, 66.27, 70.86, 45.07, 59.25, 69.54, 62.9, 45.38, 41.48, -1.71]
vh4=[39.74, 79.0, 76.6, 48.63, 55.9, 61.98, 63.91, 62.7, 49.5, 59.08, 21.07]
#th1=[11.91, 24.45, 34.18, 20.76, 34.47, 32.14, 31.04, 35.73, 31.69, 23.52, 0.86]
#th2=[-2.98, 31.22, 32.16, 17.33, 32.57, 35.76, 26.79, 32.39, 34.54, 24.55, -0.58]
#th3=[8.44, 8.75, 32.78, 30.66, 25.96, 36.13, 26.49, 36.19, 27.1, 25.52, -0.2]
#th4=[10.55, 38.92, 35.52, 33.69, 26.71, 37.91, 28.19, 33.83, 25.85, 29.71, 13.73]
id1='2'

# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})  # noqa: E501

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='Sentiment Analysis of Hotel Reviews',
                        className='nine columns'),
                html.Div(children='''
                    Aspect Based Analysis
                        ''',
                        className='nine columns'
                )
            ], className="row"
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose Hotel:'),
                        dcc.Checklist(
                                id = 'Cities',
                                options=[
                                    {'label': 'Hotel 1', 'value': '1'},
                                    {'label': 'Hotel 2', 'value': '2'},
                                    {'label': 'Hotel 3', 'value': '3'},
                                    {'label': 'Hotel 4', 'value': '4'}
                                ],
                                values=['1', '2', '3', '4'],
                                labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
            ], className="row"
        ),

        html.Div(
            [
            html.Div([
                dcc.Graph(
                    id='example-graph'
                )
                ], className= 'twelve columns'
                )
            ], className="row"
        ),
                        
        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose Hotel:'),
                        dcc.Checklist(
                                id = 'Cities-1',
                                options=[
                                    {'label': 'Hotel 1', 'value': '1'},
                                    {'label': 'Hotel 2', 'value': '2'},
                                    {'label': 'Hotel 3', 'value': '3'},
                                    {'label': 'Hotel 4', 'value': '4'}
                                ],
                                values=['1', '2', '3', '4'],
                                labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
            ], className="row"
        ),
        html.Div(
            [
            html.Div([
                dcc.Graph(
                    id='example-graph-1'
                )
                ], className= 'twelve columns'
                )
            ], className="row"
        ),
                        
         html.Div([
            html.Label('Please Select a Hotel from the list'),
            dcc.Dropdown(
                    id='each',
                 options=[
                     {'label': 'Hotel 1', 'value': '1'},
                     {'label': 'Hotel 2', 'value': '2'},
                     {'label': 'Hotel 3', 'value': '3'},
                     {'label': 'Hotel 4', 'value': '4'}
                 ],
                 value='1'
                 #labelStyle={'display': 'inline-block'}
                 ),
        ]),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(
                            id='example-graph2',
                            figure={
                        'data': [
                            {'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel1_average, 'type': 'line', 'name': 'Hotel1'},
                            {'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel2_average, 'type': 'line', 'name': 'Hotel2'},
                            {'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel3_average, 'type': 'line', 'name': 'Hotel3'},
                            {'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel4_average, 'type': 'line', 'name': 'Hotel4'},
                        ],
                        'layout': {
                            'title': 'Graph 2'
                        }
                    }
                            #values=[1],
                            #labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='ten columns',
                    style={'margin-top': '10'}
                ),
            ], className="row"
        )
                        
#        html.Div(
#            [
#                html.Div(
#                    [
#                        html.P('Choose Hotel:'),
#                        dcc.Checklist(
#                                id = 'Cities-2',
#                                options=[
#                                    {'label': 'Hotel1', 'value': '1'},
#                                    {'label': 'Hotel2', 'value': '2'},
#                                    {'label': 'Hotel3', 'value': '3'},
#                                    {'label': 'Hotel4', 'value': '4'}
#                                ],
#                                values=['1', '2', '3', '4'],
#                                labelStyle={'display': 'inline-block'}
#                        ),
#                    ],
#                    className='six columns',
#                    style={'margin-top': '10'}
#                ),
#            ], className="row"
#        ),
#        html.Div(
#            [
#            html.Div([
#                dcc.Graph(
#                    id='example-graph-2'
#                )
#                ], className= 'twelve columns'
#                )
#            ], className="row"
#        ),
        
                        
        
    ], className='ten columns offset-by-one')
)                    

@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('Cities', 'values')])
def update_image_src(selector):
    data = []
    if '1' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel1_average, 'type': 'bar', 'name': 'Hotel1'})
    if '2' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel2_average, 'type': 'bar', 'name': 'Hotel2'})
    if '3' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel3_average, 'type': 'bar', 'name': 'Hotel3'})
    if '4' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel4_average, 'type': 'bar', 'name': 'Hotel4'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Overall Graph using Naive Bayes',
            'xaxis' : dict(
                title='Features',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='Percentage',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('example-graph-1', 'figure'),
    [dash.dependencies.Input('Cities-1', 'values')])
def update_image_src(selector):
    data = []
    if '1' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': vh1, 'type': 'bar', 'name': 'Hotel1'})
    if '2' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': vh2, 'type': 'bar', 'name': 'Hotel2'})
    if '3' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': vh3, 'type': 'bar', 'name': 'Hotel3'})
    if '4' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': vh4, 'type': 'bar', 'name': 'Hotel4'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Overall Graph using Vader Sentiment Analysis',
            'xaxis' : dict(
                title='Features',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='Percentage',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('example-graph2', 'figure'),
    [dash.dependencies.Input('each', 'value')])
def update_image_src(selector):
    data = []
    if '1' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel1_average, 'type': 'bar', 'name': 'Hotel1'})
    elif '2' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel2_average, 'type': 'bar', 'name': 'Hotel2'})
    elif '3' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel3_average, 'type': 'bar', 'name': 'Hotel3'})
    elif '4' in selector:
        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': c.hotel4_average, 'type': 'bar', 'name': 'Hotel4'})
    figure = {
        'data': data,
        'layout': {
            'title': 'Individual Summary of Selected Hotel',
            'xaxis' : dict(
                title='Features',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='Percentage',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

#@app.callback(
#    dash.dependencies.Output('example-graph-2', 'figure'),
#    [dash.dependencies.Input('Cities-2', 'values')])
#def update_image_src(selector):
#    data = []
#    if '1' in selector:
#        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': th1, 'type': 'bar', 'name': 'Hotel1'})
#    if '2' in selector:
#        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': th2, 'type': 'bar', 'name': 'Hotel2'})
#    if '3' in selector:
#        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': th3, 'type': 'bar', 'name': 'Hotel3'})
#    if '4' in selector:
#        data.append({'x': ['Affordability', 'Amenities', 'Cleanliness','Customer Support','Food','Location','Quietness','Staff','View','Payment','Wifi'], 'y': th4, 'type': 'bar', 'name': 'Hotel4'})
#    figure = {
#        'data': data,
#        'layout': {
#            'title': 'Overall Graph using TextBlob',
#            'xaxis' : dict(
#                title='Features',
#                titlefont=dict(
#                family='Courier New, monospace',
#                size=20,
#                color='#7f7f7f'
#            )),
#            'yaxis' : dict(
#                title='Percentage',
#                titlefont=dict(
#                family='Helvetica, monospace',
#                size=20,
#                color='#7f7f7f'
#            ))
#        }
#    }
#    return figure



if __name__ == '__main__':
    app.run_server(debug=True)
