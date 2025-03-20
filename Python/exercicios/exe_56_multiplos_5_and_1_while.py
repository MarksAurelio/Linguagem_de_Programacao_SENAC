""" Escreva um programa que imprima os múltiplos de 5 de 1 até o número informado pelo usuário. """,
numero = int(input('Digite um número: '))
i = 1
while i <= numero:
    if i % 5 == 0:
        print(i)
    i = i + 1

# e também 
numero = int(input('Digite um número: '))
while True:
    if numero % 5 == 0:
        print('O número é múltiplo de 5.')
    else:
        print('O número não é múltiplo de 5.')
    break