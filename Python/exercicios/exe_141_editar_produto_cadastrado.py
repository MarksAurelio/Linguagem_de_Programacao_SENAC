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

    resultado.insert(tk.END, f"{nome} - {quantidade} units - R$ {preco:.2f}")
    
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
    result.delete(indice)
    clear_fields()
    message.config(text='Product deleted successfully!', fg='green')
    indice_selected = None
def load_data(event):
    global indice_selected
    selected_product = result.curselection()
    if selected_product:
        indice_selected = selected_product[0]
        product = result.get(indice_selected)
        try: 
            product, rest = product.split(' - ', 1)
            quantity_str, price_str = rest.split(" units - $ ")
        except ValueError:
            message.config(text='Invalid product format.', fg='red')
            return
        entry_product.delete(0, tk.END)
        entry_product.insert(0, product)
        entry_quantity.delete(0, tk.END)
        entry_quantity.insert(0, quantity_str)
        entry_price.delete(0, tk.END)
        entry_price.insert(0, price_str)
def update_product():
    global indice_selected
    if indice_selected is None:
        message.config(text='Select a product to upgrade.', fg='red')
        return
    
    product = entry_product.get()
    quantity = entry_quantity.get()
    price = entry_price.get()

    message.config(text='')

    if not product or not quantity or not price:
        message.config(text='Fill in all fields!', fg='red')

    try:
        quantity = int(quantity)
        price = float(price)
    except ValueError:
        message.config(text='Quantity must be a whole number and price must be a decimal number.', fg="red")
        return
    
    formatted_product = f'{product} - {quantity} units - R$ {price:.2f}'
    # update item in Listbox
    result.delete(indice_selected)
    result.insert(indice_selected, formatted_product)
    clear_fields()
    message.config(text='Product updated successfully!', fg="green")
    indice_selected = None

def clear_fields():
    entry_product.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)

window = tk.Tk()
window.title('Product Registration')
window.geometry("450x550")

tk.Label(window, text='Product name:').pack(pady=5)
entry_product = tk.Entry(window, width=30)
entry_product.pack()

tk.Label(window, text='Quantity:').pack(pady=5)
entry_quantity = tk.Entry(window, width=30)
entry_quantity.pack()

tk.Label(window, text='Price ($):').pack(pady=5)
entry_price = tk.Entry(window, width=30)
entry_price.pack()

message = tk.Label(window, text="", fg="red")
message.pack(pady=5)

tk.Button(window, text='Save product', command=save_product).pack(pady=5)
tk.Button(window, text='Delete product', command=delete_product).pack(pady=5)
tk.Button(window, text='Update product', command=update_product).pack(pady=5)

tk.Label(window, text='Registered Products:').pack(pady=5)
result = tk.Listbox(window, width=50, height=10)
result.pack(pady=5)
result.bind('<<ListboxSelect>>', load_data)

window.mainloop()
