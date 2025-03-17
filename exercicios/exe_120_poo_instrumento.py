""" Implemente a classe Instrumento com o atributo privado tipo.
Crie um método emitir_som que retorna a string "Som do instrumento".
Implemente a classe Guitarra que herda de Instrumento e adicione o atributo privado cordas.
Sobrescreva o método emitir_som para retornar "Som da guitarra".

   **Instrução sobre sobrescrita:** A sobrescrita do método `emitir_som` permite que a classe `Guitarra` tenha um som específico diferente do som genérico da classe `Instrumento`. Utilizamos `super()` para chamar o método original, caso necessário.

Crie uma instância de Guitarra e exiba o som emitido.
Implemente um método que retorna o número de cordas.
Crie outra instância de Guitarra com um número diferente de cordas. """
class Instrumento:
    def __init__(self, tipo):
        self.__tipo = tipo

    def emitir_som(self):
        return f'Som do instrumento {self.__tipo}'

class Guitarra(Instrumento):
    def __init__(self, tipo, cordas):
        super().__init__(tipo)
        self.__cordas = cordas

    def emitir_som(self):
        return f'{super().emitir_som()}\nCordas: {self.__cordas}'
    
guitarra = Guitarra('Guitarra', 4)
guitarra_2 = Guitarra('Guitarra', 6)
    
print(guitarra.emitir_som())
print(guitarra_2.emitir_som())
