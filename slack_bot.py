import os
from slack import RTMClient
import psycopg2
import logging
from utils import santify_text, db_connection_config
from password_config import BOT_TOKEN
log_format = "%(asctime)s::%(levelname)s::%(name)s::" "%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(filename='logs\slack_bot.log',
                    level='DEBUG', format=log_format)


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
    select_script = f"""SELECT * FROM botdb1 where alert LIKE  '%{text}%'"""
    logging.debug("Executing the script ", select_script)
    cursor.execute(select_script)
    result = cursor.fetchone()
    logging.info("------------- Successfully created the table ---------")
    cursor.close()
    return result[2]


@RTMClient.run_on(event="message")
def bot(**payload):
    data = payload["data"]
    web_client = payload["web_client"]
    bot_id = data.get("bot_id", "")
    timestamp = data.get("ts", "")

    # If message is send from pagerduty
    if bot_id == "B049FKBTWMU":
        logging.info("------------- Pagerduty has send an alert ---------")
        channel_id = data["channel"]

        # Extracting message send by the user on the slack
        title = data.get("attachments", "")[0].get("fallback").split(":", 1)[1]
        title = santify_text(title)
        if title:
            response = ""
            response = search_db(title)
            # Sending message back to slack
            web_client.chat_postMessage(
                channel=channel_id, text=response, thread_ts=timestamp)
            logging.info("------------- Send message to slack ---------")


try:
    rtm_client = RTMClient(
        token=BOT_TOKEN)
    print("Bot is up and running!")
    rtm_client.start()
except Exception as err:
    print(err)
