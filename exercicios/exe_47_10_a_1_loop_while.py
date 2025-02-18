""" Escreva um programa faça a contagem regressiva de 1 a 10 usando um loop while e imprima cada número. """
count = 10
while count >= 1:
    print(count)
    count = count - 1

# ou

numero = int(input('Digite um número: \n'))

for i in range(numero, 0, -1):
    print(i)   