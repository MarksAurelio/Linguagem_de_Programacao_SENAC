""" Desenvolver um programa em Python que permita gerenciar o cadastro de alunos de forma interativa, utilizando uma estrutura (lista ou dicionário) para armazenar os dados.

Funções a serem implementadas:
limpar_tela()
exibir_nome_do_programa()
exibir_opcoes()
cadastrar_aluno()
listar_alunos()
buscar_aluno()
remover_aluno()
finalizar_app()
escolher_opcao()
def limpar_tela():
    # Limpa a tela imprimindo várias quebras de linha
    print("\n" * 50)

def main():
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

Requisitos do Programa:
Exibir uma arte ASCII que contenha o título “Cadastro de Alunos - Senac DF”. https://patorjk.com/software/taag/#p=display&f=Epic&t=Senac%20DF
Apresentar um menu com as opções:
Cadastrar aluno
Listar alunos
Buscar aluno
Remover aluno
Sair
Limpar a tela.
Executar a ação correspondente à opção escolhida.
Encerrar o programa corretamente ao selecionar a opção “Sair”. """

cadastro_de_alunos = []

print('''
 _______  _______  _        _______  _______    ______   _______ 
(  ____ \(  ____ \( (    /|(  ___  )(  ____ \  (  __  \ (  ____ |
| (    \/| (    \/|  \  ( || (   ) || (    \/  | (  \  )| (    \/
| (_____ | (__    |   \ | || (___) || |        | |   ) || (__    
(_____  )|  __)   | (\ \) ||  ___  || |        | |   | ||  __)   
      ) || (      | | \   || (   ) || |        | |   ) || (      
/\____) || (____/\| )  \  || )   ( || (____/\  | (__/  )| )      
\_______)(_______/|/    )_)|/     \|(_______/  (______/ |/       
                                                                 
''')

def menu():
    print('Menu')
    print('1. Cadastrar aluno')
    print('2. Listar alunos')
    print('3. Buscar aluno')
    print('4. Remover aluno')
    print('5. Sair')
    print('6. Limpar tela')
    pergunta = int(input('Escolha uma opção: '))
    return pergunta

def cadastrar_aluno():
    nome = input('Qual o nome a ser cadastrado: ')
    cadastro_de_alunos.append(nome)
    print('Cadastro do nome realizado com sucesso.')

def listar_alunos():
    if not cadastro_de_alunos:
        print('Nesta lista não há o aluno citado.')
    else:
        print('Lista:')
        for i, nome in enumerate(cadastro_de_alunos):
            print(f'{i} - {nome}')

def buscar_aluno():
    nome = input('Qual o nome para ser localizado? ')
    if nome in cadastro_de_alunos:
        print('Nome localizado.')
    else:
        print('Nome não localizado.')

def remover_aluno():
    nome = input('Qual o nome para exclusão: ')
    if nome in cadastro_de_alunos:
        cadastro_de_alunos.remove(nome)
        print('Nome excluído com sucesso.')
    else:
        print('Esse nome não foi localizado.')

def sair():
    print('Saindo...')

def limpar_tela():
    print("\n" * 50)

while True:
    pergunta = menu()
    if pergunta == 1:
        cadastrar_aluno()
    elif pergunta == 2:
        listar_alunos()
    elif pergunta == 3:
        buscar_aluno()
    elif pergunta == 4:
        remover_aluno()
    elif pergunta == 5:
        sair()
    else:
        print('Esta opção não foi localizada. Por favor escolha outra opção.')

    para_continuar = input('Gostaria de realizar outra operação? (s/n): ')
    if para_continuar.lower() != 's':
        break
        
        
