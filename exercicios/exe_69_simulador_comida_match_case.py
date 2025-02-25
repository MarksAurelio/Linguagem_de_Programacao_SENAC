""" Questão 3: Simulador de Comidas
Faça um programa que receba um número de 1 a 5 e retorne um prato específico usando match-case. 
As opções podem ser:

1: Pizza
2: Hambúrguer
3: Sushi
4: Salada
5: Lasanha
Caso o número esteja fora desse intervalo, exiba "Opção inválida". """
while True:
    numero = int(input('Digite um número de 1 a 5: '))

    match numero:
        case 1:
            print('Pizza.')
        case 2:
            print('Hambúrguer.')
        case 3:
            print('Sushi')
        case 4:
            print('Salada')
        case 5:
            print('Lasanha')
        case _:
            print('Opção inválida.')
