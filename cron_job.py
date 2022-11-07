import schedule
import time
import hashlib
import requests
import logging
from bs4 import BeautifulSoup

from database_connection import create_table, insert_into_table
from utils import santify_text

log_format = "%(asctime)s::%(levelname)s::%(name)s::"\
             "%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(filename='logs\mylogs.log',
                    level='DEBUG', format=log_format)
# Initialize a new database
create_table()

# Get SHA value for the website
url = 'http://127.0.0.1:5501/index.html'
response = requests.get(url).text
prevHash = hashlib.sha224(response.encode('utf8')).hexdigest()


def web_scrapper(result):
    doc = BeautifulSoup(result, "html.parser")
    response = doc.findAll(class_="main-section")

    database_content = []
    for count, result in enumerate(response):
        alert = result.find("header").text
        alert = santify_text(alert)

        alert_response = result.find("p")
        print("alert_response = result.find", result.find("p"))
        alert_response = santify_text(str(alert_response))
        database_content.append((count, alert, alert_response))

    # print("Database content:", database_content)
    return database_content


# Function to check if new content has been added or removed from the documentation website


def check_if_website_has_changed():
    try:
        global prevHash
        response = requests.get(url).text
        newHash = hashlib.sha224(response.encode('utf8')).hexdigest()
        logging.debug("Calculating SHA for ", url)
        logging.debug("\n\n NewHash : ", newHash, "\n PrevHash : ", prevHash)
        if newHash == prevHash:
            logging.info("New content has been added/removed")
            prevHash = newHash
            database_content = web_scrapper(response)
            insert_into_table(database_content)
    except Exception as e:
        logging.error("Error had occurred: ", e)


# schedule.every(30).seconds.do(check_if_website_has_changed)
check_if_website_has_changed()
while True:
    schedule.run_pending()
    time.sleep(1)
