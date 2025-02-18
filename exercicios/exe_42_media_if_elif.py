""" Crie um programa que receba 4 notas de um aluno e calcule a média: 
Nota >= 6 Aprovado
Nota < 6 e nota > 4 Recuperação
Nota <= 4 Reprovado """
soma = 0
count = 0
for i in range(4):
    count = count + 1
    nota = float(input(f'Digite a {count}° nota: '))
    soma = soma + nota
media = soma / 4
print('A média de notas do aluno é:', round(media))
if media >= 6:
    print('Aprovado!')
elif media < 6 and media > 4:
    print('Recuperação!')
else:
    print('Reprovado!')
