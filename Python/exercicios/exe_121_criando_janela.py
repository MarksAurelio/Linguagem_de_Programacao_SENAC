# Importando a biblioteca tkinter
# Usamos 'as tk' para abreviar o nome na hora de usar
import tkinter as tk

# Criando a janela principal
janela = tk.Tk()  # Tk() é a função que cria a janela principal

# Definindo um título para a janela
janela.title("Minha Primeira Janela")

# Definindo o tamanho da janela (largura x altura)
janela.geometry("400x300")

# Iniciando o loop principal da aplicação
janela.mainloop()  # Isso mantém a janela aberta

""" 
.import tkinter as tk # Importa a biblioteca com um apelido mais curto
.tk.Tk() # Cria a janela principal
.title() # Define o título da janela
.geometry() # Define o tamanho (400 pixels de largura, 300 de altura)
.mainloop() # Mantém a janela aberta e responde a eventos """

# Atividade 01:
# Modifique o tamanho da janela para 600x400.import tkinter as tk

janela1 = tk.Tk()
janela1.title("Minha Segunda Janela")
janela1.geometry("600x400")
janela1.mainloop()
