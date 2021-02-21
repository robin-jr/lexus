
import smtplib
from email.mime.text import MIMEText


def send_mail(name, email):
    port = 25
    smptserver = "smtp.mailtrap.io"
    login = "3071bbc1362c0f"
    password = "682faa3e9faa43"
    message = f"<h3>A response from {name} with email address {email}</h3>"
    sender_email = 'jrnspark@gmail.com'
    receiver_email = 'jrnstudy@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Sample Email'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smptserver, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
