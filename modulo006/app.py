from flask import Flask, render_template, request, redirect, url_for
from funcionarios_crud import salvar_funcionario, ler_funcionarios
from datetime import datetime

app = Flask(__name__)

nome_sistema='ZCadastro'
funcionarios_list = ['Ana', 'João', 'José', 'Maria']

@app.route('/')
def home():
    return render_template('home.html', nome_sistema=nome_sistema)

@app.route('/funcionarios')
def funcionarios():
    funcionarios_list = ler_funcionarios()
    return render_template('funcionarios/index.html', nome_sistema=nome_sistema, funcionarios=funcionarios_list)

@app.route('/funcionarios/create')
def funcionarios_create():
    return render_template('funcionarios/create.html', nome_sistema=nome_sistema)

@app.route('/funcionario/save', methods=['POST'])
def funcionario_salvar():
    nome_func = request.form.get('nome')
    sobrenome_func = request.form.get('sobrenome')
    idade_func = request.form.get('idade')
    salario_func = request.form.get('salario')
    ativo_func = True if request.form.get('ativo') else False
    salvar_funcionario(nome_func, sobrenome_func, idade_func, salario_func, ativo_func)

    return redirect(url_for('funcionarios'))
    

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', nome_sistema=nome_sistema)

@app.route('/contato')
def contato():
    return render_template('contato.html', nome_sistema=nome_sistema)

@app.context_processor
def inject_ano():
    return {'ano': datetime.now().year }

app.run(debug=True)