import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(name):
    # Obter destinatários fixos das variáveis de ambiente
    FIXED_RECIPIENTS = os.getenv('FIXED_RECIPIENTS').split(',')
    FIXED_FROM = os.getenv('FIXED_FROM')

    # Definir a mensagem de e-mail
    message = Mail(
        from_email=FIXED_FROM,
        to_emails=FIXED_RECIPIENTS,
        subject='Assunto do E-mail',
        html_content=f'<strong>Olá, {name}!</strong>'
    )

    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        return response.status_code == 202
    except Exception as e:
        print(f"Erro ao enviar e-mail: {str(e)}")  # Usar str(e) para exibir a mensagem de erro
        return False
