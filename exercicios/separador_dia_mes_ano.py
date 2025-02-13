# Escreva um programa em Python que solicite ao usuário informações sobre uma data (dia, mês e ano) 
# e utilize o parâmetro sep na função print() para imprimir a data no formato "DD/MM/AAAA".
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
print(dia, mes, ano, sep='/')
