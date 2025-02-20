""" Escreva um programa que solicite ao usuário um número e depois imprima todos os números pares de 1 até esse número, 
imprimir em ordem decrescente, usando um loop while. """
numero = int(input('Digite um número: '))
while numero >= 2: # Números pares menores que 2 são apenas o 0
    print(numero)
    numero = numero - 2
if numero %2 != 0:
    numero = numero - 1
    print(numero)
    