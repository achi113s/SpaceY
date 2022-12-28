import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv('datasets/launch_data_falcon9_wiki.csv')

# create booster version category column
spacex_df['Booster_Version_Category'] = spacex_df['Booster_Version'].map(
    lambda x: x.split()[1])

max_payload = spacex_df['Payload_Mass'].max()
min_payload = spacex_df['Payload_Mass'].min()

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Space X Launch Records Dashboard',
            style={'textAlign': 'center'}),
    dcc.Dropdown(options=[{'label': 'All Sites', 'value': 'ALL'},
                  {'label': 'CCSFS SLC-40', 'value': 'CCSFS SLC-40'},
                  {'label': 'CCSFS LC-40', 'value': 'CCSFS LC-40'}, 
                  {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}, 
                  {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'}],
                  id='site-dropdown',
                  value='ALL',
                  placeholder='Select a Launch Site Here',
                  searchable=True),
    dcc.Graph(id='success-pie-chart'),
    html.H3(children='Payload Mass Slider'),
    dcc.RangeSlider(id='payload-slider', min=min_payload, max=max_payload, step=1000, value=[min_payload, max_payload]),
    dcc.Graph(id='success-payload-scatter-chart')
])

@app.callback(Output(component_id='success-pie-chart', component_property='figure'), 
    Input(component_id='site-dropdown', component_property='value'))
def render_success_pie_chart(input_value):
    if input_value == 'ALL':
        filtered_df = spacex_df
        fig = px.pie(data_frame=filtered_df, values='Class', 
            names='Launch_Site', title='Total Successful Launches by Site')
    else:
        filtered_df = spacex_df[spacex_df['Launch_Site'] == input_value]
        fig = px.pie(data_frame=filtered_df, names='Class', 
            title=f'Total Successful Launches for {input_value}')
    return fig


@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'), 
    Input(component_id='payload-slider', component_property='value'), 
    Input(component_id='site-dropdown', component_property='value'))
def render_success_payload_scatter(slider_range, launch_site):
    if launch_site == 'ALL':
        filtered_df = spacex_df[(spacex_df['Payload_Mass'] > slider_range[0]) & (spacex_df['Payload_Mass'] < slider_range[1])]
        fig = px.scatter(data_frame=filtered_df, x='Payload_Mass', y='Class', color='Booster_Version_Category', title='Successful Landings by Payload Mass and Booster Version for All Sites')
    else:
        filtered_df = spacex_df[(spacex_df['Payload_Mass'] > slider_range[0]) & (spacex_df['Payload_Mass'] < slider_range[1])]
        filtered_df = filtered_df[filtered_df['Launch_Site'] == launch_site]
        fig = px.scatter(data_frame=filtered_df, x='Payload_Mass', y='Class', color='Booster_Version_Category', title=f'Successful Landings by Payload Mass and Booster Version for {launch_site}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

"""
Which site has the largest successful launches?
    CCSFS SCL-40 has the largest successful launches.
Which site has the highest launch success rate?
    CCSFS SCL-40 also has the highest launch success rate.
Which payload range(s) has the highest launch success rate?
    The highest launch success rate occurs in the 10-16k payload range.
Which payload range(s) has the lowest launch success rate?
    0-6k is the payload range with the lowest launch success rate.
Which F9 Booster version (v1.0, v1.1, FT, B4, B5, etc.) has the highest
launch success rate?
    The B5 F9 booster version has the highest launch success rate.
"""