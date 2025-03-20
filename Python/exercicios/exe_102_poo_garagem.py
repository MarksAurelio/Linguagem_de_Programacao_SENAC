""" Crie uma classe chamada Garagem que armazena uma lista de carros. A classe deve ter os seguintes métodos:
adicionar_carro(modelo): adiciona um carro à lista.
listar_carros(): exibe todos os carros armazenados """
class Garagem:
    def __init__(self, nome):
        self.nome = nome
        self.lista = []

    def adicionar_carro(self, carro):
        self.lista.append(carro)

    def listar_carros(self):
        print(f'Lista de carros da {self.nome}:')
        for carro in self.lista:
            print(f'- {carro}')

garagem = Garagem('Minha Garagem')

while True:
    carro = input('Digite um carro (ou sair para finalizar): ')
    if carro.lower() == 'sair':
        break
    garagem.adicionar_carro(carro)

garagem.listar_carros()
