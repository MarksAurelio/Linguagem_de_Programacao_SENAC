""" 📘Crie uma janela com um botão e um rótulo. O rótulo deve contar e mostrar quantas vezes o botão foi clicado. """

# 🧭 Instruções:

""" Crie uma variável contador começando com 0.
Toda vez que o botão for clicado, aumente contador em 1.
Atualize o texto do Label com o novo valor.
Use a palavra global dentro da função para indicar que você quer usar a variável de fora da função. """
import tkinter as tk
contador = 0
def contar():    
     global contador  # permite usar a variável "contador" de fora da função    
     contador += 1    # aumenta o valor em 1    
     label_contador.config(text=f"Cliques: {contador}")

# Label mostrando o número de cliques
janela = tk.Tk()
janela.title('Contador de cliques')
label_contador = tk.Label(janela, text="Cliques: 0")
label_contador.pack(pady=10)

botao_contar = tk.Button(janela, text='Clique para contar', command=contar)
botao_contar.pack(pady=10)

janela.mainloop()
