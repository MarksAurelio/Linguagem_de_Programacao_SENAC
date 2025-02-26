""" Crie um programa que receba um número inteiro e retorne uma mensagem de erro, 
caso o usuário informe número fracionado ou letra.

Instruções
Em resumo, try permite que você lide com possíveis erros de forma controlada, 
e ValueError é uma categoria específica de erro relacionada a valores inválidos.
try: 

 
except ValueError: """
while True:
    try:
        numero = int(input('Digite um número: '))
        print(f'O número {numero} foi digitado corretamente.')

    except ValueError:
        print('Valor inválido.')
    