""" Escreva um programa em Python que receba uma lista de palavras separadas por espaço 
e determine quantas palavras têm mais de 5 letras. """
while True:
    def palavra_mais_5_letras():
        try:
            palavras = input('Digite uma sequência de palavras (separados por espaço): ').split()
            lista = [i for i in palavras if len(i) > 5]
            print(lista)
            return lista
        except ValueError:
            print('Opção inválida.')
            return 0
    print(f'A lista de palavras digitadas têm mais de 5 letras: {palavra_mais_5_letras()}')
