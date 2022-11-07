
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


l = {'|hadoop | proc_cluster@uk: hadoop sharedcachemanager JVM Uptime < 50': 15, '|Log pipeline Demux Replicator | abc_cluster@usa Category Latency > 100': 10, '|Onprem Replicator| efg_cluster@india: JVM uptime < 60': 9, '|GCP| xyz service down': 7, '|Docker container| Docker restart issues': 6,
     '|onprem| Capacity threshold execceded': 5, '|Hadoop| Unable to run new jobs on hadoop': 4, '|Hadoop| tst@india: Namenode Uptime Rate < 30': 2, '|hadoop| core-site.xml file missing': 1, }
alert_dic = sorted(l.items(), key=lambda x: x[1],  reverse=True)
create_pie_chart(alert_dic)
