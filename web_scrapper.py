from bs4 import BeautifulSoup
import requests

url_link = "https://bejewelled-travesseiro-b351da.netlify.app/"
result = requests.get(url_link).text

doc = BeautifulSoup(result, "html.parser")
response = doc.findAll(class_="main-section")

for result in response:
    alert = result.find("header")
    print(alert)
    alert_solution = result.find("p")
    print(alert_solution)
