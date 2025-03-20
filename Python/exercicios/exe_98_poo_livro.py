""" Crie uma classe Livro com titulo, autor e estoque. Adicione um método vender(qtd) que reduz o estoque e impede valores negativos """
class Livro:
    def __init__(self, titulo, autor, estoque=0):
        self.titulo = titulo
        self.auto = autor
        self.estoque = estoque

    def vender(self, quantidade):
        if self.estoque > quantidade:
            self.estoque = self.estoque - quantidade
            print(f'A quantidade de livros no estoque é {self.estoque}.')
        else:
            print('Estoque suficiente para a venda.')

livro1 = Livro('A amora', 'Marks', 10)
        
quantidade = int(input('Digite a quantidade: '))       
livro1.vender(quantidade)
