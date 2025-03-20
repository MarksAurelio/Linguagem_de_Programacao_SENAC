""" Criar um dicionário com palavras em inglês e suas traduções para português e permitir que o usuário consulte uma palavra. """
while True:
    dicionario = {'Dog': 'Cachorro', 'Cat': 'Gato', 'Fish': 'Peixe'}

    palavra = input('Digite uma palavra: ').capitalize().strip()

    if palavra in dicionario:
        print(f'A palavra {palavra} tem a tradução {dicionario[palavra]}.')
    else:
        print('Palavra não localizada.')
