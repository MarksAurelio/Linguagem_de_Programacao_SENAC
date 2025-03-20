""" Imprima a tabuada de multiplicação de um número fornecido pelo usuário. """
numero = int(input('Digite um número: '))
for i in range(0, 11):
    print(f'{numero} x {i} =', numero * i)

# ou
while True:
    numero = int(input('Digite um número: '))
    for i in range(10):
        print(f'{numero} x {i + 1} =', numero * (i + 1))
