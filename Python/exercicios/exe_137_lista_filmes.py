""" Crie um programa onde o usuário possa digitar nomes de filmes que quer assistir depois. Se tentar adicionar vazio, avise """
import tkinter as tk
def lista_de_filmes():
    filmes = entrada.get()
    if filmes:
        resultado.insert(tk.END, filmes)
        entrada.delete(0, tk.END)
        aviso.config(text='')
    else:
        aviso.config(text='Digite um filme', fg='red')

janela = tk.Tk()
janela.title('Lista de filmes')

tk.Label(janela, text='Digite o filme: ').pack(pady=10)

entrada = tk.Entry(janela, width=40)
entrada.pack(pady=10)

aviso = tk.Label(janela, text='', fg='red')
aviso.pack(pady=10)

tk.Button(janela, text='Clique aqui', command=lista_de_filmes, fg='green').pack(pady=10)

tk.Label(janela, text='Lista de filmes cadastrados: ').pack(pady=10)

resultado = tk.Listbox(janela, height=10, width=40)
resultado.pack(pady=10)

janela.mainloop()
