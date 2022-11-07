import requests
import json
from datetime import datetime, timedelta


pagerduty_url = "https://api.pagerduty.com/incidents"


def find_date_N_days_ago(n):
    today = datetime.now()
    n_days_ago = today - timedelta(days=n)
    return n_days_ago.date()


def get_pd_alerts():
    date = str(find_date_N_days_ago(3))
    querystring = {"since": date}

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.pagerduty+json;version=2",
        "Authorization": "Token token=u+-ro5VqyBrzeNfT8EJQ"
    }

    response = requests.request(
        "GET", pagerduty_url, headers=headers, params=querystring)

    result = json.loads(response.text).get("incidents")
    print("\n\n ---------------------", result)
    return result
