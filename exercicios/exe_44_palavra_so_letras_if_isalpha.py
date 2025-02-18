""" Escreva um programa em Python que determine se uma palavra digitada pelo usuário somente contém letras, 
caso contenha algum valor numérico, informar que não contem apenas letras ou nenhuma letra. """
palavra = input('Digite um palavra: ')
if palavra.isalpha():
    print(f'A palavra "{palavra}" só possui letras.')
else:
    print(f'A palavra "{palavra}" não possui só letras.')
