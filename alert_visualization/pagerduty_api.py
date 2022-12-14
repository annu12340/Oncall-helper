import requests
import json
import logging
from datetime import datetime, timedelta
from password_config import PAGERDUTY_TOKEN

pagerduty_url = "https://api.pagerduty.com/incidents"


def get_pd_alerts(no_of_days=3):
    n_days_ago = datetime.now() - timedelta(days=no_of_days)
    date = n_days_ago.date()
    token = "Token token="+PAGERDUTY_TOKEN
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.pagerduty+json;version=2",
        "Authorization": token
    }

    response = requests.request(
        "GET", pagerduty_url, headers=headers, params={"since": date})
    result = json.loads(response.text).get("incidents")
    return result
