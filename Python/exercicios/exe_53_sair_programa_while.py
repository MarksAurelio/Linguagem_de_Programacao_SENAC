""" Crie um programa que solicite ao usuário para digitar uma palavra. O programa deve continuar solicitando 
palavras até que o usuário digite a palavra "sair", momento em que o programa deve exibir uma mensagem de 
despedida e encerrar.


while True:
    palavra = input("Digite uma palavra (ou 'sair' para encerrar): ")
    if palavra == 'sair':
        print("Encerrando o programa...")
        break

Explicação:

while True  : Inicia um loop infinito, que continuará sendo executado indefinidamente até que seja 
explicitamente interrompido com auxilio por exemplo do break.
break: Interrompe imediatamente o loop while True, fazendo com que o programa saia do loop 
e encerre a execução. """
palavra_chave = ''

while palavra_chave != 'sair':
    palavra_chave = str(input('Digite uma nova palavra (ou "sair" para encerrar.): \n'))
    
if palavra_chave == 'sair':
    print('Encerrando o programa...')
