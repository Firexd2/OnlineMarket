from django.core.mail import EmailMessage
from ProjectOnlineMarket.Celery import app


@app.task
def send_verification_email(to_email, message, mail_subject):
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
