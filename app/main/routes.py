from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.main.email import send_simple_message

main = Blueprint('main', __name__)

# Lista de usuários cadastrados (em memória)
registered_users = set()


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']

        # Verifica se o nome do usuário já foi registrado
        if name not in registered_users:
            send_simple_message(name, "Obrigado pelo submit na aula 070!")
            registered_users.add(name)
            flash('Email enviado!', 'Sucesso')
        else:
            flash('Usuário já registrado, email não enviado.', 'Informação')

        session['name'] = name
        return redirect(url_for('main.index'))

    name = session.get('name', None)
    return render_template('index.html',
                           name=name,
                           users=list(registered_users))
