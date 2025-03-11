""" Crie um programa em Python que implemente uma Agenda de Contatos utilizando o paradigma da Programação Orientada a Objetos (POO). O programa deve permitir ao usuário armazenar e gerenciar uma lista de contatos, onde cada contato possui um nome e um número de telefone.

Requisitos
Criar uma classe Contato
Deve conter os atributos:
nome: representa o nome do contato.
telefone: representa o número de telefone do contato.
Deve implementar o método __str__, que retorna uma string formatada no seguinte padrão:
              class Contato:
                   def __init__(self, nome, telefone):
                   self.nome = nome
                   self.telefone = telefone
   
             def __str__(self):
                    return f"{self.nome}: {self.telefone}"


Criar uma classe Agenda
Deve conter uma lista interna para armazenar os contatos.
Deve possuir os seguintes métodos:
adicionar_contato(nome, telefone): Adiciona um novo contato à agenda.
listar_contatos(): Exibe todos os contatos armazenados.
buscar_contato(nome): Busca um contato pelo nome e exibe suas informações, se encontrado.
remover_contato(nome): Remove um contato da agenda, se ele existir.


Implementar um exemplo de uso:
Criar uma instância da classe Agenda.
Adicionar pelo menos dois contatos.
Exibir a lista de contatos.
Buscar um contato específico pelo nome.
Remover um contato e exibir novamente a lista para confirmar a remoção.
Exemplo de Saída Esperada """
class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.lista = []

    def adicionar_contato(self):
        nome = input('Digite o nome: ').capitalize()
        telefone = input('Digite o telefone: ')
        self.lista.append({'nome': nome, 'telefone': telefone})
        print(self.lista)

    def listar_contatos(self):
        print(f'{self.nome}')
        for contato in self.lista:
            print(f'- Nome: {contato["nome"]}\n- Telefone: {contato["telefone"]}')

    def buscar_contato(self):
        nome = input('Qual o nome para ser localizado: ').capitalize()
        for contato in self.lista:
            if contato['nome'] == nome:
                print('Nome localizado.')
                return
        print('Nome não localizado.')

    def remover_contato(self):
        nome = input('Digite o nome para ser removido: ').capitalize()
        for contato in self.lista:
            if contato['nome'] == nome:
                self.lista.remove(contato)
                print('Nome removido com sucesso.')
                return
        print('Nome não localizado.')

    def sair(self):
        print('Saindo...')

    def menu(self):
        print('Menu')
        print('1. Adcionar contato')
        print('2. Listar contatos')
        print('3. Buscar contato')
        print('4. Remover contato')
        print('5. Sair')
        pergunta = int(input('Escolha uma opção: '))
        return pergunta

contato = Contato('Meus Contatos', 'Telefone')

while True:
    pergunta = contato.menu()
    if pergunta == 1:
        contato.adicionar_contato()
    elif pergunta == 2:
        contato.listar_contatos()
    elif pergunta == 3:
        contato.buscar_contato()
    elif pergunta == 4:
        contato.remover_contato()
    elif pergunta == 5:
        contato.sair()
                              
    para_continuar = input('Gostaria de realizar outra operação? (s/n): ').lower()
    if para_continuar != 's':
        break
    