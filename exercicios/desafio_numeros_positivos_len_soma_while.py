""" Escreva um programa que solicita ao usuário um número inteiro positivo e calcula 
a soma dos seus dígitos.
exemplo:
Número informado: 110
1  + 1 + 0 = 2


len(): Retorna o comprimento (número de elementos) de um objeto, como uma string, lista ou tupla. """
soma = 0
cont = 0
numero = input('Digite um número: ')
while cont < len(numero):
    soma = soma + int(numero[cont])
    cont = cont + 1
print(soma)
