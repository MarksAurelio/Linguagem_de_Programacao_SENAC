""" Crie uma classe chamada Livro com os seguintes atributos:

titulo (público): título do livro.
__preco (privado): preço do livro.
Implemente um método chamado exibir_preco() que retorne o preço do livro formatado.
No código principal, crie uma instância de Livro e exiba o preço usando o método, evidenciando que o atributo privado não pode ser acessado diretamente. """
class Livro:
    def __init__(self, titulo, preco):
        self.titulo = titulo
        self.__preco = preco

    def exibir_preco(self):
        return self.__preco

livro = Livro('Amizade', 19.90)

# Acesso ao atributo público
print(f'O título do livro é {livro.titulo}')

# Acesso ao atributo privado (gera erro)
# print(f'O preço do livro é {livro.__preco}')

# Acesso ao atributo privado através do método
print(f'O preço do livro é {livro.exibir_preco()}')
