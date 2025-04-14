""" Crie um programa que permita ao usuário digitar tarefas do dia. Cada tarefa será listada em uma caixa. Mostre uma mensagem se a pessoa tentar adicionar sem escrever nada. """
import tkinter as tk
def lista_de_tarefas():
    tarefa = entrada.get()
    if tarefa:
        resultado.insert(tk.END, tarefa)
        entrada.delete(0, tk.END)
        aviso.config(text='')
    else:
        aviso.config(text='Digite uma tarefa: ', fg='red')

janela = tk.Tk()
janela.title('Lista de tarefas')

tk.Label(janela, text='Digite uma tarefa: ').pack(pady=10)

entrada = tk.Entry(janela, width=50)
entrada.pack()

aviso = tk.Label(janela, text='', fg='red')
aviso.pack()

tk.Button(janela, text='Clique aqui', command=lista_de_tarefas).pack(pady=10)

tk.Label(janela, text='Lista de tarefas cadastrados: ').pack(pady=10)

resultado = tk.Listbox(janela, width=40, height=10)
resultado.pack(pady=10)

janela.mainloop()
