""" Crie uma classe Cliente com nome e historico_compras. Adicione um método adicionar_compra(valor) que adiciona uma compra ao histórico. """
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.historico_compras = []

    def adicionar_compra(self, valor):
        self.historico_compras.append(valor)

compra1 = Cliente('Marks')
compra1.adicionar_compra(1)
compra1.adicionar_compra(2)

print(f'O histórico de compras do cliente {compra1.nome} é: {compra1.historico_compras}.')
