""" Utilizando if e else em Python:
if condição:
    # Código a ser executado se a condição for verdadeira
else:
    # Código a ser executado se a condição for falsa
Em Python, a indentação é fundamental para definir o bloco de código dentro das estruturas de controle. 
O código dentro do bloco if e else deve ser indentado para indicar que ele está condicionado àquela estrutura.
Os operadores de comparação (==, !=, <, >, <=, >=) são usados para comparar valores. 
Eles retornam True se a comparação for verdadeira e False caso contrário.
Você pode usar operadores lógicos (and, or, not) para combinar múltiplas condições em uma única instrução if. """

""" Escreva um programa que solicite ao usuário para inserir dois números inteiros. 
O programa deve então verificar qual número é maior e imprimir uma mensagem correspondente. """
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
if numero_1 > numero_2:
    print(f'O primeiro número: {numero_1} é maior que o segundo número: {numero_2}')
else: 
    print(f'O segundo número: {numero_2} é maior que o primeiro número: {numero_1}')
