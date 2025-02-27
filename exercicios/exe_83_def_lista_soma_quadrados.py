""" Escreva um programa em Python que receba uma lista de números inteiros separados por espaço e determine 
a soma dos quadrados dos números na lista.

nova_lista[expressão for variável in sequencia]
Quando a condição for verdadeira, ele interage sobre a expressão. """
while True:
    def soma_quadrados():
        try:
            numeros = input('Digite uma sequência de números (separados por espaço): ').split()
            lista = [int(i)**2 for i in numeros]
            print(lista)
            return sum(lista)
        except ValueError:
            print('Valor inválido.')
            return 0
    print(f'A soma dos quadrados dos números da lista é: {soma_quadrados()}')
