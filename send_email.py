

from alert_visualization import pagerduty_api, process_alerts
import smtplib
import ssl
from email.message import EmailMessage
import datetime
import sys
from pathlib import Path
from datetime import datetime, timedelta
import os.path
import sys
from utils import tabulate_response
import imghdr


def main():
    result = pagerduty_api.get_pd_alerts(7)
    alert_dic, count = process_alerts.group_by_alert_type(result)
    alert_dic = dict(
        sorted(alert_dic.items(), key=lambda x: x[1],  reverse=True))
    response = ""
    for key, value in alert_dic.items():
        response += (f"\n\n\t\t*{key} -> {value}")
    return response, count


with open('fig1.png', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name


# Define email sender and receiver
email_sender = 'annuqwerty123@gmail.com'
email_password = 'rzhorjpxbzdagsvw'
email_receiver = 'annujolly17@gmail.com'
today = datetime.now()
past_date = today - timedelta(days=7)
result, count = main()
# Set the subject and body of the email
subject = 'Weekly oncall report'
body = f""" 
 Weekly report for {past_date.date()} - {today.date()} 
 \n\n This week there were a lot of {count} alerts. The most frequent alerts were :-  {result}
"""
body.format('\033[1m', body)


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
em.add_attachment(image_data, maintype='image',
                  subtype=image_type, filename=image_name)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
