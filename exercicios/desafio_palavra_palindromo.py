""" Crie um programa que verifique se um palavra é um palíndromo(Igual, quando lida de trás para frente). """
palavra = input('Digite uma palavra: ')
if palavra == palavra[::-1]:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
    