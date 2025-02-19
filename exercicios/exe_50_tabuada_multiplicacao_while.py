""" Escreva um programa que imprima a tabuada de multiplicação de um número específico até 10, 
usando um loop while """
numero = int(input('Digite um número: '))

for i in range(10):
    print(f'{numero} x {i + 1} =', numero * (i + 1))

# ou
    
cont = 1
numero = int(input('Informe um número: '))
while cont <= 10:
    print(f'{numero} x {cont} = {numero * cont}')
    cont = cont + 1
