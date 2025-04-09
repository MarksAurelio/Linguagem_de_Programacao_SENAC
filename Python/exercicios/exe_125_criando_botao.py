import tkinter as tk

def dizer_ola():
    print("Olá, Mundo!")  # Isso aparece no terminal, não na janela

janela = tk.Tk()
janela.title("Janela com Botão")

# Criando um botão
botao = tk.Button(
    janela,  # Indica que o botão pertence à janela
    text="Clique aqui",  # Texto que aparece no botão
    command=dizer_ola  # Função que será chamada ao clicar
)

# Empacotando o botão na janela (isso o exibe)
botao.pack()

janela.mainloop()

"""
Criamos uma função dizer_ola() que será chamada quando o botão for clicado
tk.Button() cria um botão com texto e ação
.pack() é um gerenciador de layout simples que coloca o widget na janela """

# Atividade:
# Mostrar no terminal uma frase de saudação, por exemplo: "Bem vindo(a)!"

def dizer_bem_vindo():
    print('Bem vindo!')

janela1 = tk.Tk()
janela1.geometry('600x400')
janela1.title('Janela1 com Botão')
botao1= tk.Button(
    janela1,
    text='Clique aqui',
    command=dizer_bem_vindo, width=20, height=8)
botao1.pack()
janela1.mainloop()
