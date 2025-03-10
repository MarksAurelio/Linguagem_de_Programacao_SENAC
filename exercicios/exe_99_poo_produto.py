""" Crie uma classe Produto com nome e estoque. Adicione um método repor_estoque(quantidade) que aumenta o estoque """
class Produto:
    def __init__(self, nome, estoque):
        self.nome = nome
        self.estoque = estoque

    def repor_estoque(self, quantidade):
        if self.estoque > 1:
            self.estoque = self.estoque + quantidade
            print(f'A quantidade de produtos no estoque é: {self.estoque}')

produto1 = Produto('Carrinho', 10)

quantidade = int(input('Digite a quantidade: '))
produto1.repor_estoque(quantidade)
