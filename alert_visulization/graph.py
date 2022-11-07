
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go

import dash_core_components as dcc
import plotly.express as px
import plotly.subplots as sp
from plotly.subplots import make_subplots


def create_graph1(alert_dic1, alert_dic2):
    key1 = list(alert_dic1.keys())
    values1 = list(alert_dic1.values())

    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(rows=2, cols=2, specs=[
                        [{'type': 'domain'}, {'type': 'domain'}]])
    fig.add_trace(go.Pie(labels=key1, values=values1, name="GHG Emissions"),
                  1, 1)
    fig.add_trace(go.Pie(labels=['a', 'b', 'c', 'd', 'e', 'f'], values=[27, 11, 25, 8, 1, 3, 25], name="CO2 Emissions"),
                  1, 2)

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.4, hoverinfo="label+percent")

    fig.update_layout(
        title_text="",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='GHG', x=0.18, y=0.5, font_size=20, showarrow=False),
                     dict(text='CO2', x=0.82, y=0.5, font_size=20, showarrow=False)])
    fig.show()


def create_graph(data):
    df = pd.DataFrame(list(data), columns=['alert', 'count'])
    fig = px.pie(df, values='count', names='alert',
                 color_discrete_sequence=px.colors.sequential.Aggrnyl)
    print("df\n\n\n\n", df)
    fig.show()


def create_graph2(data):
    df = pd.DataFrame(list(data), columns=['alert', 'count'])
    fig = px.pie(df, values='count', names='alert',
                 color_discrete_sequence=px.colors.sequential.Aggrnyl)
    fig.show()
