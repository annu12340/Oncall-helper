# Oncall helper

- Oncall can become a high stress environment. In such a scenario, going through tons of several documentations in order to resolve a highly critical issue can be time consuming and challenging. The oncall automation bot to an extend tries to resolve this issue

## Index 
- [Oncall helper](#oncall-helper)
    + [What it does](#what-it-does)
      - [1. PD auto response](#1-pd-auto-response)
      - [2. Automated oncall handoff mails](#2-automated-oncall-handoff-mails)
      - [3. Interactive dashboard](#3-interactive-dashboard)
    + [Main modules](#main-modules)
  * [Tech stack](#tech-stack)
  * [Code structure](#code-structure)
  * [Installation](#installation)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


### What it does 

#### 1. PD auto response 
- The bot mointers the internal documentations by periodically checking the SHA hash value of the documentation website. If the current SHA hash of the site doesn't match with the previous value, it indicates that the website has been modified
- Whenever there is an update in the content,  a web scrapping module is invoked. It scrapes the data and updates the PostgreSQL database
<img src="https://user-images.githubusercontent.com/43414928/200408377-7f4c711f-2cc5-4dc5-b1c5-3f357d74d9ab.png" height="330">
https://test-documentation101.netlify.app/ 
<p style="text-align:center">↓↓↓ (scrapes content from documentation and saves it to db) ↓↓↓ </p>
<img src="https://user-images.githubusercontent.com/43414928/200408392-cdb697ba-8aea-4a20-8396-3fffd944be4d.png" height="330">

- Slack’s Real-Time Messaging API (RTM API) allows us to receive events from Slack in real-time. The slack bot constantly checks for pagerduty alerts. 
- When a PD alert is triggered, the bot checks in the database to see if there is a match for the triggered incident in the documentation. If yes, it directly sends the alert resolution steps as a thread
- This would save the oncall engineer from the hustle of going through multiple documentations to resolve a particular issue

<img src="https://user-images.githubusercontent.com/43414928/200409779-e6908bc6-1596-4f94-bae7-f4f24656ddcc.png">
<img src="https://user-images.githubusercontent.com/43414928/200409787-314db920-72bf-4410-88dc-9d9a159fdbe7.png">

#### 2. Automated oncall handoff mails 
- Once the oncall is done, the oncall engineer is expected to capture the details regarding the most frequent alerts and share it with the team. The tool automates this process by capturing the most frequent alerts details  for the week and sends an automated email to the group mail id with the same
<img src="https://user-images.githubusercontent.com/43414928/200408678-f1d815d5-e1d4-4094-afb5-9281aec61c3c.gif">

#### 3. Interactive dashboard
- The tool also create a dashboard that aggregates pagerduty information and shows results like the most occurring type of alert, number of alerts that occurred in a week etc in a visual manner. 
<img src="https://user-images.githubusercontent.com/43414928/200406710-aec2f7a7-9c4a-45c3-a226-d939487f7ddb.gif">

### Main modules
- Document generator module
- Slack module
- Send automated mail module
- Alert visualization module

## Tech stack
- Python
- Flask
- Plotly: For creating interactive graphs
- Pandas
- schedule: For scheduling events
- Psycopg2: Postgress db connection
- BeautifulSoup: Web scrapping
- smtplib: For sending emails
- slack RTMClient: Real time slack message communication
- Logging

## Code structure
```
├───alert_visualization
│   ├───images: The images for the dashboard is stored in this folder
│   ├───static: Contains CSS for the dashboard
│   ├───templates: Contains the main index.html file
│   └───graph.py: Generated the bar and pie chart
│   ├───main.py: Starting point for the flask app
│   └───pagerduty_api.py: Generates JSON from pagerduty api
│   ├───process_alerts.py: Calculates the frequency of each alerts, counts of         alerts in a week etc from the PD JSON response 

├───generate_documentation_db
│   ├───database_connection: Used of creating and inserting data into        │       database
│   ├───web_scrapper.py: Scrapes the site when the hashs doesn't match

├───logs
│   ├───send_mail.logs
│   ├───scrapper.logs
│   ├───slack_bot.logs
│   └───visualization.logs
└───send_mail.py: Sends an automated oncall handooff mail after every 7 days
└───slack_bot.py: Recieves and process realtime slack messages
└───utils.py: Contains commonly used functions
```

## Installation
* Fork & Clone the repo
```
  git clone https://github.com/[yourname]/Oncall-helper.git
```

* Navigate through the project
```
  cd Oncall-helper
```
* Install all requirements
  ``` 
  pip install -r requirements.txt
  ```
* Create a file called password_config and include the following in it 
  ```
  BOT_TOKEN = ""
  SENDER_ID = "
  SENDER_PASSWORD = ""
  PAGERDUTY_TOKEN = ""
  ```
* Run :
  ```
  python3 <filename>.py
  ```