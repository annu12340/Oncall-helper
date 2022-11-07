from slack import RTMClient
import psycopg2
hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'a'
port_id = 5432
conn = None


def search_db(text):
    print("entered")
    # Establishing the connection
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    create_script = f"""SELECT * FROM botdb1 where alert LIKE  '%{text}%'"""
    print("create_script", create_script)
    cursor.execute(create_script)
    a = cursor.fetchone()
    print(a[2])
    cursor.close()
    print("--------------------- done ---------------------")


@RTMClient.run_on(event="message")
def amusebot(**payload):
    data = payload["data"]
    web_client = payload["web_client"]
    bot_id = data.get("bot_id", "")

    # If a message is not send by the bot
    if bot_id == "":
        channel_id = data["channel"]

        # Extracting message send by the user on the slack
        text = data.get("text", "")
        text = text.split(">")[-1].strip()

        response = ""
        print("text", text)
        search_db(text)

        # Sending message back to slack
        web_client.chat_postMessage(channel=channel_id, text=response)


try:
    rtm_client = RTMClient(
        token="xoxb-4328155727859-4340911367537-hYcqbJH9x6IvRoU5WILTNI6e")
    print("Bot is up and running!")
    rtm_client.start()
except Exception as err:
    print(err)
