""" Escreva um programa que solicite ao usuário que insira uma senha correta 
e continue pedindo até que a senha correta seja inserida, usando um loop while. """
senha = int(input('Digite a senha: \n'))

if senha == 1234:
    print('Senha correta!')
else:
    print('Senha incorreta!')

# ou

senha_correta = 1234
senha_digitada = "" 

while senha_correta != senha_digitada:
    senha_digitada = int(input('Digite a senha: \n'))

if senha_correta  != senha_digitada:
    print('Senha incorreta!')
else:
    print('Senha correta!')
