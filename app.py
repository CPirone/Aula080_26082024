import os
import requests
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)
print("FIXED_RECIPIENTS app.py:", os.getenv('FIXED_RECIPIENTS'))
# Configurações da API SendGrid obtidas de variáveis de ambiente
FIXED_RECIPIENTS = os.getenv('FIXED_RECIPIENTS').split(',')
FIXED_FROM = os.getenv('FIXED_FROM')

# Gere uma chave secreta segura (para produção, use uma chave mais complexa)
app.secret_key = secrets.token_hex(16)

def send_email(name, message):
    message = Mail(
        from_email=FIXED_FROM,
        to_emails=FIXED_RECIPIENTS,
        subject=f'Hello {name}!',
        html_content=f'<strong>{message}</strong>'
    )
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        return response
    except Exception as e:
        print(e.message)
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        response = send_email(name, "Obrigado pelo submit na aula 70!")
        if response and response.status_code == 202:  # SendGrid retorna 202 para sucesso
            flash('Email enviado!', 'success')
        else:
            flash('Falha ao enviar e-mail. Por favor, tente mais tarde.', 'danger')
        session['name'] = name
        return redirect(url_for('index'))

    name = session.get('name', None)
    return render_template('index.html', name=name)

if __name__ == '__main__':
     app.run(debug=True)