""" Criar um dicionário para armazenar as notas de um aluno e calcular a média. """
dicionario = {}

nome = input('Digite o nome do aluno: ')
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))
nota_4 = float(input('Digite a quarta nota: '))

dicionario ['Nome:'] = nome
dicionario ['Primeira nota:'] = nota_1
dicionario ['Segunda nota:'] = nota_2
dicionario ['Terceira nota:'] = nota_3
dicionario ['Quarta nota'] = nota_4

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(dicionario)
print(f'A média de notas do {nome} é: {media}')
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
