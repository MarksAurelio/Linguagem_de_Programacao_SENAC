# Escreva um programa em Python que peça ao usuário para inserir dois números 
# e calcule a divisão do primeiro número pelo segundo número. 
# Certifique-se de verificar se o segundo número não é zero antes de realizar a divisão. 
# Em seguida, exiba o resultado da divisão.
numero_1 = float(input('Insira o primeiro número: '))
numero_2 = float(input('Insira o segundo número: '))
divisao = numero_1 / numero_2
divisao_arredondada = round(divisao, 2)
print(f'O resultado da divisão é: {divisao_arredondada}')
