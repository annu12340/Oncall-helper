from flask import Flask
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from pagerduty_api import get_pd_alerts
from process_alerts import group_by_alert_type, group_by_alert_count
from graph import create_graph1, create_graph2

app = Flask(__name__)


@app.route('/')
def main():
    result = get_pd_alerts()
    alert_dic1 = {}
    alert_dic2 = {}
    alert_dic1 = group_by_alert_type(result)
    alert_dic2 = group_by_alert_count(result)

    create_graph1(alert_dic1, alert_dic2)
    return None


if __name__ == '__main__':
    app.run()
