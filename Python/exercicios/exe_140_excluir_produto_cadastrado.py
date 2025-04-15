""" Crie um programa em Python usando Tkinter que permita excluir um produto previamente cadastrado. Ao clicar no botão "Excluir Produto", o item será excluido da lista.

def excluir_produto():
    selecao = resultado.curselection()              # Obtém o índice do item selecionado
    if not selecao:                                   # Se nenhum item foi selecionado
        mensagem.config(text="Selecione um produto para excluir.", fg="red")
        return
    indice = selecao[0]                               # Captura o índice do item selecionado
    resultado.delete(indice)                          # Remove o item da Listbox
    mensagem.config(text="Produto excluído com sucesso!", fg="green") """

""" import tkinter as tk
from tkinter import messagebox

# Função para salvar o produto
def salvar_produto():
    produto = entry_produto.get()
    quantidade = entry_quantidade.get()
    preco = entry_preco.get()

    # Limpa a mensagem anterior
    mensagem.config(text="")

    if not produto or not quantidade or not preco:
        mensagem.config(text="Preencha todos os campos!", fg="red")
        return

    try:
        quantidade = int(quantidade)
        preco = float(preco)
    except ValueError:
        mensagem.config(text="Quantidade deve ser um número inteiro e preço um número decimal.", fg="red")
        return

    resultado.insert(tk.END, f"{produto} - {quantidade} unidades - R$ {preco:.2f}")
    
    # Limpa os campos
    entry_produto.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    mensagem.config(text="Produto cadastrado com sucesso!", fg="green")

# Função para excluir o produto selecionado
def excluir_produto():
    selecao = resultado.curselection()
    if not selecao:
        mensagem.config(text="Selecione um produto para excluir.", fg="red")
        return
    indice = selecao[0]
    resultado.delete(indice)
    mensagem.config(text="Produto excluído com sucesso!", fg="green")

# Interface principal
janela = tk.Tk()
janela.title("Cadastro de Produto")
janela.geometry("400x450")

# Campos
tk.Label(janela, text="produto do Produto:").pack(pady=5)
entry_produto = tk.Entry(janela, width=30)
entry_produto.pack()

tk.Label(janela, text="Quantidade:").pack(pady=5)
entry_quantidade = tk.Entry(janela, width=30)
entry_quantidade.pack()

tk.Label(janela, text="Preço (R$):").pack(pady=5)
entry_preco = tk.Entry(janela, width=30)
entry_preco.pack()

# Label para mensagens
mensagem = tk.Label(janela, text="", fg="red")
mensagem.pack(pady=5)

# Botões de salvar e excluir
tk.Button(janela, text="Salvar Produto", command=salvar_produto).pack(pady=5)
tk.Button(janela, text="Excluir Produto", command=excluir_produto).pack(pady=5)

# Lista de produtos cadastrados
tk.Label(janela, text="Produtos Cadastrados:").pack(pady=5)
resultado = tk.Listbox(janela, width=50, height=10)
resultado.pack()

# Executa a janela
janela.mainloop() """
import tkinter as tk
def cadastrar_produtos():
    produto = entry_produto.get()
    quantidade = entry_quantidade.get()
    preco = entry_preco.get()
    
    message.config(text='')
    
    if not produto or not quantidade or not preco: 
        message.config(text='Um ou mais campos não estão preenchidos.', fg='red')
        return
    try:
        quantidade = int(quantidade)
        preco = float(preco)
    except ValueError:
        message.config(text='A quantidade = interiro e preco = decimal.', fg='red')
        return
    
    resultado.insert(tk.END, f'produto {produto} - Quantidade{quantidade} unidades - Preço (R$){preco:.2f}')

    entry_produto.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    message.config(text='Produto cadastrado!', fg='green')

def excluir_produto():
    produto_selecionado = resultado.curselection()
    if not produto_selecionado:
        message.config(text='Selecione o produto para excluir.', fg='red')
        return
    indice = produto_selecionado[0]
    resultado.delete(indice)
    message.config(text='Produto excluído com sucesso!')

janela = tk.Tk()
janela.title('Exclusão de produtos')
janela.geometry('500x500')

tk.Label(janela, text='Produto: ').pack(pady=10)
entry_produto = tk.Entry(janela)
entry_produto.pack(pady=10)

tk.Label(janela, text='Quantidade: ').pack(pady=10)
entry_quantidade = tk.Entry(janela)
entry_quantidade.pack(pady=10)

tk.Label(janela, text='Preço: ').pack(pady=10)
entry_preco = tk.Entry(janela)
entry_preco.pack(pady=10)

message = tk.Label(janela, text='', fg='red')
message.pack(pady=10)

tk.Button(janela, text='Cadastrar produto', command=cadastrar_produtos).pack(pady=10)
tk.Button(janela, text='Excluir produto', command=excluir_produto).pack(pady=10)

tk.Label(janela, text='Lista de produtos cadastrados: ').pack(pady=10)
resultado = tk.Listbox(janela, width=60, height=60)
resultado.pack(pady=10)

janela.mainloop()
