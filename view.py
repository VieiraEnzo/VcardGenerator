from flask import Flask, render_template, request
from control import Cartao, Usuario


app = Flask(__name__)


#Funćao para verificar se o usuario está no BD
def valida_senha(nome,senha):
    #codigo
    return render_template('###tela inserir informaćoes###')
    #if usuario not in DB return render_template("##tela de login", erro = "Email ou senha invalidos")
    

#tela inicial do site (login)
@app.route("/")
def index():
    return render_template('###tela de login###')


#Submite do Forms da tela de login
@app.route("/login")
def login():
    nome = request.form["nome"]
    senha = request.form["senha"]
    return valida_senha(nome, senha)


#Funcão para criar o cartão
def cria_cartao(card):
    #criar um qrcode
    #armazena no BD
    return render_template("###tela final da imagem")


#Tela de insercão de informacões
@app.route("/info")
def information():
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    site = request.form["site"]
    email = request.form["email"]
    end = request.form["end"]
    card = Cartao(nome,telefone,site,email,end)
    return cria_cartao(card)


#Funćão que insere o usuario na DATABASE
def insert_usuario_DB(user):
    #codigo
    return render_template("###tela de login")


@app.route("/CriaConta")
def Cria_Conta():
    login = request.form["login"]
    nome_completo = request.form["nome_completo"]
    senha = request.form["senha"]
    senha_ctrl = request.form["senha_repetida"]
    if senha == senha_ctrl:
        return render_template("###tela de registro", erro = "As senhas precisam ser iguais")
    else:        
        user = Usuario(login,nome_completo,senha)
        return insert_usuario_DB(user)


@app.route("/register")
def register():
    return render_template("###tela de registro")