""" Escreva uma função chamada soma que aceita dois argumentos e retorna a soma deles.
#Com argumento
def soma(a, b): 
        return a + b 
 
# Exemplo de uso: 
resultado = soma(3, 5) 
print(resultado) # Saí

#Sem argumento
def saudacao(): 
         print("Olá, mundo!") 
         # Chamando a função
saudacao()

Em Python, def é uma palavra-chave usada para definir uma função. 
Quando você usa def, está indicando ao interpretador Python que está prestes a definir uma função 
com um nome específico, parâmetros (se houver) e um bloco de código que será executado quando 
a função for chamada. """
def soma(a, b):
    return a + b
resultado = soma(1, 2)
print(f'O resultado da soma é: {resultado}')

def saudacao():
    print('Olá mundo!')
saudacao()
