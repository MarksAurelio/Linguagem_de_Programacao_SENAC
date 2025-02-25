""" Escreva uma função chamada dobro que aceita um número como argumento e retorna o dobro desse número. """
def dobro(a):
    return a + a
resultado = dobro(2)
print(resultado)

# ou
numero = int(input('Digite um número: '))
print(f'O dobro do número {numero} é: {dobro(numero)}' )
