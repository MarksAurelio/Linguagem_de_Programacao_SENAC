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
def numero_perfeito(numero):
    try:
        lista = [i for i in range(1, int(numero)) if int(numero) % i == 0]
        return sum(lista) == int(numero)
    except ValueError:
        print('Opção inválida.')
        return False
while True:
    numeros = input('Digite uma sequência de números inteiros (separado por espaços): ').split()
    lista_perfeitos = []
    for numero in numeros:
        if numero_perfeito(numero):
            lista_perfeitos.append(numero)
        
    print(f'Os números perfeitos encontrados na lista são: {lista_perfeitos}')
