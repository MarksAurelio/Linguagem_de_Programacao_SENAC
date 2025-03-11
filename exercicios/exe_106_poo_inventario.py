""" Crie uma classe chamada Inventário que armazena um conjunto de produtos em estoque. A classe deve ter os seguintes métodos:
adicionar_produto(nome, quantidade): adiciona um produto ao estoque.
listar_produtos(): exibe todos os produtos armazenados. """
class Inventário:
    def __init__(self, nome):
        self.nome = nome
        self.lista = []

    def adicionar_produto(self, produto):
        self.lista.append(produto)

    def listar_produtos(self):
        print(f'{self.nome}:')
        for produto in self.lista:
            print(f'- Nome: {produto["nome"]}\n- Quantidade: {produto["quantidade"]}')

inventario = Inventário('Meu Inventário')

while True:
    nome = input('Digite um produto (ou sair para finalizar): ').capitalize()
    if nome.lower() == 'sair':
        break
    
    quantidade = int(input('Digite a idade: '))
    produto = {'nome': nome, 'quantidade': quantidade}
    inventario.adicionar_produto(produto)

inventario.listar_produtos()
