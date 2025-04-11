import tkinter as tk

def verificar_resposta():
    resposta = escolha.get()
    if resposta:
        label_resultado.config(text=f"Você escolheu: {resposta}")
    else:
        label_resultado.config(text="Nenhuma opção selecionada.")

# Criar a janela
janela = tk.Tk()
janela.title("Você gostou?")
janela.geometry("250x180")

# Variável do Radiobutton
escolha = tk.StringVar(value="Sim")  # Começa com seleção

# Texto da pergunta
tk.Label(janela, text="Você gostou do exemplo?").pack(pady=10)

# Botões de opção
tk.Radiobutton(janela, text="Sim", variable=escolha, value="Sim").pack()
tk.Radiobutton(janela, text="Não", variable=escolha, value="Não").pack()

# Botão para confirmar a resposta
tk.Button(janela, text="Confirmar", command=verificar_resposta).pack(pady=10)

# Onde será mostrada a resposta
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Rodar a interface
janela.mainloop()

# Atividade:

""" Crie uma interface para o usuário escolher um turno de aula com as opções:
"Manhã", "Tarde", e "Noite". Deixar o turno da manhã marcado por padrão
Ao clicar no botão "Selecionar Turno", mostre qual foi a escolha feita. """
def verificar_resposta1():
    resposta1 = escolha1.get()
    if resposta1:
        resultado1.config(text=f'Você escolheu: {resposta1}')

janela1 = tk.Tk()
janela1.title('Escolha o turno')
janela1.geometry('300x200')

escolha1 = tk.StringVar(value='Manhã') # começa a opção já selecionada

tk.Label(janela1, text='Escolha um turno: ').pack(pady=10)

tk.Radiobutton(janela1, text='Manhã', variable=escolha1, value='Manhã').pack()
tk.Radiobutton(janela1, text='Tarde', variable=escolha1, value='Tarde').pack()
tk.Radiobutton(janela1, text='Noite', variable=escolha1, value='Noite').pack()

tk.Button(janela1, text='Confirmar', command=verificar_resposta1).pack(pady=10)

resultado1= tk.Label(janela1, text='')
resultado1.pack(pady=10)

janela1.mainloop()
