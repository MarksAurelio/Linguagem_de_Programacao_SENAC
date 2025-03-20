""" Objetivo: Criar um dicionário para armazenar informações de um produto e exibi-las depois.

O que é um Dicionário em Python?
Um dicionário (dict) em Python é uma estrutura de dados que armazena pares de chave: valor. Ele é mutável, ou seja, pode ser modificado após sua criação.

Os dicionários são úteis quando precisamos armazenar e acessar dados de forma rápida, associando chaves únicas a valores correspondentes.

# Criando um dicionário vazio
meu_dicionario = {}

# Criando um dicionário com informações de um carro
carro = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2022,
    "cor": "Prata"
}

# Exibindo o dicionário completo
print("Informações do carro:")
print(carro)

# Acessando valores individuais
print("\n Marca do carro:", carro["marca"])
print(" Modelo do carro:", carro["modelo"])

# Modificando um valor (alterando o ano do carro)
carro["ano"] = 2023
print("\n Ano atualizado:", carro["ano"])

# Adicionando um novo atributo (adicionando o preço)
carro["preco"] = 120000
print("\n Adicionando o preço do carro:", carro["preco"])

# Removendo um atributo (removendo a cor)
del carro["cor"]
print("\n Removendo a cor do carro.")

# Exibindo todas as chaves, valores e pares chave-valor
print("\n Todas as chaves do dicionário:", carro.keys())
print(" Todos os valores do dicionário:", carro.values())
print(" Todos os itens do dicionário:", carro.items())

# Exibindo o dicionário final
print("\n Dicionário atualizado:")
print(carro)

Explicação:

As chaves são únicas e podem ser do tipo string, int, float, bool ou tuple.
Os valores podem ser de qualquer tipo (int, float, string, list, dict, etc.).
As chaves e os valores são separados por dois pontos :.
Os pares chave: valor são separados por vírgulas ,.

Exercício resolvido:
produto = {}

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade em estoque: "))

produto["Nome"] = nome
produto["Preço"] = preco
produto["Quantidade"] = quantidade

print("\nInformações do Produto:")
print(produto) """

dicionario = {}

nome = input('Digite o nome de um produto: ')
preco = float(input('Digite o preço do produto: '))
quantidade = int(input('Digite a quantidade em estoque: '))

dicionario['Nome'] = nome
dicionario['Preço'] = preco
dicionario['Quantidade'] = quantidade

print('\n Informações do Produto: ')
print(dicionario)
