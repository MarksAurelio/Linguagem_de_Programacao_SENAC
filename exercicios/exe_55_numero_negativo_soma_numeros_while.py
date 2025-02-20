""" Crie um programa que peça ao usuário para digitar números até que ele digite um número negativo.
Em seguida, imprima a soma dos números digitados. """
soma = 0
numero = 1
while True:
    numero = int(input('Digite um número: \n'))
    if numero > 0:
        soma = soma + numero
    if numero < 0:
        print('Número negativo digitado. A soma dos números acumulados é:', soma)
        break
    