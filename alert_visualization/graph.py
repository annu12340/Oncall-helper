
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
    fig = make_subplots(rows=2, cols=1,
                        specs=[
                            [{'type': 'domain'}], [{'type': 'xy'}]
                        ])
    fig.add_trace(go.Pie(labels=key1, values=values1, name="Alert type"),
                  1, 1)
    fig.add_trace(go.Bar(x=[1, 2, 3], y=[4, 5, 6],
                         marker=dict(color=[4, 5, 6])),
                  2, 1)

    fig.update_layout(title="Dashboard", height=1300, showlegend=True)
    fig.show()


def create_graph(data):
    df = pd.DataFrame(list(data), columns=['alert', 'count'])
    fig = px.pie(df, values='count', names='alert',
                 color_discrete_sequence=px.colors.sequential.Aggrnyl)
    print("df\n\n\n\n", df)
    fig.show()
    fig.write_image("images/fig1.png")


def create_graph2(data):
    df = pd.DataFrame(list(data), columns=['alert', 'count'])
    fig = px.pie(df, values='count', names='alert',
                 color_discrete_sequence=px.colors.sequential.Aggrnyl)
    fig.show()
