""" Escreva um programa em Python que solicite ao usuário para adivinhar um número entre 1 e 100. 
O programa deve continuar pedindo um palpite até que o usuário adivinhe corretamente o número. 
O programa deve fornecer dicas se o palpite estiver muito alto ou muito baixo


Instruções
Para usar as funções e recursos de uma biblioteca em Python, 
você precisa primeiro importá-la para o seu script ou programa. 
A importação é feita usando a palavra-chave import, seguida do nome da biblioteca.
import random
Depois de importar a biblioteca, você pode chamar suas funções e recursos em seu programa. 
Isso é feito usando a sintaxe nome_da_biblioteca.nome_da_função().
numero_advinhado =  random.randint(1, 100)  
import random

# Função random()
# Esta função retorna um número de ponto flutuante aleatório no intervalo [0.0, 1.0), incluindo 0.0, 
mas excluindo 1.0.
numero_advinhado = random.random()
print("Número aleatório (random()):", numero_advinhado)

# Função randint(a, b)
# Esta função retorna um número inteiro aleatório no intervalo [a, b], incluindo ambos os extremos.
numero_advinhado = random.randint(1, 100)
print("Número inteiro aleatório (randint(1, 100)):", numero_advinhado)

# Função choice(seq)
# Esta função retorna um elemento aleatório de uma sequência não vazia.
lista = ['maçã', 'banana', 'laranja', 'uva']
escolha_aleatoria = random.choice(lista)
print("Escolha aleatória de uma lista (choice(lista)):", escolha_aleatoria) """
import random

numero_aleatorio = random.randint(1, 10)
numero_digitado = 0
while True:
    numero_digitado = int(input('Informe um número: '))
    if numero_digitado == numero_aleatorio:
        print('Você acertou o número!')
        break
    elif numero_digitado < numero_aleatorio:
        print('Frio')
    elif numero_digitado > numero_aleatorio:
        print('Quente')
