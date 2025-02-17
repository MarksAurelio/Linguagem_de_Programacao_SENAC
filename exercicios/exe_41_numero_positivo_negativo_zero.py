""" Escreva um programa que solicite ao usuário para inserir um número 
e determine se é positivo, negativo ou zero. """
numero = int(input('Digite um número: '))
if numero < 0:
    print(f'O número {numero} é negativo.')
elif numero > 0:
    print(f'O número {numero} é positivo')
else:
    print(f'O número {numero} é neutro.')
