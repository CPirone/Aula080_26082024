from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def send_simple_message(name, message):
    message = Mail(
        from_email=os.getenv('FIXED_FROM'),
        to_emails=os.getenv('FIXED_RECIPIENTS').split(','),
        subject=f'Novo usuário registrado: {name}',
        html_content=f'<strong>{message}</strong>'
    )
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))
