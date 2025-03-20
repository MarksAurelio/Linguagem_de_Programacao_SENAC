""" Crie uma função que receba 4 números e retorne a média dos números """
def media (a, b, c, d):
    return (a + b + c + d) / 4

a = int(input('Digite o 1° número: '))
b = int(input('Digite o 2° número: '))
c = int(input('Digite o 3° número: '))
d = int(input('Digite o 4° número: '))

resultado = media(a, b, c, d)
print(f'O resultado da média dos números é: {resultado}')
