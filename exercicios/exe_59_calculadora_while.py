""" Calculadora Simples
Enunciado: Escreva um programa que solicite ao usuário dois números 
e uma operação (adição, subtração, multiplicação ou divisão) e realize a operação desejada. """
operador = str(input('Escolha um operador + - * ÷ : '))
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

if operador == '+':
    print(numero_1 + numero_2)
elif operador == '-':
    print(numero_1 - numero_2)
elif operador == 'x':
    print(numero_1 * numero_2)
elif operador == '÷':
    print(numero_1 / numero_2)

# ou

operador = str(input('Escolha um operador + - * /: '))
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2

if operador == '+':
    print(numero_1, '+', numero_2, '=', soma)
elif operador == '-':
    print(numero_1, '-', numero_2, '=', subtracao)
elif operador == '*':
    print(numero_1, '*', numero_2, '=', multiplicacao)
elif operador == '/':
    print(numero_1, '/', numero_2, '=', divisao)
    
# ou
while True:
    operador = str(input('Escolha um operador + - * /: '))
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))

    soma = numero_1 + numero_2
    subtracao = numero_1 - numero_2
    multiplicacao = numero_1 * numero_2
    divisao = numero_1 / numero_2

    if operador == '+':
        print(numero_1, '+', numero_2, '=', soma)
    elif operador == '-':
        print(numero_1, '-', numero_2, '=', subtracao)
    elif operador == '*':
        print(numero_1, '*', numero_2, '=', multiplicacao)
    elif operador == '/':
        print(numero_1, '/', numero_2, '=', divisao)
 