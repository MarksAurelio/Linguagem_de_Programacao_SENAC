""" Escreva uma função chamada inverter_string que aceita uma string como argumento e retorna 
a string invertida. """
def inverter_string(string):
    return string[::-1]
palavra = input('Digite uma palavra: ')
print(f'A palavra {palavra} invertida fica: {inverter_string(palavra)}')
