""" O objetivo desta atividade é criar uma interface gráfica que permita ao usuário cadastrar produtos, fornecendo o nome, a quantidade e o preço de cada item. O sistema deve validar os dados inseridos, garantindo que todos os campos sejam preenchidos corretamente antes de salvar as informações. """
import tkinter as tk
def cadastrar_produtos():
    produto = entrada_produto.get()
    quantidade = entrada_quantidade.get()
    preco = entrada_preco.get()
    if produto:
        resultado.insert(tk.END, f'Produto: {produto}, Quantidade: {quantidade}, Produto: {preco}')
        entrada_produto.delete(0, tk.END)
        entrada_quantidade.delete(0, tk.END)
        entrada_preco.delete(0, tk.END)
        aviso.config(text='')
    else:
        aviso.config(text='Digite um produto.', fg='red')

janela = tk.Tk()
janela.title('Cadastro de produtos')
janela.geometry('500x500')

tk.Label(janela, text='Digite um produto: ').pack(pady=10)
entrada_produto = tk.Entry(janela)
entrada_produto.pack(pady=10)

tk.Label(janela, text='Quantidade: ').pack(pady=10)
entrada_quantidade = tk.Entry(janela)
entrada_quantidade.pack(pady=10)

tk.Label(janela, text='Preço (R$): ').pack(pady=10)
entrada_preco = tk.Entry(janela)
entrada_preco.pack(pady=10)

aviso = tk.Label(janela, text='', fg='red')
aviso.pack(pady=10)

tk.Button(janela, text='Cadastrar produto', command=cadastrar_produtos, fg='green').pack(pady=10)

tk.Label(janela, text='Lista de produtos: ').pack(pady=10)
resultado = tk.Listbox(janela, width=60, height=60)
resultado.pack(pady=10)

janela.mainloop()
