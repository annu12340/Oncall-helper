
import imghdr
import logging
import smtplib
import ssl
import schedule
import time
from email.message import EmailMessage
from datetime import datetime, timedelta
from alert_visualization import pagerduty_api, process_alerts
from password_config import SENDER_ID, SENDER_PASSWORD

log_format = "%(asctime)s::%(levelname)s::%(name)s::" "%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(filename='logs\send_email.log',
                    level='DEBUG', format=log_format)


def get_pagerduty_response():
    result = pagerduty_api.get_pd_alerts(7)
    logging.info("Got pagerduty api response")
    alert_dic, count = process_alerts.group_by_alert_type(result)
    alert_dic = dict(
        sorted(alert_dic.items(), key=lambda x: x[1],  reverse=True))
    response = ""
    for key, value in alert_dic.items():
        response += (f"\n\n\t\t*{key} -> {value}")

    return response, count


def generate_email_body():
    today = datetime.now()
    past_date = today - timedelta(days=7)
    result, count = get_pagerduty_response()
    body = f"""Weekly report for {past_date.date()} - {today.date()} 
    \n\n This week there were a total of {count} alerts. The most frequent alerts were :-  {result}
    """
    logging.debug("Generated email body content ")
    return body


def send_mail():
    # Define email sender and receiver
    email_sender = SENDER_ID
    email_password = SENDER_PASSWORD
    email_receiver = '2000annujolly@gmail.com'

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = 'Weekly oncall report'
    body = generate_email_body()
    em.set_content(body)

    with open('alert_visualization/images/alert_frequency.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    em.add_attachment(image_data, maintype='image',
                      subtype=image_type, filename=image_name)
    logging.debug("EmailMessage object is created")
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    logging.info("------------- Email send successfully ---------")


schedule.every(7).days.do(send_mail)

while True:
    schedule.run_pending()
    time.sleep(1)
