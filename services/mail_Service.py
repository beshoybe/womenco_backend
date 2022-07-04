from http.client import INTERNAL_SERVER_ERROR
from threading import Thread
from flask import render_template
from flask_mail import Message
from app import app,mail

def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except ConnectionRefusedError:
            raise INTERNAL_SERVER_ERROR("[MAIL SERVER] not working")


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()


