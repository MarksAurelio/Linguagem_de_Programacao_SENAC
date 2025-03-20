""" Escreva um programa que leia uma lista de números e imprima apenas aqueles que são (números que podem ser lidos da mesma forma da esquerda 
para a direita e vice-versa). """
while True:
    def numero_palindromo():
        try:
            numeros = input('Digite uma sequência de números (separados por espaço): ').split()
            lista = [i for i in numeros if str(i) == str(i[::-1])]
            print(lista)
            return lista
        except ValueError:
            print('Opção inválida.')
            return 0
        
    print(f'A lista de números que são palíndromos são: {numero_palindromo()}')
    