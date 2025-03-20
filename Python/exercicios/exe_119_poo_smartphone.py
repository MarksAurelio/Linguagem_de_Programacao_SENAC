""" Implemente a classe Dispositivo com os atributos privados marca, modelo e preco.
Crie um método exibir_dados que retorna uma string com as informações do dispositivo.
Implemente a classe Smartphone que herda de Dispositivo e adicione o atributo privado sistema_operacional.
Sobrescreva o método exibir_dados para incluir o sistema operacional.
              **Instrução sobre sobrescrita:** A sobrescrita de um método ocorre quando a classe filha redefine um método herdado da                  classe pai para adicionar ou modificar seu comportamento. Para isso, utilizamos a função `super()`, que permite chamar o                  método original da classe pai e adicionar novos comportamentos. No caso, a classe `Smartphone` herda o método                               `exibir_dados` da classe `Dispositivo`, mas o reescrevemos para adicionar o atributo `sistema_operacional`.

                class Dispositivo:
                        def __init__(self, marca, modelo, preco):
                              self.__marca = marca
                              self.__modelo = modelo
                              self.__preco = preco

                         def exibir_dados(self):
                               return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Preço: {self.__preco}"

               class Smartphone(Dispositivo):
                         def __init__(self, marca, modelo, preco, sistema_operacional):
                                    super().__init__(marca, modelo, preco)
                                    self.__sistema_operacional = sistema_operacional

                         # Sobrescrita do método exibir_dados
                         def exibir_dados(self):
                                    dados_dispositivo = super().exibir_dados()
                                     return f"{dados_dispositivo}, Sistema Operacional: {self.__sistema_operacional}"
Crie uma instância de Smartphone com dados fictícios e exiba as informações.
Crie um método que calcula o preço com desconto percentual.
Aplique o método de desconto para reduzir 10% do preço do smartphone.
Implemente um método para atualizar o preço do dispositivo.
Atualize o preço do smartphone para 3000 e exiba as informações atualizadas.
Crie uma nova instância de Smartphone com dados fictícios e outro sistema operacional. """
class Dispositivo:
    def __init__(self, marca, modelo, preco):
        self.__marca = marca
        self.__modelo = modelo
        self.__preco = preco

    def exibir_dados(self):
        return f'Marca: {self.__marca}\nModelo: {self.__modelo}\nPreço: {self.__preco}'
    
    def desconto(self):
        desconto_a_vista = self.__preco * 0.10
        desconto_smartphone = self.__preco - desconto_a_vista
        return f'O valor do aparelho {self.__marca} {self.__modelo} com o desconto de 10% é R${desconto_smartphone:.1f}'
    
dispositivo = Dispositivo('Samsung', 'S24', 4.900)

print(dispositivo.exibir_dados())
print(dispositivo.desconto())

class Smartphone(Dispositivo):
    def __init__(self, marca, modelo, preco, sistema_operacional):
        super().__init__(marca, modelo, preco)
        self.__sistema_operacional = sistema_operacional

    def exibir_dados(self):
        return f'{super().exibir_dados()}\nSistema Operacional: {self.__sistema_operacional}'

    def desconto(self):
        return super().desconto()
    
smartphone = Smartphone('Samsung', 'S25 Ultra', 10.999, 'Android')

print(smartphone.exibir_dados())
print(smartphone.desconto())

smartphone_2  = Smartphone('Samsung', 'S25 Plus', 6.999, 'Android')

print(smartphone_2.exibir_dados())
print(smartphone_2.desconto())
