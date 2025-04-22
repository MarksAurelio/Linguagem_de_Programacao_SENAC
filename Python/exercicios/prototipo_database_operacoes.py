import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

db_host = 'localhost'
db_user = 'root'
db_password = 'senac'
db_port = 3307
db_database = 'app'

def conectar_db():
    try:
        meu_db = mysql.connector.connect(host=db_host, user=db_user, password=db_password, port=db_port, database=db_database)
        return meu_db
    except Error as e:
        messagebox.showerror('Erro de Banco de Dados', f'Erro ao conectar ao MySQL: {e}')
        return None

def criar_tabela_alunos():
    meu_db = conectar_db()
    if meu_db:
        meu_cursor = meu_db.cursor()
        try:
            meu_cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos (
                    matricula INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    idade INT NOT NULL,
                    curso VARCHAR(255) NOT NULL
                )
            ''')
            meu_db.commit()
        except Error as e:
            messagebox.showerror('Erro de Banco de Dados', f'Erro ao criar tabela: {e}')
        finally:
            if meu_cursor:
                meu_cursor.close()
            if meu_db and meu_db.is_connected():
                meu_db.close()

def cadastrar_aluno(nome, idade, curso):
    meu_db = conectar_db()
    if meu_db:
        meu_cursor = meu_db.cursor()
        try:
            sql = 'INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)'
            val = (nome, idade, curso)
            meu_cursor.execute(sql, val)
            meu_db.commit()
            return True
        except Error as e:
            messagebox.showerror('Erro de Banco de Dados', f'Erro ao cadastrar aluno: {e}')
            return False
        finally:
            if meu_cursor:
                meu_cursor.close()
            if meu_db and meu_db.is_connected():
                meu_db.close()
    return False

def buscar_aluno(termo_busca):
    meu_db = conectar_db()
    alunos_encontrados = []
    if meu_db:
        meu_cursor = meu_db.cursor()
        try:
            sql = 'SELECT matricula, nome, idade, curso FROM alunos WHERE LOWER(nome) LIKE %s'
            val = (f'%{termo_busca.lower()}%',)
            meu_cursor.execute(sql, val)
            alunos = meu_cursor.fetchall()
            for matricula, nome, idade, curso in alunos:
                alunos_encontrados.append({'matricula': matricula, 'nome': nome, 'idade': idade, 'curso': curso})
            return alunos_encontrados
        except Error as e:
            messagebox.showerror('Erro de Banco de Dados', f'Erro ao buscar alunos: {e}')
            return []
        finally:
            if meu_cursor:
                meu_cursor.close()
            if meu_db and meu_db.is_connected():
                meu_db.close()
    return []

def atualizar_aluno(matricula, novo_nome, nova_idade, novo_curso):
    meu_db = conectar_db()
    if meu_db:
        meu_cursor = meu_db.cursor()
        try:
            sql = 'UPDATE alunos SET nome=%s, idade=%s, curso=%s WHERE matricula=%s'
            val = (novo_nome, nova_idade, novo_curso, matricula)
            meu_cursor.execute(sql, val)
            meu_db.commit()
            return True
        except Error as e:
            messagebox.showerror('Erro de Banco de Dados', f'Erro ao atualizar aluno: {e}')
            return False
        finally:
            if meu_cursor:
                meu_cursor.close()
            if meu_db and meu_db.is_connected():
                meu_db.close()
    return False

def excluir_aluno_db(matricula):
    meu_db = conectar_db()
    if meu_db:
        meu_cursor = meu_db.cursor()
        try:
            sql = 'DELETE FROM alunos WHERE matricula=%s'
            val = (matricula,)
            meu_cursor.execute(sql, val)
            meu_db.commit()
            return True
        except Error as e:
            messagebox.showerror('Erro de Banco de Dados', f'Erro ao excluir aluno: {e}')
            return False
        finally:
            if meu_cursor:
                meu_cursor.close()
            if meu_db and meu_db.is_connected():
                meu_db.close()
    return False

def listar_alunos():
    meu_db = conectar_db()
    alunos_lista = []
    if meu_db:
        meu_cursor = meu_db.cursor()
        try:
            meu_cursor.execute('SELECT matricula, nome, idade, curso FROM alunos')
            alunos = meu_cursor.fetchall()
            for matricula, nome, idade, curso in alunos:
                alunos_lista.append({'matricula': matricula, 'nome': nome, 'idade': idade, 'curso': curso})
            return alunos_lista
        except Error as e:
            messagebox.showerror('Erro de Banco de Dados', f'Erro ao buscar alunos: {e}')
            return []
        finally:
            if meu_cursor:
                meu_cursor.close()
            if meu_db and meu_db.is_connected():
                meu_db.close()
    return []
