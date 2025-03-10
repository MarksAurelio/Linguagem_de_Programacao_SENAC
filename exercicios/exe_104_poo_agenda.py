""" Crie uma classe chamada Agenda que armazena uma lista de contatos. Cada contato deve ter um nome e um número de telefone. A classe deve ter os seguintes métodos:
adicionar_contato(nome, telefone): adiciona um contato à agenda.
listar_contatos(): exibe todos os contatos armazenados. """
class Agenda:
    def __init__(self, nome):
        self.nome = nome
        self.lista = []

    def adicionar_contato(self, contato):
        self.lista.append(contato)

    def listar_contatos(self):
        print(f'A lista de contato {self.nome}')
        for contato in self.lista:
            print(f'- Nome: {contato["nome"]}, Telefone: {contato["telefone"]}')

agenda = Agenda('Minha Agenda')

while True:
    nome = input('Digite um nome (ou sair para finalizar): ')
    
    if nome.lower() == 'sair':
        break
    telefone = input('Digite o telefone: ')  
    contato = {'nome': nome, 'telefone': telefone} 
    agenda.adicionar_contato(contato)

agenda.listar_contatos()
