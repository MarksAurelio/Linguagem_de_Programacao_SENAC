""" Escreva um programa que solicite ao usuário que insira números 
e calcule a soma desses números até que a soma ultrapasse um limite específico, 
usando um loop while """
for i in range(2):
    numero = int(input('Digite um número: '))
    soma = soma + numero
    while soma <= 100:
        print('A soma dos números chegou ao limite.')
        soma = soma + 1
