""" Escreva um programa que verifique se uma palavra está toda em letras maiúsculas """
palavra = input('Digite uma palavra: ')
# palavra.isupper()
if palavra == palavra.upper():
    print(f'A palavra {palavra} está toda em letras maiúsculas.')
else:
    print(f'A palavra {palavra} não está toda em letras maiúsculas.')
