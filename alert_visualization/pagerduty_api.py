import requests
import json
from utils import find_date_N_days_ago


pagerduty_url = "https://api.pagerduty.com/incidents"


def get_pd_alerts(days=3):
    date = str(find_date_N_days_ago(days))
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
