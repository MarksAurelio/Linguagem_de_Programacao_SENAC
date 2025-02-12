""" Escreva um programa em Python que use o parâmetro sep na função print() para imprimir o nome, idade 
e altura de uma pessoa separados por um hífen. """
nome = str(input('Digite um nome de uma pessoa: '))
idade = int(input('Digite a idade dessa pessoa: '))
altura = float(input('Digite a altura dessa pessoa: '))
print(nome, idade, altura, sep='-')
