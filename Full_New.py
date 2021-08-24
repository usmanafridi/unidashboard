import pandas as pd #(version 0.24.2)
import datetime as dt
import dash         #(version 1.0.0)
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import plotly       #(version 4.4.1)
import plotly.express as px

df=pd.read_csv('D:/KIU1.csv')
year = df.Year.drop_duplicates().sort_values()
AcTerm= df.AcademicTerm.drop_duplicates().sort_values()
app = dash.Dash(__name__)


app.layout = html.Div([
html.Div([
html.Div(
					children = [
						# Title and subtitle
						html.Div(
							children = [
								html.H2(
									children = "University Admission Portal",
									style = {
										"margin-bottom": "0",
										"color": "white"
									}
								),

							]
						)
					],
					className = "six column",
					id = 'title'
				),

html.Div([

        html.Div([
            html.Label(['Select Year'],style={'font-weight': 'bold', 'color':'white'}),
            dcc.Dropdown(
                id="dropdown",
                options=[{"label": x, "value": x} for x in year],
                value=year[0],
                clearable=False,
                style={"width": "55%", },
                className='dcc_compon'
            ),
        ], className='create_container three columns'),

html.Div([
            html.Label(['Select Academic Level'],style={'font-weight': 'bold', 'color':'white'}),
            dcc.Dropdown(
                id="dropdown2",
                options=[{"label": x, "value": x} for x in AcTerm],
                value=AcTerm[0],
                clearable=False,
                style={"width": "60%", },
                className='dcc_compon'
            ),
        ], className='create_container three columns'),
],className = "row flex-display",
			style = {
				"margin-bottom": "25px"
			}),
html.Div(
			children = [
				# (Column 1): Total Applied
				html.Div(
					children = [
						# Title
						html.H6(
							children = "Total Applied",
							style = {
								"textAlign": "center",
								"color": "white"
							}
						),
						# Total value
						html.P(id="card_1",
							children = "000",
							style = {
								"textAlign": "center",
								"color": "orange",
								"fontSize": 40
							}
						),

					],
					className = "create_container three columns", id="card1"
				),
				# (Column 2): Approved
				html.Div(
					children = [
						# Title
						html.H6(
							children = "Approved",
							style = {
								"textAlign": "center",
								"color": "white"
							}
						),
						# Total value
						html.P(id="card_2",
							children = "000",
							style = {
								"textAlign": "center",
								"color": "#dd1e35",
								"fontSize": 40
							}
						),

					],
					className = "card_container three columns"
				),
				# (Column 3): Pending
				html.Div(
					children = [
						# Title
						html.H6(
							children = "Pending",
							style = {
								"textAlign": "center",
								"color": "white"
							}
						),
						# Total recovered
						html.P(id="card_3",
							children = "000",
							style = {
								"textAlign": "center",
								"color": "green",
								"fontSize": 40
							}
						),

					],
					className = "card_container three columns"
				),
				# (Column 4): Declined
				html.Div(
					children = [
						# Title
						html.H6(
							children = "Declined",
							style = {
								"textAlign": "center",
								"color": "white"
							}
						),
						# Total v
						html.P(id="card_4",
							children = "000",
							style = {
								"textAlign": "center",
								"color": "#e55467",
								"fontSize": 40
							}
						),

					],
					className = "card_container three columns"
				)
			],
			className = "row flex-display"
		),

],id = "mainContainer",
	style = {
		"display": "flex",
		"flex-direction": "column"
	}),



html.Div([
html.Div(
					children = [
						# Donut chart
						dcc.Graph(
							id = "pie_chart",
							config = {
								"displayModeBar": "hover"
							}
						)
					],
					className = "create_container three columns",
					style = {
						"maxWidth": "400px"
					}
				),
html.Div(
					children = [
						# Donut chart
						dcc.Graph(
							id = "pie_chart1",
							config = {
								"displayModeBar": "hover"
							}
						)
					],
					className = "create_container three columns",
					style = {
						"maxWidth": "400px"
					}
				),
	html.Div([
		dcc.Graph(id='the_graph1')
	], className="create_container six columns"),

	],className = "row flex-display"),

html.Div([
    html.Div([
        dcc.Graph(id='the_graph')
    ],className = "create_container six columns"),



],className = "row flex-display"),
])
#-------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
     Input("dropdown", "value"),
     Input("dropdown2", "value"))




def update_graph( year, term):
    mask= (df['Year']==year) & (df['AcademicTerm']==term)


    dfg=df[mask].groupby('Department').count().reset_index()

    fig = {
        "data": [
            go.Bar(
                x=dfg['Department'],
                y=dfg['AppID'],
                name="Department Wise",
                marker={
                    "color": "orange"
                },
                hoverinfo="text",

            ),

        ],
        "layout": go.Layout(
            title={
                "text": f"Number of applications by Department in {term}, {year} ",
                "y": 0.93,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top"
            },
            titlefont={
                "color": "white",
                "size": 15
            },
            xaxis={
                "title": "<b>Department</b>",
                "color": "white",
                "showline": True,
                "showgrid": True,
                "showticklabels": True,
                "linecolor": "white",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "white",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Number of applications</b>",
                "color": "white",
                "showline": True,
                "showgrid": True,
                "showticklabels": True,
                "linecolor": "white",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "white",
                    "size": 12
                }
            },
            font={
                "family": "sans-serif",
                "color": "white",
                "size": 12
            },
            hovermode="closest",
            paper_bgcolor="#1f2c56",
            plot_bgcolor="#1f2c56",
            legend={
                "orientation": "h",
                "bgcolor": "#1f2c56",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )
    }
    # Return the figure
    return fig

