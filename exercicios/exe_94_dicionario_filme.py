""" Crie um dicionário representando um filme , contendo Título, Ano e Gênero. Depois, adicione a duração  e remova o campo "ano". """
dicionario = {}

titulo = input('Digite o título do filme: ')
ano = int(input('Digite o ano (no formato 0000): '))
genero = input(('Digite o gênero do filme: '))

dicionario['Título:'] = titulo
dicionario['Ano:'] = ano
dicionario['Gênero:']= genero

print(dicionario)

print('\nAdicionando a chave "Duração"')
duracao = input('Digite a duração do filme: ')
dicionario['Duração'] = duracao

print(dicionario)

print('\nRemovendo a chave "Ano"')
del dicionario['Ano:']

print(dicionario)
