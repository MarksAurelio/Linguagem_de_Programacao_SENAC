""" Implemente um programa que imprima o fatorial do número informado pelo usuário. """
numero = int(input('Digite um número: '))
fatorial = 0
cont = 1
while numero >= cont:
    fatorial = fatorial + cont
    cont = cont + 1
print(fatorial)
