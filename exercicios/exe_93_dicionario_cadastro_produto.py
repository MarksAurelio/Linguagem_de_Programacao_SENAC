""" Crie um programa que cadastre um produto em um dicionário, incluindo nome, preço e quantidade. Em seguida, adicione a marca do produto, remova a chave "quantidade" e exiba o dicionário atualizado. """
dicionario = {}

nome = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: '))
quantidade = int(input('Digite a quantidade em estoque do produto: '))

dicionario['Nome produto: '] = nome
dicionario['Preço produto: '] = preco
dicionario['Quantidade estoque: '] = quantidade

print(dicionario)

print('\nAdicionando marca do produto')

marca = input('Digite a marca do produto: ')
dicionario['Marca produto: '] = marca

print(dicionario)

print('\nRemovendo a chave "Quantidade"')

print(dicionario)

del dicionario['Quantidade estoque: ']

print(dicionario)
