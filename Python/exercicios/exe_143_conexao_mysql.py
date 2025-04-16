""" O objetivo desta atividade é criar uma interface gráfica de cadastro de usuários utilizando a biblioteca Tkinter, com integração ao banco de dados MySQL. O programa deverá permitir que o usuário insira seu nome e senha e, ao clicar no botão "Cadastrar", esses dados sejam armazenados em uma tabela no banco de dados.  Instalar a biblioteca: pip install mysql-connector-python

import tkinter as tk
import mysql.connector
from mysql.connector import Error

# Função para criar a conexão com o banco de dados
def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="usuario"
        )
        return conexao
    except Error as e:
        mensagem.config(text=f"Erro na conexão: {e}", fg="red")
        return None

# Função para criar a tabela se não existir
def criar_tabela(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute(
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                senha VARCHAR(50) NOT NULL
            )
       )
        conexao.commit()
    except Error as e:
        mensagem.config(text=f"Erro ao criar tabela: {e}", fg="red")

# Função para cadastrar usuário
def cadastrar():
    nome = entrada_nome.get()
    senha = entrada_senha.get()

    if nome and senha:
        conexao = criar_conexao()
        if conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (%s, %s)", (nome, senha))
                conexao.commit()
                conexao.close()

                mensagem.config(text="Usuário cadastrado com sucesso!", fg="green")
                entrada_nome.delete(0, tk.END)
                entrada_senha.delete(0, tk.END)
            except Error as e:
                mensagem.config(text=f"Erro ao cadastrar: {e}", fg="red")
        else:
            mensagem.config(text="Falha na conexão com o banco.", fg="red")
    else:
        mensagem.config(text="Preencha todos os campos!", fg="red")

# Interface gráfica
janela = tk.Tk()
janela.title("Cadastro de Usuário - MySQL")
janela.geometry("300x250")

tk.Label(janela, text="Nome de usuário").pack(pady=5)
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack()

tk.Label(janela, text="Senha:").pack(pady=5)
entrada_senha = tk.Entry(janela, show="*", width=30)
entrada_senha.pack()

mensagem = tk.Label(janela, text="", fg="red")
mensagem.pack()

tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=10)

# Criando a conexão e a tabela apenas uma vez
conexao = criar_conexao()
if conexao:
    criar_tabela(conexao)

janela.mainloop() """
import tkinter as tk
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            password="senac",
            database="cadastro"
        )
        return connection
    except Error as e:
        message.config(text=f"Connection error: {e}", fg="red")
        return None

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                senha VARCHAR(50) NOT NULL
            )
        """)
        connection.commit()
    except Error as e:
        message.config(text=f"Error creating table: {e}", fg="red")

def register():
    name = entry_name.get()
    password = entry_password.get()

    if name and password:
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (%s, %s)", (name, password))
                connection.commit()
                connection.close()
                message.config(text="User registered successfully!", fg="green")
                entry_name.delete(0, tk.END)
                entry_password.delete(0, tk.END)
            except Error as e:
                message.config(text=f"Error registering: {e}", fg="red")
        else:
            message.config(text="Failed to connect to the database.", fg="red")
    else:
        message.config(text="Fill in all the fields!", fg="red")

window = tk.Tk()
window.title("User Registration - MySQL")
window.geometry("300x250")

tk.Label(window, text="Username").pack(pady=5)
entry_name = tk.Entry(window, width=30)
entry_name.pack()

tk.Label(window, text="Password:").pack(pady=5)
entry_password = tk.Entry(window, show="*", width=30)
entry_password.pack()

message = tk.Label(window, text="", fg="red")
message.pack()

tk.Button(window, text="Register", command=register).pack(pady=10)

# Creating the connection and the table only once
connection = create_connection()
if connection:
    create_table(connection)
    if connection.is_connected(): # Ensure connection is still open before closing
        connection.close()

window.mainloop()
