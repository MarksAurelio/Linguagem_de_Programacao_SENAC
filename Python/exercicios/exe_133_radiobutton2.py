""" Crie uma janela com a pergunta:

"Qual sabor de pizza você deseja?"

As opções são:
Calabresa
Frango com Catupiry
Mussarela
Portuguesa
Banana com Canela
Sensação

Ao clicar no botão "Confirmar Pedido", deve ser exibida a escolha do usuário. """
import tkinter as tk
def qual_sabor():
    resposta = opcoes.get()
    if resposta and resposta != ' ':
        resultado.config(text=f'Você escolheu: {resposta}')
    else:
        resultado.config(text='Você não escolheu nenhuma opção.', fg='red')

janela = tk.Tk()
janela.title('Sabor Pizza')
janela.geometry('300x300')

opcoes = tk.StringVar(value=' ')

tk.Label(janela, text='Escolha uma opção: ').pack(pady=10)

tk.Radiobutton(janela, text='Calabresa', variable=opcoes, value='Calabresa', ).pack()
tk.Radiobutton(janela, text='Frango com Catupiry', variable=opcoes, value='Frango com Catupiry').pack()
tk.Radiobutton(janela, text='Mussarela', variable=opcoes, value='Mussarela').pack()
tk.Radiobutton(janela, text='Portuguesa', variable=opcoes, value='Portuguesa').pack()
tk.Radiobutton(janela, text='Banana com Canela', variable=opcoes, value='Banana com Canela').pack()
tk.Radiobutton(janela, text='Sensação', variable=opcoes, value='Sensação').pack()

tk.Button(janela, text='Confirmar Pedido', command=qual_sabor).pack(pady=10)

resultado = tk.Label(janela, text='')
resultado.pack(pady=10)

janela.mainloop()
