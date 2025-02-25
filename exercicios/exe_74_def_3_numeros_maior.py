""" Defina uma função, que receba 3 números e retorne o maior deles """
def maior_numero(a, b, c):
    if a > b > c:
        print(a)
    elif a < b > c:
        print(b)
    elif a < b < c:
        print(c)
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
maior_numero(a, b, c)
