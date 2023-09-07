import smtplib
from email.message import EmailMessage
import celery

s = "zpycyvbbmvvigfte"

app = celery.Celery("main", broker="redis://localhost:6379/0")


@app.task()
def send_email(email):
    email_address = "imonqulovf1234@gmail.com"
    email_password = s
    msg = EmailMessage()
    msg['Subject'] = "Email Subject "
    msg['From'] = email_address
    msg['To'] = email
    msg.set_content('Salom bollar')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        print("send email")
