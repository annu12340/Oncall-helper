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
