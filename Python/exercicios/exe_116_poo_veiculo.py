""" Crie um programa em Python que modele um sistema de veículos utilizando herança.

Implemente uma classe chamada Veiculo que tenha os seguintes atributos:

marca: Representa a marca do veículo.
modelo: Representa o modelo do veículo.
ano: Representa o ano de fabricação do veículo.

A classe Veiculo deve ter os seguintes métodos:

exibir_dados(): Retorna uma string com as informações do veículo.
ligar(): Retorna uma mensagem informando que o veículo foi ligado.

Crie uma classe Carro que herde da classe Veiculo e adicione um novo atributo:

portas: Representa a quantidade de portas do carro. """
class Veiculos:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}'
    
    def ligar(self):
        return 'Veículo ligado.'

veiculos = Veiculos('Honda', 'Civic', '2005')

class Carros(Veiculos):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def exibir_dados(self):
        return f'{super().exibir_dados()}\nPortas: {self.portas}'
    
carros = Carros('Honda', 'Civic', '2005', 4)

print(carros.ligar())
print(carros.exibir_dados())
