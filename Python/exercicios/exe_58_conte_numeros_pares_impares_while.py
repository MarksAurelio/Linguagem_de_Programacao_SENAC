""" Escreva um programa que solicita ao usuário uma sequência de números inteiros positivos 
e conta quantos números pares e quantos números ímpares foram digitados.
O programa deve encerrar, quando for inserido um número negativo. """
numero_digitado = 0
par = 0
impar = 0
while numero_digitado > 0:
    numero_digitado = int(input('Digite um número positivo (negativo para sair): '))
    if numero_digitado < 0:
        break
    if numero_digitado %2 == 0:
        par = par + 1
        print('Os números pares são:', numero_digitado)
    elif numero_digitado %2 == 1:
        impar = impar + 1
        print('Os números ímpares são:', numero_digitado)
