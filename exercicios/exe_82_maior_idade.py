""" Crie um programa que verifique se uma pessoa é maior de idade.
Situação: Este programa precisa lidar com a entrada de valores não inteiros ou negativos. """
while True:
    try:
        idade = float(input('Digite a idade: '))
        if idade >= 18:
            print('Maior de idade.')
        else:
            print('Menor de idade.')
    except ValueError:
        print('Valor inválido.')
        