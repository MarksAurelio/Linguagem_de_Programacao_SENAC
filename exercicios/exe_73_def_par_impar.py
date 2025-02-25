""" Escreva uma função chamada par_ou_impar que aceita um número como argumento e retorna "par" 
se o número for par e "ímpar" se o número for ímpar. """
while True:
    def par_ou_impar(numero):
        if numero % 2 == 0:
            print('Par.')
        else:
            print('Ímpar.')

    numero = int(input('Digite um número: '))
    par_ou_impar(numero)
