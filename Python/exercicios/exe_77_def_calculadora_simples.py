""" Criar um programa que simula uma calculadora básica com operações de adição, subtração, multiplicação 
e divisão. O programa solicitará ao usuário que escolha a operação desejada, 
inserindo um número correspondente, e então pedirá os dois números nos quais a operação será realizada. 
Por fim, mostrará o resultado da operação escolhida """
def calculadora(a, b, operador):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        return a / b
while True:  
    operador = input('Escolha um operador + - * /: ')     
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    
    resultado = calculadora(a, b, operador)
    print(f'O resultado de {a} {operador} {b} = {resultado}')

# ou
    
while True:
    def soma(a, b):
        return a + b
    def subtracao(a, b):
        return a - b
    def multiplicação(a, b):
        return a * b
    def divisão(a, b):
        return a / b


    operador = input('Escolha um operador + - * /: ')
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))

    resultado_soma = soma(a, b)
    resultado_subtracao = subtracao(a, b)
    resultado_multiplicacao = multiplicação(a, b)
    resultado_divisao = divisão(a, b)
    if operador == '+':
        print(f'O resultado de {a} {operador} {b} = {resultado_soma}')
    elif operador == '-':
        print(f'O resultado de {a} {operador} {b} = {resultado_subtracao}')
    elif operador == '*':
        print(f'O resultado de {a} {operador} {b} = {resultado_multiplicacao}')
    elif operador == '/':
        print(f'O resultado de {a} {operador} {b} = {resultado_divisao}')
