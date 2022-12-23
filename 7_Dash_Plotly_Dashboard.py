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
    dcc.Graph(id='success-pie-chart')
])

@app.callback(Output(component_id='success-pie-chart', component_property='figure'), 
    Input(component_id='site-dropdown', component_property='value'))
def render_success_pie_chart(input_value):
    if input_value == 'ALL':
        filtered_df = spacex_df
        fig = px.pie(data_frame=filtered_df, values='Class', names='Launch_Site', title='Total Successful Launches by Site')
    else:
        filtered_df = spacex_df[spacex_df['Launch_Site'] == input_value]
        fig = px.pie(data_frame=filtered_df, values='Class', names='Class', title=f'Total Successful Launches for {input_value}')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
