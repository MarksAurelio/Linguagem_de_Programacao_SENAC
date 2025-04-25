import mysql.connector
from tkinter import messagebox
def conectar_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            port=3307,
            password="senac",
            database="cadastro_3" 
        )
    except mysql.connector.Error as err:
        print(f'Erro ao se conectar ao Mysql: {err}')
        return None

def criar_tabela():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id int AUTO_INCREMENT PRIMARY key, 
            username varchar (50) not null,
            idade varchar (50) not null
            )
        """)
    conn.commit()
    conn.close()

def inserir_usuario(username, idade):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (username, idade) VALUES (%s,%s)", (username, idade))
    conn.commit()
    conn.close()

def listar_alunos():
    conn = conectar_db()
    if conn is not None: # Verifica se a conexão foi bem-sucedida
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id, username, idade FROM usuarios")
            alunos = cursor.fetchall()
            return alunos  
        except mysql.connector.Error as err:
            print(f"Erro ao listar alunos: {err}")
            messagebox.showerror("Erro", f"Erro ao listar alunos.\nErro: {err}")
            return [] # Retorna uma lista vazia em caso de erro
        finally: # Garante que a conexão será fechada
            cursor.close()
            conn.close()
    