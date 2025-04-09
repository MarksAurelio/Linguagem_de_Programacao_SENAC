# O usuário digita sua idade. O programa responde se é maior ou menor de idade.
import tkinter as tk
def maior_idade():
    idade = entrada_idade.get()
    idade = int(idade)
    mensagem = ''
    if idade >= 18:
        mensagem = 'Maior de idade'
    else:
        mensagem = 'Menor de idade'
    label_verificar_idade.config(text=mensagem)
    

janela = tk.Tk()
janela.title('Verificador de idade')

caixa_idade = tk.Label(janela, text='Digite sua idade: ')
caixa_idade.pack(pady=10)

entrada_idade = tk.Entry(janela)
entrada_idade.pack(pady=10)

botao_verificar = tk.Button(janela, text='Verificar', command=maior_idade)
botao_verificar.pack(pady=10)

label_verificar_idade = tk.Label(janela)
label_verificar_idade.pack(pady=10)

janela.mainloop()
