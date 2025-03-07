""" Objetivo: Criar uma classe Aluno que receba o nome e a nota do aluno no construtor e tenha um método para verificar se ele foi aprovado ou reprovado.

Instruções:
Crie a classe Aluno com os atributos nome e nota.
No construtor (__init__), inicialize esses atributos.
Crie um método chamado verificar_aprovacao(), que retorna:
                 "Aprovado" se a nota for maior ou igual a 7.
                 "Reprovado" caso contrário.
Instancie dois alunos, atribua diferentes notas e exiba o resultado. """
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        
    def verificar_aprovacao(self):
        if self.nota >= 7:
            print(f'{self.nome} Aprovado.')
        else:
            print(f'{self.nome} Reprovado.')

nome1 = input('Digite o nome do aluno: ').capitalize()
nota1 = float(input('Digite uma nota para o primeiro aluno: '))  

aluno1 = Aluno(nome1, nota1)
aluno1.verificar_aprovacao()

nome2 = input('Digite o nome do aluno: ').capitalize()
nota2 = float(input('Digite uma nota para o primeiro aluno: '))  

aluno2 = Aluno(nome2, nota2)
aluno2.verificar_aprovacao()
