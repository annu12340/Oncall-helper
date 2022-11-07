
from flask import Flask, render_template
from pagerduty_api import get_pd_alerts
from process_alerts import group_by_alert_type, group_by_alert_count
from graph import create_pie_chart, create_bar_chart


app = Flask(__name__)


@app.route('/')
def main():
    # Get pagerduty API response
    result = get_pd_alerts()

    alert_dic, count = group_by_alert_type(result)
    alert_dic = sorted(alert_dic.items(), key=lambda x: x[1],  reverse=True)
    create_pie_chart(alert_dic)

    alert_dic, _ = group_by_alert_count(result)
    alert_dic = sorted(alert_dic.items(), key=lambda x: x[1],  reverse=True)
    create_bar_chart(alert_dic)
    return render_template('index.html', current_alerts=count)


if __name__ == '__main__':
    app.run()
