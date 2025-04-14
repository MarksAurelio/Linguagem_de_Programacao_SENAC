""" Crie um programa em Tkinter que permita ao usuário digitar um nome de produto em uma Entry e, ao clicar no botão "Adicionar", o produto seja adicionado à Listbox.  

import tkinter as tk

def adicionar_produto():
    produto = entrada.get()
    if produto:  # Se tiver texto, adiciona
        resultado.insert(tk.END, produto)
        entrada.delete(0, tk.END)
        aviso.config(text="")  # Limpa a mensagem de aviso, se houver
    else:
        aviso.config(text="⚠️ Por favor, digite o nome de um produto.", fg="red")

# Janela principal
janela = tk.Tk()
janela.title("Cadastro de Produtos")

# Label e Entry
tk.Label(janela, text="Digite o nome do produto:").pack(pady=5)
entrada = tk.Entry(janela, width=50)
entrada.pack(pady=5)

# Aviso (mensagem de erro)
aviso = tk.Label(janela, text="", fg="red")
aviso.pack()

# Botão
botao = tk.Button(janela, text="Adicionar", command=adicionar_produto)
botao.pack(pady=5)

# Listbox
tk.Label(janela, text="Produtos Cadastrados:").pack(pady=5)
resultado = tk.Listbox(janela, width=50, height=10)
resultado.pack()

# Loop da janela
janela.mainloop() """

import tkinter as tk
def adicionar_produto():
    produto = entrada.get()
    if produto:
        resultado.insert(tk.END, produto)
        entrada.delete(0, tk.END)
        aviso.config(text='')
    else:
        aviso.config(text='Digite o nome do produto: ', fg='red')

janela = tk.Tk()
janela.title('Cadastro de produtos')

tk.Label(janela, text='Digite o nome do produto: ').pack(pady=5)
entrada = tk.Entry(janela, width=50)
entrada.pack(pady=5)

aviso = tk.Label(janela, text='', fg='red')
aviso.pack()

botao = tk.Button(janela, text='Clique aqui', command=adicionar_produto)
botao.pack(pady=5)

tk.Label(janela, text='Produtos cadastrados: ').pack(pady=5)
resultado = tk.Listbox(janela, width=50, height=10)
resultado.pack()

janela.mainloop()
