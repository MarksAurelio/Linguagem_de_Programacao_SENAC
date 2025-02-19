""" Escreva um programa que solicite ao usuário que insira números 
e calcule a soma desses números até que a soma ultrapasse um limite específico, 
usando um loop while """
numero = 0
soma = 0

limite = int(input('Digite um limite: '))

while soma <= limite:
   numero = int(input('Informe um número para a soma: '))
   soma += numero
print(soma)
