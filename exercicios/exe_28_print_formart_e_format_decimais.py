""" Escreva um programa em Python que utilize o método format() para formatar uma mensagem 
com informações sobre um livro. 
Você deve criar variáveis para armazenar as seguintes informações: """
titulo_livro = 'O Pequeno Príncipe'
autor = 'Antoine de Saint-Exupér'
ano_publicacao = 1943
preco = 39.90
mensagem = '{} é um livro escrito por {}. Foi publicado em {} e custa R$ {:.2f}'.format(titulo_livro, autor, ano_publicacao, preco)
print(mensagem)
