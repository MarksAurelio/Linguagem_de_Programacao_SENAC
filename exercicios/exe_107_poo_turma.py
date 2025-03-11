""" Crie uma classe chamada Turma que armazena uma lista de alunos. A classe deve ter os seguintes métodos:
adicionar_aluno(nome, idade): adiciona um aluno à turma.
listar_alunos(): exibe todos os alunos cadastrados. """
class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.lista = []

    def adicionar_aluno(self, aluno):
        self.lista.append(aluno)

    def listar_alunos(self):
        print(f'{self.nome}:')
        for aluno in self.lista:
            print(f'- Nome: {aluno["nome"]}\n- Idade: {aluno["idade"]}')

turma = Turma('Minha Turma')

while True:
    nome = input('Digite um aluno (ou sair para finalizar): ').capitalize()
    if nome.lower() == 'sair':
        break
    idade = int(input('Digite a idade: '))
    aluno = {'nome': nome, 'idade': idade}
    turma.adicionar_aluno(aluno)

turma.listar_alunos()
