from flask import Flask, render_template
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from pagerduty_api import get_pd_alerts
from process_alerts import group_by_alert_type, group_by_alert_count
from graph import create_graph, create_graph2

app = Flask(__name__)


@app.route('/')
def main():
    result = get_pd_alerts()
    alert_dic, count = group_by_alert_type(result)
    alert_dic = sorted(alert_dic.items(), key=lambda x: x[1],  reverse=True)
    create_graph(alert_dic)

    alert_dic, count = group_by_alert_count(result)
    alert_dic = sorted(alert_dic.items(), key=lambda x: x[1],  reverse=True)
    create_graph2(alert_dic)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
