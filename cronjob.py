import schedule
import time
import hashlib
import requests

url = 'https://bejewelled-travesseiro-b351da.netlify.app/'
response = requests.get(url).text
prevHash = hashlib.sha224(response.encode('utf8')).hexdigest()


# Function to check if new content has been added or removed from the documentation website


def check_if_website_has_changed():
    try:
        response = requests.get(url).text
        newHash = hashlib.sha224(response.encode('utf8')).hexdigest()
        global prevHash
        print("\n\n NewHash : ", newHash, "\n PrevHash : ", prevHash)

        if newHash != prevHash:
            print("New content has been added/removed")
            prevHash = newHash
    except Exception as e:
        print("error had occurred: ", e)


schedule.every(20).seconds.do(check_if_website_has_changed)

while True:
    schedule.run_pending()
    time.sleep(1)
