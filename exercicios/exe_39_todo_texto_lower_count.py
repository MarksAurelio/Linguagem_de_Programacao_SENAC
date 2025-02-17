""" Faça um programa que transforme um texto todo em letras minúsculas 
e conte quantas letras 'e' ele possui. """
texto = input('Digite uma frase: ').lower()
contar_letras = texto.count('e')
print(f'O texto "{texto}" digitado têm {contar_letras} letra(s).')
