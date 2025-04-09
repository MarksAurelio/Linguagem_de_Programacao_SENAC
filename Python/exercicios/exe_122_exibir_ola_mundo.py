import tkinter as tk

def dizer_ola():
    # Criando um rótulo (label) para exibir o texto
    label_ola = tk.Label(janela, text="Olá, Mundo!")
    label_ola.pack()

janela = tk.Tk()
janela.title("Olá Mundo na Janela")

botao = tk.Button(janela, text="Clique aqui", command=dizer_ola)
botao.pack()

janela.mainloop()

# Atividade:
# Personalizar uma mensagem ao clicar em dizer_ola_mundo

def ola_mundo():
    label_ola_mundo = tk.Label(janela1, text='Olá Mundo')
    label_ola_mundo.pack()

janela1 = tk.Tk()
janela1.title('Olá Mundo na Janela1')

botao1 = tk.Button(janela1, text='Clique aqui', command=ola_mundo)
botao1.pack()

janela1.mainloop()
