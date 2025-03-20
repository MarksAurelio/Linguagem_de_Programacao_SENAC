""" Escreva um programa em Python que receba uma lista de números inteiros separados por espaço 
e determine quantos números são divisíveis por 3 e 5 simultaneamente """
while True:
    def divisor_3_5():
        try:
            numeros = input('Digite uma sequência de números (separados por espaço): ').split()
            lista = [int(i) for i in numeros if int(i) % 5 == 0 and int(i) % 3 == 0 and int(i) > 0]
            print(lista)
            return len(lista)
        except ValueError:
            print('Opção inválida.')
            return 0
    print(f'O números da lista que são divisíveis por 3 e 5 são: {divisor_3_5()}')
