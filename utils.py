from datetime import datetime, timedelta
from beautifultable import BeautifulTable


def tabulate_response(alert_dic):
    response = ""
    for key, value in alert_dic.items():
        response.append(f"{key} -> {value}")
    return response


def find_date_N_days_ago(n):
    today = datetime.now()
    n_days_ago = today - timedelta(days=n)
    return n_days_ago.date()


def santify_text(text):
    if text:
        text = text.strip()
        text = text.replace("&gt;", ">")
        text = text.replace("&lt;", "<")
        text = text.replace("<p>", "")
        text = text.replace("</p>", "")
        text = text.replace("<code>", "```\n")
        text = text.replace("</code>", "\n```")
        return text


def db_connection_config():
    return {
        "hostname": 'localhost',
        "database": 'demo',
        "username": 'postgres',
        "pwd": 'a',
        "port_id": 5432,
        "conn": None
    }
