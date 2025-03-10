""" Crie uma classe chamada Restaurante que armazena um cardápio de pratos. A classe deve ter os seguintes métodos:
adicionar_prato(prato): adiciona um prato ao cardápio.
listar_cardapio(): exibe todos os pratos disponíveis. """
class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.lista = []

    def adicionar_prato(self, prato):
        self.lista.append(prato)

    def listar_cardapio(self):
        print(f'Cardápio do {self.nome}:')
        for prato in self.lista:
            print(f'- {prato}')

restaurante = Restaurante('Meu Restaurante')

while True:
    prato = input('Digite um prato (ou sair para finalizar): ')
    if prato.lower() == 'sair':
        break
    
    restaurante.adicionar_prato(prato)

restaurante.listar_cardapio()
