""" Crie uma interface gráfica usando a biblioteca Tkinter que simule uma tela de login simples. A interface deve conter dois campos de entrada: um para o nome de usuário e outro para a senha (com caracteres ocultos).

Ao clicar no botão "Entrar", o sistema deve verificar se o nome de usuário é "admin" e a senha é "1234".
Se os dados estiverem corretos, exiba a mensagem "Login bem-sucedido!" em verde.
Caso contrário, mostre "Usuário ou senha incorretos." em vermelho.
Utilize Label, Entry, Button e config() para alterar dinamicamente o texto e a cor da mensagem exibida.

Informações adicionais:
A senha deve ser digitada com os caracteres ocultos (utilize o parâmetro show="*" no Entry da senha):
exemplo: entry_senha = tk.Entry(janela, show="*")
Use o método .config(fg="cor") para definir a cor do texto do Label de resposta:
Exemplo: label_resultado.config(text="Mensagem", fg="green") """
import tkinter as tk
def login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if usuario == 'admin' and senha == '1234':
        resultado.config(text='Login bem-sucedido!', fg='green')
    else: 
        resultado.config(text='Usuário ou senha incorretos.', fg='red')

janela = tk.Tk()
janela.title('Janela Login')
janela.geometry('200x300')

caixa_usuario = tk.Label(janela, text='Digite o Usuário: ')
caixa_usuario.pack(pady=10)

entrada_usuario = tk.Entry(janela)
entrada_usuario.pack(pady=10)

caixa_senha = tk.Label(janela, text='Digite a senha: ')
caixa_senha.pack(pady=10)

entrada_senha = tk.Entry(janela, show='*')
entrada_senha.pack(pady=10)

botao = tk.Button(janela, text='Clique aqui', command=login)
botao.pack(pady=10)

resultado = tk.Label(janela, text='')
resultado.pack(pady=10)

janela.mainloop()
