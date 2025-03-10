""" Crie uma classe Livraria que armazena uma lista de livros. Adicione métodos para adicionar livros e listar os títulos disponíveis. """
class Livraria:
    def __init__(self, nome):
        self.nome = nome
        self.lista_livros = []

    def adicionar_livro (self, livro):
        self.lista_livros.append(livro)

    def lista_titulos(self):
        print(f'Lista de livros da {self.nome}:')
        for livro in self.lista_livros: 
            print(f'- {livro}')
           
minha_livraria = Livraria('Minha livraria')

while True:
    titulo_livro = input('Digite o título do livro (ou sair para finalizar): ')
    if titulo_livro.lower() == 'sair':
        break
    minha_livraria.adicionar_livro(titulo_livro)

minha_livraria.lista_titulos()
