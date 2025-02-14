""" Escreva um programa em Python que aceite uma sequência de linguagens de programação separadas por espaços. 
O programa deve dividir essa sequência em uma lista de linguagens individuais 
e imprimir a lista resultante. Ao final imprimir o tipo da variável. """
linguagens = "Python,Java,C#,C++,PHP"
string_linguagens = linguagens.split(',')
print(string_linguagens)
print(type(string_linguagens))
