""" Entrega 1 – Apresentação do Projeto e Planejamento
 Apresentação dos objetivos do projeto integrador.
 Discussão dos temas possíveis.
 Definição do projeto por grupo (ou individual).
 Esboço no papel das telas e dados necessários.
Entrega parcial: Tema definido + protótipo desenhado com campos e funcionalidades. """

print('''
 _______  _______  _        _______  _______    ______   _______ 
(  ____ \(  ____ \( (    /|(  ___  )(  ____ \  (  __  \ (  ____ |
| (    \/| (    \/|  \  ( || (   ) || (    \/  | (  \  )| (    \/
| (_____ | (__    |   \ | || (___) || |        | |   ) || (__    
(_____  )|  __)   | (\ \) ||  ___  || |        | |   | ||  __)   
      ) || (      | | \   || (   ) || |        | |   ) || (      
/\____) || (____/\| )  \  || )   ( || (____/\  | (__/  )| )      
\_______)(_______/|/    )_)|/     \|(_______/  (______/ |/       
                                                                 
''')
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def cadastrar_aluno():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    email = entrada_email.get()
    curso = combo_curso_var.get()  

    if not nome or not idade or not email or not curso:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    if not idade.isdigit():
        messagebox.showerror("Erro", "A idade deve ser um número inteiro.")
        return

    aluno_info = f"Nome: {nome}, Idade: {idade}, Email: {email}, Curso: {curso}"
    lista_alunos.insert(tk.END, aluno_info)  

    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    combo_curso.set('')

janela = tk.Tk()
janela.title('Cadastro de Alunos')
janela.geometry('500x500')

combo_curso_var = tk.StringVar()  

label_nome = ttk.Label(janela, text='Nome Completo:')
label_nome.pack(padx=10, pady=5)
entrada_nome = ttk.Entry(janela, width=40)
entrada_nome.pack(padx=10, pady=5)

label_idade = ttk.Label(janela, text="Idade:")
label_idade.pack(pady=5)
entrada_idade = ttk.Entry(janela, width=10)
entrada_idade.pack(pady=5)

label_email = ttk.Label(janela, text="Email:")
label_email.pack(pady=5)
entrada_email = ttk.Entry(janela, width=40)
entrada_email.pack(pady=5)

label_curso = ttk.Label(janela, text="Curso:")
label_curso.pack(pady=5)
cursos = ['Engenharia de Software', "Ciência da Computação", "Programação de Sistemas", "Sistemas de Informação"]
combo_curso = ttk.Combobox(janela, textvariable=combo_curso_var, values=cursos, width=40)
combo_curso.pack(pady=5)
combo_curso.set("Selecione um curso")

botao_cadastrar = ttk.Button(janela, text="Cadastrar Aluno", command=cadastrar_aluno)
botao_cadastrar.pack(pady=10)

label_lista = ttk.Label(janela, text="Alunos Cadastrados:")
label_lista.pack(pady=10)
lista_alunos = tk.Listbox(janela, height=100, width=100)
lista_alunos.pack(pady=10)

janela.mainloop()
