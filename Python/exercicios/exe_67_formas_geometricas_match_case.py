""" Instrução sobre match-case
O match-case é uma estrutura de controle de fluxo introduzida no Python 3.10, 
que funciona como um switch-case encontrado em outras linguagens. Ele permite verificar padrões de valores 
e executar um bloco de código específico conforme o caso correspondente.

Sintaxe básica:
valor = input("Digite um valor 'A ou B': ").upper()

match valor:
    case "A":
        print("Você escolheu A")
    case "B":
        print("Você escolheu B")
    case _:
        print("Opção inválida")

Questão 1: Identificando Formas Geométricas
Escreva um programa em Python que solicita ao usuário o nome de uma forma geométrica (triângulo, quadrado,
círculo) e utiliza match-case para exibir uma mensagem correspondente à forma escolhida.

Resultado:
Digite uma forma geométrica: quadrado
Saída: O quadrado tem 4 lados iguais. """
while True:
    formas_geometricas = input('Digite uma das formas formas geométricas a seguir (triângulo, quadrado, círculo): ').upper()

    match formas_geometricas:
        case 'A':
            print('O triângulo têm 3 lados.')
        case 'B':
            print('O quadrado têm 4 lados.')
        case 'C':
            print('O círculo não possui lados.')
        case _:
            print('Opção inválida.')
