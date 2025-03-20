""" Escreva um programa que solicite ao usuário um número 
e depois imprima todos os números pares de 1 até esse número, usando um loop while """
numero = int(input('Digite um número: '))
count = 1
while count <= numero:
    if count %2 == 0:
        print(count)
    count = count + 1
