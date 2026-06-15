import smtplib
from email.mime.text import MIMEText

from config.settings import *

def send_email(body):

    msg = MIMEText(body)

    msg["Subject"] = "Daily Job Report"
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_TO

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as server:

        server.login(
            EMAIL_USER,
            EMAIL_PASSWORD
        )

        server.send_message(msg)
