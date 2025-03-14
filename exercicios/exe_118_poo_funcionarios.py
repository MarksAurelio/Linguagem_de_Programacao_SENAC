""" Crie um programa em Python que modele um sistema de funcionários utilizando herança e encapsulamento.
Implemente a classe Funcionario com os seguintes atributos privados:
nome (string): Representa o nome do funcionário.
cargo (string): Representa o cargo do funcionário.
salario (float): Representa o salário do funcionário.

A classe deve conter os seguintes métodos:
exibir_dados(): Retorna uma string com as informações do funcionário.
calcular_bonus(): Retorna o valor do bônus (10% do salário).

Crie uma classe Gerente que herde de Funcionario e adicione o atributo privado:
setor (string): Representa o setor em que o gerente atua. """
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario

    def exibir_dados(self):
        return f'Nome: {self.__nome}\nCargo: {self.__cargo}\nSalário: {self.__salario}'
    
    def calcular_bonus(self):
        bonus = self.__salario * 0.10
        salario_bonus = self.__salario + bonus
        return f'O salário do {self.__nome} com o bônus é {salario_bonus}.'
    
funcionario = Funcionario('Marks', 'Gerente', 10.000)

print(funcionario.exibir_dados())
print(funcionario.calcular_bonus())

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, setor):
        super().__init__(nome, cargo, salario)
        self.__setor = setor

    def exibir_dados(self):
        return f'{super().exibir_dados()}\nSetor: {self.__setor}'
    
gerente = Gerente('Marks', 'Gerente', 10.000, 'Vendas')

print(gerente.exibir_dados())
