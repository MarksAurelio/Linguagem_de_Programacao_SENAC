""" Faça uma programa que capta dados e a quantidade de fitas que uma vídeo locadora possui 
e o valor que ela cobra por cada aluguel, informe:
Sabendo que um terço das fitas são alugadas por mês, qual o seu faturamento anual.
Sabendo que quando o cliente atrasa a entrega é cobrada uma multa de 10% sobre o valor do aluguel. 
Um décimo das fitas alugadas no mês são devolvidas com atraso é o valor ganho com multas por mês. """
estoque = int(input('Estoque de fitas: '))
valor_aluguel = float(input('Digite o valor do aluguel: '))
quantidade_fitas_alugadas = estoque / 3 * valor_aluguel
multa_atraso = quantidade_fitas_alugadas * 0.1
faturamento_anual = (quantidade_fitas_alugadas * 12) + multa_atraso * 12
print(f'O faturamento anual da locadora é: {faturamento_anual}')
