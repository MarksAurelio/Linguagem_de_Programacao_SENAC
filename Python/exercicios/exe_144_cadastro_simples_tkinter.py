""" Desenvolver uma aplicação gráfica simples com Tkinter, conectada a um banco de dados MySQL, que permita ao usuário cadastrar um login (usuário e senha) e exibir uma mensagem confirmando o cadastro.  
db.py → funções de banco de dados
ui.py → interface gráfica
main.py → ponto de entrada
#db.py
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sua_senha",  # substitua por sua senha real
        database="usuarios_db"
    )

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            senha VARCHAR(50) NOT NULL
        )
    )
    conn.commit()
    conn.close()

def inserir_usuario(username, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (username, senha) VALUES (%s, %s)", (username, senha))
    conn.commit()
    conn.close()


#ui.py
import tkinter as tk
from tkinter import messagebox
import db

def iniciar_interface():
    def cadastrar_usuario():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        if usuario and senha:
            db.inserir_usuario(usuario, senha)
            messagebox.showinfo("Sucesso", f"Usuário '{usuario}' cadastrado com sucesso!")
            entrada_usuario.delete(0, tk.END)
            entrada_senha.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos vazios", "Preencha todos os campos.")

    janela = tk.Tk()
    janela.title("Cadastro de Usuário")

    tk.Label(janela, text="Usuário:").grid(row=0, column=0)
    entrada_usuario = tk.Entry(janela)
    entrada_usuario.grid(row=0, column=1)

    tk.Label(janela, text="Senha:").grid(row=1, column=0)
    entrada_senha = tk.Entry(janela, show="*")
    entrada_senha.grid(row=1, column=1)

    btn_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_usuario)
    btn_cadastrar.grid(row=2, column=0, columnspan=2, pady=10)

    janela.mainloop()

#main.py
import db
import ui

if __name__ == "__main__":
    db.criar_tabela()
    ui.iniciar_interface()

Crear o banco antes de testar
CREATE DATABASE usuarios_db;pip install auto-py-to-exe """
