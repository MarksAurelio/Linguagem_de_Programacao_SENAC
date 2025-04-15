""" import tkinter as tk
from tkinter import messagebox

# Função para salvar o produto
def salvar_produto():
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()
    preco = entry_preco.get()

    # Limpa a mensagem anterior
    mensagem.config(text="")

    if not nome or not quantidade or not preco:
        mensagem.config(text="Preencha todos os campos!", fg="red")
        return

    try:
        quantidade = int(quantidade)
        preco = float(preco)
    except ValueError:
        mensagem.config(text="Quantidade deve ser um número inteiro e preço um número decimal.", fg="red")
        return

    resultado.insert(tk.END, f"{nome} - {quantidade} unidades - R$ {preco:.2f}")
    
    # Limpa os campos
    entry_nome.delete(0, tk.END)
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
tk.Label(janela, text="Nome do Produto:").pack(pady=5)
entry_nome = tk.Entry(janela, width=30)
entry_nome.pack()

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
from tkinter import messagebox
indice_selected = None
def save_product():
    product = entry_product.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    message.config(text='')

    if not product or not quantity or not price:
        message.config(text='Please fill in all fields', fg='red')
        return
    
    try:
        quantity = int(quantity)
        price = float(price)
    except ValueError:
        message.config(text='Quantity must be an integer and price, a decimal number.')
        return
    formatted_product = f'Product: {product} - Quantity: {quantity} - Price ($): {price:.2f}'
    result.insert(tk.END, formatted_product)

    message.config(text='Product registered successfully!', fg='green')
def delete_product():
    global indice_selected
    selected_product = result.curselection()
    if not selected_product:
        message.config(text='Select a product to delete.', fg='red')
        return
    indice = selected_product[0]
    result.config(indice)
    clear_fields()
    message.config(text='Product deleted successfully!', fg='green')
    indice_selected = None
def load_data(event):
    global indice_selected
    selected_product = result.curselection()
    if selected_product:
        indice_selected = selected_product[0]
        product_1 = result.get(indice_selected)
        try: 
            product, resto = product_1.split(' unidades - $ ')
        except ValueError:
            message.config(text='Invalid product format.')
            
