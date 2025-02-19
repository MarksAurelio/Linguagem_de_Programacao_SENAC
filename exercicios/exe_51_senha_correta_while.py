""" Escreva um programa que solicite ao usuário que insira uma senha correta 
e continue pedindo até que a senha correta seja inserida, usando um loop while. """
senha = int(input('Digite a senha: \n'))

if senha == 1234:
    print('Senha correta!')
else:
    print('Senha incorreta!')

# ou

senha_cadastrada = str(input('Cadastre uma senha: \n'))
senha_digitada = "" 

while senha_cadastrada != senha_digitada:
    senha_digitada = str(input('Digite a senha: \n'))

if senha_cadastrada  != senha_digitada:
    print('Senha incorreta!')
else:
    print('Senha correta!')
