import os
from dotenv import load_dotenv
from email.message import EmailMessage
from email.utils import formataddr
import smtplib

def create_server():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    load_dotenv()
    server.login(os.getenv('SENDER_EMAIL'), os.getenv('EMAIL_PASSWORD'))
    print('Server / Login success')

    return server

def write_message(receiver_email, receiver_name, time, task):
    msg = EmailMessage()
    msg["Subject"] = "App Reminder"
    msg["From"] = formataddr((f"{ os.getenv('SENDER_NAME') }", f"{ os.getenv('SENDER_EMAIL') }"))
    msg["To"] = receiver_email

    msg.add_alternative(
        f"""\
        <html>
            <body>
                <p>Hello, <b>{ receiver_name }</b></p>
                <p>I hope you are doing well.</p>
                <p>We are sending you this email just to remind you of the current task you have to do or complete.</p>
                <p>Your next task is: <strong>{ task }</strong> and it must be done before <strong>{ time }</strong>.</p> 
                <p>Good luck.</p>
                <br />
                <p>Best regards</p>
            </body>
        </html>
        """,
        subtype='html'
    )

    return msg

def send_email(server, receiver_email, receiver_name, time, task):
    msg = write_message(receiver_email, receiver_name, time, task)

    server.sendmail(
        os.getenv('SENDER_EMAIL'), 
        receiver_email, 
        msg.as_string()
    )
    print(f'Email sent to { receiver_name }')