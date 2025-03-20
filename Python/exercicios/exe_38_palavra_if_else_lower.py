""" Escreva um programa que verifique se uma palavra está toda em letras minúsculas. """
palavra = input('Digite um palavra: ')
if palavra == palavra.lower():
    print(f'A palavra {palavra} está toda em letras minúsculas.')
else:
    print(f'A palavra {palavra} não está em letras minúsculas.')
