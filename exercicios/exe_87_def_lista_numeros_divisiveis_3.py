""" Escreva um programa que leia uma lista de números e imprima apenas aqueles que são divisíveis por 3. """
while True:
    def numero_divisivel_3():
        try:
            numeros = input('Digite uma sequência de números (separados por espaço): ').split()
            lista = [int(i) for i in numeros if int(i) %3 == 0 and int(i) > 0]
            print(lista)
            return lista
        except ValueError:
            return 0
        
    print(f'A lista de números divisíveis por 3 são: {numero_divisivel_3()}')
