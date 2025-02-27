""" Enunciado:
Um número perfeito é um número inteiro positivo que é igual à soma de seus divisores próprios, ou seja, 
a soma de todos os seus divisores, excluindo o próprio número.
Por exemplo:
6 é um número perfeito, porque seus divisores próprios são 1,2,3, e a soma 1+2+3=6.
28 é um número perfeito, porque seus divisores próprios são 1,2,4,7,14, e a soma 1+2+4+7+14=28.
Objetivo:
Crie uma lista de números inteiros.
Para cada número, verifique se ele é um número perfeito.
Exiba os números perfeitos encontrados na lista.
  
Em Python, append() é um método usado em listas para adicionar um novo elemento ao final da lista. 
Ele modifica a lista original e não retorna um novo objeto.  
lista.append(elemento) """
while True:
    numeros = input('Digite uma sequência de números inteiros (separado por espaços): ').split()

    def numero_perfeito():
        try:
            lista = [int(i) for i in range(1,numeros) if numeros % i == 0]
            lista_perfeitos = []
            return sum(lista) == numeros
        for 
        if numero_perfeito():
                
                print(lista_perfeitos.append(lista))
            return lista_perfeitos
        except ValueError:
            print('Opção inválida.')
            return 0
    print(f'Os números perfeitos encontrados na lista são: {numero_perfeito()}')
