""" Crie um programa em Python que aceite uma TUPLA de linguagens de programação 
e as junte em uma única String separada por hífens, 
verificar o tipo da variável antes e após a operação: """
tupla= "Python", "Java", "C#", "C++", "PHP"
string_tupla = sep="-".join(tupla)
print(string_tupla)
print(type(string_tupla))
