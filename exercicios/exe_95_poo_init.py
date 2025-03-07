""" O que é POO em Python?  

A Programação Orientada a Objetos (POO) organiza o código em classes e objetos, facilitando a reutilização e manutenção.

Construtor (__init__): Método especial chamado ao criar um objeto, inicializando seus atributos.
self: Referência ao próprio objeto, usada para acessar atributos e métodos dentro da classe.
Instanciação: Processo de criar um objeto a partir de uma classe.

class Carro:
    def __init__(self, marca):
        self.marca = marca  # `self.marca` pertence à instância

    def mostrar_marca(self):
        print(f"O carro é da marca {self.marca}")

# Criando objeto e chamando método
carro1 = Carro("Toyota")
carro1.mostrar_marca()  # Saída: O carro é da marca Toyota

Atividade:
Criar uma classe Aluno com nome e curso
Criar uma classe Livro com título e autor
Criar uma classe Celular com modelo e fabricante
Criar uma classe Cachorro com nome e raça
Criar uma classe Computador com processador e memória
Criar uma classe Funcionario com nome e cargo
Criar uma classe Bicicleta com tipo e tamanho do aro
Criar uma classe Filme com título e diretor
Criar uma classe Restaurante com nome e tipo de cozinha
Criar uma classe Avião com companhia aérea e modelo """

# Criar uma classe Aluno com nome e curso
class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso

    def mostrar_nome(self):
        print(f'O nome do aluno é {self.nome}.')
       

    def mostrar_curso(self):
        print(f'O aluno cursa {self.curso}.')
        

aluno1 = Aluno('Marks', 'Python')
aluno1.mostrar_nome()
aluno1.mostrar_curso()

# Criar uma classe Livro com título e autor
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrar_titulo(self):
        print(f'O livro têm o Titulo {self.titulo}.')

    def mostrar_autor(self):
        print(f'O autor do livro é {self.autor}.')

livro1 = Livro('"A obra"', 'Mariano Dias')
livro1.mostrar_titulo()
livro1.mostrar_autor()

#Criar uma classe Celular com modelo e fabricante
class Celular:
    def __init__(self, modelo, fabricante):
        self.modelo = modelo
        self.fabricante = fabricante

    def mostrar_modelo(self):
        print(f'O modelo do celular é {self.modelo}.')

    def mostrar_fabricante(self):
        print(f'O fabricante do celular é {self.fabricante}.')

celular1 = Celular('A55', 'Samsung')
celular1.mostrar_modelo()
celular1.mostrar_fabricante()

# Criar uma classe Cachorro com nome e raça
class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
    
    def mostrar_nome(self):
        print(f'O nome do cachorro é {self.nome}.')

    def mostrar_raca(self):
        print(f'A raça do cachorro é {self.raca}.')

cachorro1 = Cachorro('Markollf', 'vira-lata')
cachorro1.mostrar_nome()
cachorro1.mostrar_raca()

#Criar uma classe Computador com processador e memória
class Computador:
    def __init__(self, processador, memoria):
        self.processador = processador
        self.memoria = memoria

    def mostrar_processador(self):
        print(f'O processador do computador é {self.processador}.')

    def mostrar_memoria(self):
        print(f'A memória do computador é {self.memoria}.')

computador1 = Computador('AMD', '128MB')
computador1.mostrar_processador()
computador1.mostrar_memoria()

# Criar uma classe Funcionario com nome e cargo
class Funcionario:
    def __init__(self, nome_funcionario, cargo):
        self.nome_funcionario = nome_funcionario
        self.cargo = cargo

    def mostrar_nome(self):
        print(f'O nome do funcionário é {self.nome_funcionario}.')

    def mostrar_cargo(self):
        print(f'O cargo do funcionário é {self.cargo}.')

funcionario1 = Funcionario('Thiago', 'Designer')
funcionario1.mostrar_nome()
funcionario1.mostrar_cargo()

# Criar uma classe Bicicleta com tipo e tamanho do aro
class Bicicleta:
    def __init__(self, tipo, tamanho):
        self.tipo = tipo
        self.tamanho = tamanho

    def mostrar_tipo(self):
        print(f'O tipo da bicicleta é {self.tipo}.')

    def mostrar_tamanho(self):
        print(f'O tamanho do aro da bicicleta é {self.tamanho}.')

bicicleta1 = Bicicleta('elétrica', 17)
bicicleta1.mostrar_tipo()
bicicleta1.mostrar_tamanho()

# Criar uma classe Filme com título e diretor
class Filme:
    def __init__(self, titulo, diretor):
        self.titulo = titulo 
        self.diretor = diretor

    def mostrar_titulo(self):
        print(f'O título do filme é {self.titulo}.')

    def mostrar_diretor(self):
        print(f'O diretor do filme é {self.diretor}.')

filme1 = Filme('"O gato"', 'Patrick Home')
filme1.mostrar_titulo()
filme1.mostrar_diretor()

# Criar uma classe Restaurante com nome e tipo de cozinha
class Restaurante:
    def __init__(self, nome, tipo_cozinha):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha

    def mostrar_nome(self):
        print(f'O nome do restarurante é {self.nome}.')

    def mostrar_tipo_cozinha(self):
        print(f'O tipo de cozinha é {self.tipo_cozinha}.')

restaurante1 = Restaurante('Comida Boa', 'brasileira')
restaurante1.mostrar_nome()
restaurante1.mostrar_tipo_cozinha()

# Criar uma classe Avião com companhia aérea e modelo
class Aviao:
    def __init__(self, companhia, modelo):
        self.companhia = companhia
        self.modelo = modelo

    def mostrar_companhia(self):
        print(f'A companhia aérea é {self.companhia}.')

    def mostrar_modelo(self):
        print(f'O modelo do avião é {self.modelo}.')

aviao1 = Aviao('Gol', 'Boeing')
aviao1.mostrar_companhia()
aviao1.mostrar_modelo()
