
import pandas as pd
import plotly.express as px


def create_pie_chart(data):
    df = pd.DataFrame(list(data), columns=['alert', 'count'])
    fig = px.pie(df, values='count', names='alert',
                 color_discrete_sequence=px.colors.sequential.Aggrnyl)
    fig.write_image("images/alert_frequency.png")
    fig.show()


def create_bar_chart(data):
    df = pd.DataFrame(list(data), columns=['alert', 'count'])
    fig = px.bar(df, y='count', x='alert')
    fig.write_image("images/alert_count.png")
    fig.show()
