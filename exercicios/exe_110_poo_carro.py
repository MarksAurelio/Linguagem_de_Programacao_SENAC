""" Crie uma classe chamada Carro com os seguintes atributos:

modelo (público): modelo do carro.
__ano (privado): ano do carro.
Implemente um método chamado exibir_ano() que retorne uma string informando o ano do carro.
No código principal, crie uma instância de Carro e exiba o ano usando o método, demonstrando que o atributo privado não pode ser acessado diretamente. """
class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.__ano = ano

    def exibir_ano(self):
        return print(f'O ano do carro é {self.__ano}.')

carro = Carro('Civic', 2005)

# Acesso ao atributo público
print(f'O modelo do carro é {carro.modelo}.')

# Acesso ao atributo privado (gera erro)
# print(f'O ano do carro é {carro.__ano}')

# Acesso ao atributo privado através do método
print(carro.exibir_ano())
