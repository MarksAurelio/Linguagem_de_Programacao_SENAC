''' Entrega 1 – Apresentação do Projeto e Planejamento
 Apresentação dos objetivos do projeto integrador.
 Discussão dos temas possíveis.
 Definição do projeto por grupo (ou individual).
 Esboço no papel das telas e dados necessários.
Entrega parcial: Tema definido + protótipo desenhado com campos e funcionalidades. '''
import tkinter as tk

def cadastrar_aluno():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    email = entrada_email.get()
    curso = entrada_curso.get()  
    
    if not nome or not idade or not email or curso == 'Selecione um curso':
        resultado.config(text='Há um ou mais campos sem preencher.', fg='red')
        return
    else:
        aluno_info = f'Nome: {nome}, Idade: {idade}, Email: {email}, Curso: {curso}'
        lista_alunos.insert(tk.END, aluno_info) 

    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_curso.set('Selecione um curso')
    resultado.config(text='')

janela = tk.Tk()
janela.title('Cadastro de Alunos')
janela.geometry('500x500')

entrada_curso = tk.StringVar()  

label_nome = tk.Label(janela, text='Nome Completo:')
label_nome.pack(padx=10, pady=5)
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(padx=10, pady=5)

label_idade = tk.Label(janela, text='Idade:')
label_idade.pack(pady=5)
entrada_idade = tk.Entry(janela, width=10)
entrada_idade.pack(pady=5)

label_email = tk.Label(janela, text='Email:')
label_email.pack(pady=5)
entrada_email = tk.Entry(janela, width=40)
entrada_email.pack(pady=5)

label_curso = tk.Label(janela, text='Curso:')
label_curso.pack(pady=5)
cursos = ['Engenharia de Software', 'Ciência da Computação', 'Programação de Sistemas', 'Sistemas de Informação']
entrada_curso.set('Selecione um curso')
opcoes_curso = tk.OptionMenu(janela, entrada_curso, *cursos)
opcoes_curso.config(width=37)
opcoes_curso.pack(pady=5)

tk.Button(janela, text='Cadastrar Aluno(a)', command=cadastrar_aluno).pack(pady=10)

label_lista = tk.Label(janela, text='Alunos Cadastrados:')
label_lista.pack(pady=10)
lista_alunos = tk.Listbox(janela, height=100, width=100)
lista_alunos.pack(pady=10)

resultado = tk.Label(janela, text='', fg='green')
resultado.pack(pady=5)

janela.mainloop()
