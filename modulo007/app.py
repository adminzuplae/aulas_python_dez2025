from flask import Flask, render_template, request, redirect, url_for, session
from viacep_service import consulta_cep
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'chave-secreta-cep'
app.permanent_session_lifetime = timedelta(minutes=5)

nome_sistema = 'Consulta CEP'

@app.route('/')
def home():
    endereco = session.get('endereco')
    error = session.get('error')
    return render_template('home.html', nome_sistema=nome_sistema, endereco=endereco, error=error)

@app.route('/cep', methods=['POST'])
def cep():
    cep = request.form.get('cep')
    session.pop('endereco', None)
    session.pop('error', None)
    try:
        resp = consulta_cep(cep)
        session['endereco'] = resp
        return redirect(url_for('home'))
    except Exception as e:
        session['error'] = str(e)
        return redirect(url_for('home'))


@app.route('/sobre')
def sobre():
    return render_template('sobre.html', nome_sistema=nome_sistema)

app.run(debug=True)