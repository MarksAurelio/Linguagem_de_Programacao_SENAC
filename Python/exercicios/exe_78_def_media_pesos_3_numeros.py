""" Escreva um programa que calcula a média ponderada de três números fornecidos pelo usuário, 
onde os pesos são fornecidos pelo usuário também. """
def media_ponderada ():
    return ((a*p1) + (b*p2) + (c*p3)) / (p1 + p2 + p3)

a = float(input('Digite a 1° nota: '))
p1 = int(input('Digite o 1° peso: '))

b = float(input('Digite a 2° nota: '))
p2 = int(input('Digite o 2° peso: '))

c = float(input('Digite a 3° nota: '))
p3 = int(input('Digite o 3° peso: '))

print('A média das notas ponderadas é:', media_ponderada())
