import tkinter as tk
from tkinter import messagebox
import mysql.connector 

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
        messagebox.showerror('Erro de Conexão', f'Não foi possível conectar ao banco de dados. Erro: {err}')
        return None

def criar_tabela():
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    idade VARCHAR(50) NOT NULL
                )
            """)
            conn.commit()
            messagebox.showinfo('Tabela Criada', 'Tabela "usuarios" criada com sucesso!')
        except mysql.connector.Error as err:
            print(f'Erro ao criar tabela: {err}')
            messagebox.showerror('Erro ao Criar Tabela', f'Erro ao criar a tabela "usuarios". Erro: {err}')
        finally:
            cursor.close()
            conn.close()

def inserir_usuario(username, idade):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO usuarios (username, idade) VALUES (%s, %s)', (username, idade))
            conn.commit()
            messagebox.showinfo('Sucesso', f'Aluno {username} cadastrado com sucesso!')
        except mysql.connector.Error as err:
            print(f'Erro ao inserir usuário: {err}')
            messagebox.showerror('Erro ao Inserir Usuário', f'Erro ao inserir usuário. Erro: {err}')
        finally:
            cursor.close()
            conn.close()

def listar_alunos():
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT id, username, idade FROM usuarios')
            alunos = cursor.fetchall()
            return alunos
        except mysql.connector.Error as err:
            print(f'Erro ao listar alunos: {err}')
            messagebox.showerror('Erro ao Listar Alunos', f'Erro ao listar os alunos. Erro: {err}')
            return []
        finally:
            cursor.close()
            conn.close()

def iniciar_interface():
    criar_tabela()  

    def cadastrar_aluno():
        aluno = entrada_aluno.get()
        idade = entrada_idade.get()
        if aluno and idade:
            inserir_usuario(aluno, idade) 
            entrada_aluno.delete(0, tk.END)
            entrada_idade.delete(0, tk.END)
        else:
            messagebox.showwarning('Campos vazios', 'Preencha todos os campos.')

    def mostrar_alunos_interface():
        alunos = listar_alunos()  
        if alunos:
            texto = '\n'.join(f'{nome} ({idade} anos)' for _, nome, idade in alunos)  
            messagebox.showinfo('Alunos Cadastrados', texto)
        else:
            messagebox.showinfo('Sem Alunos', 'Não há alunos cadastrados.')

    janela = tk.Tk()
    janela.title('Cadastro de Alunos')
    janela.geometry('500x300')

    tk.Label(janela, text='Nome do Aluno:').pack(pady=10)
    entrada_aluno = tk.Entry(janela)
    entrada_aluno.pack(pady=10)

    tk.Label(janela, text='Idade do Aluno:').pack(pady=10)
    entrada_idade = tk.Entry(janela)
    entrada_idade.pack(pady=10)

    tk.Button(janela, text='Cadastrar Aluno(a)', command=cadastrar_aluno).pack(pady=10)
    tk.Button(janela, text='Listar Alunos(a)', command=mostrar_alunos_interface).pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    iniciar_interface()
