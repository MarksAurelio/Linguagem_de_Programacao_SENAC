""" Escreva um programa em Python que determine se os números digitados pelo usuário contém somente números, 
caso contenha algum valor não numérico, 
informar que é permitido somente números 
numeros.isdigit()
verificar se todos os caracteres na frase são dígitos de (0 a 9). Se todos os caracteres forem dígitos, 
a função retorna True, caso contrário, retorna False. """
numeros = input('Digite uma sequência de números: ')
if numeros.isdigit():
    print(f'A sequência de números "{numeros}" só possui números.')
else:
    print(f'A sequência "{numeros}" não possui só números, digite somente números.')
