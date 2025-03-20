print('### Bem vindo ao Quiz de Informática! ###')

print('### O que é um CPU? ### \n 1. Unidade Central de Processamento \n 2. Placa de Vídeo \n 3. Memória RAM \n 4. Fonte de Alimentação \n Escolha a opção correta (1, 2, 3, 4)')
respostas = int(input('Digite um número para a resposta: '))
match respostas:
    case 1:
        print('Unidade Central de Processamento.')
    case 2:
        print('Placa de Vídeo.')
    case 3:
        print('Memória RAM.')
    case 4:
        print('Fonte de Alimentação.')
    case _:
        print('Opção inválida.')
if respostas == 1:
    print('### Correto! ###')
else:
    print('### Errado! ###')

print('### O que é um sistema operacional? ### \n 1 . Software que gerencia hardware e software \n 2 . Um tipo de antivírus \n 3 . Um programa de edição de texto \n 4 . Um hardware de rede \n Escolha a opção correta (1, 2, 3, 4)')
respostas_2 = int(input('Digite um número para a resposta: '))
match respostas_2:
    case 1:
        print('Software que gerencia hardware e software.')
    case 2:
        print('Um tipo de antivírus.')
    case 3:
        print('Um programa de edição de texto.')
    case 4:
        print('Um hardware de rede.')
    case _:
        print('Opção inválida.')
if respostas_2 == 1:
    print('### Correto! ###')
else:
    print('### Errado! ###')

def pontuação_final(respostas, respostas_2):
    pontuacao = 0
    if respostas == 1:
        pontuacao = pontuacao + 1
    if respostas_2 == 1:
        pontuacao = pontuacao + 1
    return pontuacao
print(f'Sua pontuação final é: {pontuação_final(respostas, respostas_2)} / 2')
