""" Faça um programa que transforme um texto todo em letras maiúsculas 
e conte quantas letras 'A' ele possui. """
texto = input('Digite uma frase: ').upper()
quantidade_A = texto.count('A')
print(f'O texto {texto} contém {quantidade_A} letra(s) A')

# ou

texto = input('Digite uma frase: ').upper()
quantidade_A = texto.count('A')
print(texto)
if quantidade_A > 0:
    print(f'A quantidade de letra(s) A é: {quantidade_A}')
else: 
    print("O texto não contém letras 'A'")
