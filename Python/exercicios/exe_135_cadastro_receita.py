""" Crie um programa que permita ao usuário digitar ingredientes de uma receita e adicioná-los a uma lista. Se o campo estiver vazio, mostre uma mensagem pedindo para digitar algo. """
import tkinter as tk
def adicionar_ingredientes():
    ingrediente = entrada.get()
    if ingrediente:
        resultado.insert(tk.END, ingrediente)
        entrada.delete(0, tk.END)
        aviso.config(text='')
    else:
        aviso.config(text='Digite o ingrediente: ', fg='red')

janela = tk.Tk()
janela.title('Cadastro de Receita')

tk.Label(janela, text='Digite o ingrediente: ').pack(pady=5)

entrada = tk.Entry(janela, width=20)
entrada.pack(pady=5)

aviso = tk.Label(janela, text='', fg='red')
aviso.pack()

tk.Button(janela, text='Clique aqui', fg='green', command=adicionar_ingredientes).pack(pady=5)

tk.Label(janela, text='Ingredientes cadastrados: ').pack(pady=5)
resultado = tk.Listbox(janela, width=30, height=10)
resultado.pack()

janela.mainloop()
