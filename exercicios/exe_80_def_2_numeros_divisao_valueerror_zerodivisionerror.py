""" Crie um programa que receba dois números e faça a divisão dos dois, e crie uma mensagem de erro da
divisão por zero ou se o usuário informar algo diferente de números. 
try:

except ZeroDivisionError:

except ValueError:"""
while True:
    try:
        numero_1 = int(input('Digite o dividendo: '))
        numero_2 = int(input('Digite o divisor: '))
        print('O resultado da divisão é:', numero_1/numero_2)
    except ValueError:
        print('Opçaõ inválida.')
    except ZeroDivisionError:
        print('Divisão por zero (favor digitar outro número).')
