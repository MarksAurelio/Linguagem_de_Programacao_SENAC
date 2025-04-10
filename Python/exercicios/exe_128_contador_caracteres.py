# Contar quantos caracteres o usuário digitou em um campo de texto.
import tkinter as tk
def contador_caracteres():
    palavra = entrada_palavra.get()
    numero_caracteres = len(palavra)
    caixa_contar_caracteres.config(text=f'Números de caracteres é: {numero_caracteres}')

janela = tk.Tk()
janela.title('Janela Contador de caracteres')

caixa_palavra = tk.Label(janela, text='Digite a palavra')
caixa_palavra.pack(pady=10)

entrada_palavra = tk.Entry(janela)
entrada_palavra.pack(pady=10)

botao_contar = tk.Button(janela, text='Clique para contar os caracteres', command=contador_caracteres)
botao_contar.pack(pady=10)

caixa_contar_caracteres = tk.Label(janela, text='Números de caracteres é: ')
caixa_contar_caracteres.pack(pady=10)

janela.mainloop()
