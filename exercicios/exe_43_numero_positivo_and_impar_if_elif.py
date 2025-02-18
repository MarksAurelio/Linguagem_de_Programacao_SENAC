""" Escreva um programa em Python que determine se um número digitado pelo usuário é um número positivo 
e ímpar. """
numero = int(input('Digite um número: '))
if numero > 0 and numero %2 == 1:
    print(f'O número {numero} é positivo e ímpar.')
elif numero > 0 and numero %2 == 0:
    print(f'O número {numero} é positivo e par.')
elif numero < 0 and numero %2 == 1:
    print(f'O número {numero} é negativo e ímpar.')
elif numero < 0 and numero %2 == 0:
    print(f'O número {numero} é negativo e par.')
else:
    print(f'O número {numero} é neutro.')
