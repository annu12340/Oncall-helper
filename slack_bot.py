from slack import RTMClient
import psycopg2
from utils import santify_text

from utils import db_connection_config


def search_db(text):
    print("entered")
    # Establishing the connection

    config = db_connection_config()
    # Establishing the connection
    conn = psycopg2.connect(
        host=config["hostname"],
        dbname=config["database"],
        user=config["username"],
        password=config["pwd"],
        port=config["port_id"])
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    create_script = f"""SELECT * FROM documentationdb where alert LIKE  '%{text}%'"""
    print("create_script", create_script)
    cursor.execute(create_script)
    a = cursor.fetchone()
    cursor.close()
    print("--------------------- done ---------------------")
    return a[2]


@RTMClient.run_on(event="message")
def amusebot(**payload):
    data = payload["data"]
    web_client = payload["web_client"]
    bot_id = data.get("bot_id", "")
    timestamp = data.get("ts", "")
    print("\n\n -------------------------------- \ndata", data)
    text = ''
    # If a message is not send by the bot
    if bot_id == "B049FKBTWMU":
        channel_id = data["channel"]

        # Extracting message send by the user on the slack
        title = data.get("attachments", "")[0].get("fallback").split(":", 1)[1]
        print("^^^ title", title)
        title = santify_text(title)
        if title:
            response = ""
            response = search_db(title)
            print("****", response)
            # Sending message back to slack
            web_client.chat_postMessage(
                channel=channel_id, text=response, thread_ts=timestamp)
            print("################################## DONE #############3")


try:
    rtm_client = RTMClient(
        token="xoxb-4328155727859-4340911367537-hYcqbJH9x6IvRoU5WILTNI6e")
    print("Bot is up and running!")
    rtm_client.start()
except Exception as err:
    print(err)
