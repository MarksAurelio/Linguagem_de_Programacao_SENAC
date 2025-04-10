# Verificar se a palavra digitada é um palíndromo (mesmo ao contrário)
import tkinter as tk
def palindromo():
    palavra = entrada_palavra.get()
    mensagem = ''
    if palavra == palavra[::-1]:
        mensagem = 'É palíndromo!'
    else:
        mensagem = 'Não é palíndromo!'
    caixa_verificar_palindromo.config(text=mensagem)

janela = tk.Tk()
janela.title('Janela verificar se a palavra é palíndromo')

caixa_palavra = tk.Label(janela, text='Digite a palavra: ')
caixa_palavra.pack(pady=10)

entrada_palavra = tk.Entry(janela)
entrada_palavra.pack(pady=10)

botao_palavra = tk.Button(janela, text='Clique aqui', command=palindromo)
botao_palavra.pack(pady=10)

caixa_verificar_palindromo = tk.Label(janela)
caixa_verificar_palindromo.pack(pady=10)

janela.mainloop()