@app.callback(
    Output(component_id='the_graph1', component_property='figure'),
     Input("dropdown", "value"),
     Input("dropdown2", "value"))




def update_graph( year,term):
    bins = [18, 25, 30, 35, 40]
    labels = ['18-24', '25-30', '30-35', '35-40']
    df['AgeGroup'] = pd.cut(df.Age, bins, labels=labels, include_lowest=True)

    mask = (df['Year'] == year) & (df['AcademicTerm'] == term)
    dfg=df[mask].groupby('AgeGroup').count().reset_index()

    fig = {
        "data": [
            go.Bar(
                x=dfg['AgeGroup'],
                y=dfg['AppID'],
                name="Age group wise",
                marker={
                    "color": "orange"
                },
                hoverinfo="text",

            ),

        ],
        "layout": go.Layout(
            title={
                "text": f"Number of applications by Age Group in {term}, {year} ",
                "y": 0.93,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top"
            },
            titlefont={
                "color": "white",
                "size": 15
            },
            xaxis={
                "title": "<b>Age Group</b>",
                "color": "white",
                "showline": True,
                "showgrid": True,
                "showticklabels": True,
                "linecolor": "white",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "white",
                    "size": 12
                }
            },
            yaxis={
                "title": "<b>Number of applications</b>",
                "color": "white",
                "showline": True,
                "showgrid": True,
                "showticklabels": True,
                "linecolor": "white",
                "linewidth": 1,
                "ticks": "outside",
                "tickfont": {
                    "family": "Aerial",
                    "color": "white",
                    "size": 12
                }
            },
            font={
                "family": "sans-serif",
                "color": "white",
                "size": 12
            },
            hovermode="closest",
            paper_bgcolor="#1f2c56",
            plot_bgcolor="#1f2c56",
            legend={
                "orientation": "h",
                "bgcolor": "#1f2c56",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.7
            }
        )
    }
    # Return the figure
    return fig



@app.callback(
    Output(component_id='pie_chart', component_property='figure'),
	Input("dropdown", "value"),
	Input("dropdown2", "value"))

def update_graph(year, term):


                            #make sure to make copy of the datafreame and never play with the original one.
	mask = (df['Year'] == year) & (df['AcademicTerm'] == term)
	labels = df[mask]['Gender'].unique()
	values = df[mask]['Gender'].value_counts()


	fig = {
								"data": [
									go.Pie(
										labels=labels,
										values=values,
										marker={

										},
										hoverinfo="label+value+percent",
										textinfo="percent",
										hole=0.7,
										rotation=45,
										insidetextorientation="radial"
									)
								],
								"layout": go.Layout(
									title={
										"text": f"Gender Proportion in {term}, {year}",
										"y": 0.93,
										"x": 0.5,
										"xanchor": "center",
										"yanchor": "top"
									},
									titlefont={
										"color": "white",
										"size": 15
									},
									font={
										"family": "sans-serif",
										"color": "white",
										"size": 12
									},
									hovermode="closest",
									paper_bgcolor="#1f2c56",
									plot_bgcolor="#1f2c56",
									legend={
										"orientation": "h",
										"bgcolor": "#1f2c56",
										"xanchor": "center",
										"x": 0.5,
										"y": -0.7
									}
								)
							}

	return fig

@app.callback(
    Output(component_id='pie_chart1', component_property='figure'),
	Input("dropdown", "value"),
	Input("dropdown2", "value"))

def update_graph(year, term):


#make sure to make copy of the datafreame and never play with the original one.
	mask = (df['Year'] == year) & (df['AcademicTerm'] == term)
	labels = ['BS', 'MS', 'PHD']
	values = df[mask]['AcademicLevel'].value_counts()


	fig = {
								"data": [
									go.Pie(
										labels=labels,
										values=values,

										hoverinfo="value+label+percent",
										textinfo="percent",

										rotation=45,
										insidetextorientation="radial"
									)
								],
								"layout": go.Layout(
									title={
										"text": f"Academic Level Proportion in {term}, {year}",
										"y": 0.93,
										"x": 0.5,
										"xanchor": "center",
										"yanchor": "top"
									},
									titlefont={
										"color": "white",
										"size": 15
									},
									font={
										"family": "sans-serif",
										"color": "white",
										"size": 12
									},
									hovermode="closest",
									paper_bgcolor="#1f2c56",
									plot_bgcolor="#1f2c56",
									legend={
										"orientation": "h",
										"bgcolor": "#1f2c56",
										"xanchor": "center",
										"x": 0.5,
										"y": -0.7
									}
								)
							}

	return fig

@app.callback(
    Output('card_1', 'children' ),
	Output('card_2', 'children' ),
	Output('card_3', 'children' ),
	Output('card_4', 'children' ),


	Input("dropdown", "value"),
	Input("dropdown2", "value"))
def update_card(year, term):
	mask = (df['Year'] == year) & (df['AcademicTerm'] == term)
	apps=df[mask]['AppID'].count()

	approved= df[mask]['Status'].value_counts().A

	pending=df[mask]['Status'].value_counts().P

	declined=df[mask]['Status'].value_counts().D
	return apps, approved, pending, declined


if __name__ == '__main__':
    app.run_server(debug=True, port=1239, )