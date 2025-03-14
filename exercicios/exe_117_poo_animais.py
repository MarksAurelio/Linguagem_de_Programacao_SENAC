""" Crie um programa em Python que modele um sistema de animais utilizando herança e encapsulamento.

Implemente a classe Animal com os seguintes atributos privados:

especie (string): Representa a espécie do animal.
nome (string): Representa o nome do animal.
idade (inteiro): Representa a idade do animal.
A classe deve conter os seguintes métodos:

emitir_som(): Retorna uma mensagem indicando o som que o animal faz.
informacoes(): Retorna uma string com as informações do animal.
Crie uma classe Cachorro que herde de Animal e adicione o método:

abanar_rabo(): Retorna uma mensagem indicando que o cachorro está abanando o rabo. """
class Animal:
    def __init__(self, especie, nome, idade):
        self.__especie = especie
        self.__nome = nome
        self.__idade = idade

    def emitir_som(self):
        return 'Au au au'
    
    def informacoes(self):
        return f'Espécie: {self.__especie}\nNome: {self.__nome}\nIdade: {self.__idade}'


animal = Animal('Cachorro', 'Markoff', 4)   

print(animal.emitir_som())
print(animal.informacoes())

class Cachorro(Animal):
    def __init__(self, especie, nome, idade):
        super().__init__(especie, nome, idade)

    def informacoes(self):
        return super().informacoes()

    def abanar_rabo(self):
        return f'O cachorro está abanando o rabo.'

cachorro = Cachorro('Cachorro', 'Markoff', 4)

print(cachorro.emitir_som())
print(cachorro.informacoes())
print(cachorro.abanar_rabo())
