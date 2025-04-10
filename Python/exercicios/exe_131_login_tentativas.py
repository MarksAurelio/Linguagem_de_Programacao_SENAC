""" Crie uma aplicação de login com Tkinter que permita no máximo 3 tentativas de acesso.
A interface deve conter campos para entrada do nome de usuário e senha (ocultando os caracteres digitados).
Quando o botão "Entrar" for pressionado, o programa deve verificar se o nome de usuário é "admin" e a senha é "1234".

Caso os dados estejam corretos, exiba "Login bem-sucedido!" em verde.
Se estiverem incorretos, diminua o número de tentativas restantes e informe ao usuário.
Após 3 tentativas incorretas, desative o botão de login e mostre a mensagem "Conta bloqueada!" em vermelho.

Utilize variáveis globais, condicionais (if), e o método config() para atualizar dinamicamente as informações da interface.

Instruções adicionais:
Para desativar o botão após 3 tentativas:  
botao_login.config(state="disabled") """
import tkinter as tk
contador = 3
def login():
    global contador 
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if usuario == 'admin' and senha == '1234':
        resultado.config(text='Login bem-sucedido!', fg='green')
    else: 
        resultado.config(text=f'Usuário ou senha incorretos. Tentativas restantes: {contador}', fg='red')  
        contador -= 1  
        if contador <= 0:     
            resultado.config(text=f'Conta bloqueada!')
            botao.config(state='disabled')
     
janela = tk.Tk()
janela.title('Janela Login')
janela.geometry('300x300')

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
