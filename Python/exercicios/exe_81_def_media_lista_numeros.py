""" Programa para calcular a média de uma lista de números.
Situação: Este programa precisa permitir de valores com casas decimais ou negativos. 
Observação: Toda a lista vai ser inserida em um único input """
while True:
    def media():
        try:
            numeros = input('Digite uma sequência de números (separados por espaço): ').split()
            lista = [float(i) for i in numeros]
            return sum(lista)/len(lista)
        except ValueError:
            print('Opção inválida.')
            return 0
    print(f'A média da lista de números digitados é: {media()}')
