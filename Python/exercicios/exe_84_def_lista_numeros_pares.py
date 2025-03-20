""" Escreva um programa em Python que receba uma lista de números inteiros separados por espaço 
e conte quantos números pares estão presentes na lista.
nova_lista[expressão for variável in sequencia  if condição] """
while True:
    def numeros_pares():
        try:
            numeros = input('Digite uma sequência de números inteiros (separados por espaço): ').split()
            lista = [int(i) for i in numeros if int(i) %2 == 0]
            print(lista)
            return len(lista)
        except ValueError:
            print('Opção inválida.')
            return 0
    print(f'O números pares da lista são: {numeros_pares()}')
