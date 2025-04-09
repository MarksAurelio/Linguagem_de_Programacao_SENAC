import tkinter as tk

def dizer_ola():
    nome = entrada_nome.get()
    mensagem = f"Olá, {nome}!"
    label_ola = tk.Label(janela, text=mensagem)
    label_ola.pack()

janela = tk.Tk()
janela.title("Olá com Nome")
janela.geometry("400x200")  # Largura x Altura da janela

# Campo de entrada
entrada_nome = tk.Entry(janela, font=("Arial", 14))
entrada_nome.pack(pady=10)

# Botão
botao = tk.Button(janela, text="Dizer Olá", command=dizer_ola, font=("Arial", 12))
botao.pack()

janela.mainloop()

# Atividade:
# Entender o código e adicionar uma mensagem personalizada para o usuário.

def dizer_bem_vindo():
    nome1 = entrada_nome1.get()
    mensagem1 = f'Bem vindo, {nome1}'
    label_bem_vindo = tk.Label(janela1, text=mensagem1)
    label_bem_vindo.pack()

janela1 = tk.Tk()
janela1.title('Bem vindo com Nome')
janela1.geometry('400x200')

entrada_nome1 = tk.Entry(janela1, font=('Arial', 15))
entrada_nome1.pack(pady=10)

botao1 = tk.Button (janela1, text='Bem vindo', command=dizer_bem_vindo, font=('Arial', 12))
botao1.pack()

janela1.mainloop()
