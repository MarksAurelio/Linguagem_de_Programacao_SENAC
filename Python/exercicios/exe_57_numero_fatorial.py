""" Implemente um programa que imprima o fatorial do número informado pelo usuário. 
numero = int(input("Digite um número: "))
resultado = 1
i = numero

while i > 1:
    resultado *= i
    print(f"{resultado // i} * {i} = {resultado}")
    # faz divisão inteira e retorna apenas a parte inteira do resultado, descartando a parte decimal.
    # print(10 / 3)   # Saída: 3.3333333333333335 (float)
    # print(10 // 3)  # Saída: 3 (int, sem parte decimal)

    i -= 1

print(f"Fatorial de {numero} é {resultado}")


# Segunda Forma
numero = int(input("Digite um número: "))  
resultado = 1  
i = numero  

while i > 1:  
    anterior = resultado  # Guarda o valor antes da multiplicação
    resultado *= i  
    print(f"{anterior} * {i} = {resultado}")  # Usa a variável auxiliar  (anterior)
    i -= 1  

print(f"Fatorial de {numero} é {resultado}") """
numero = int(input('Digite um número: '))
fatorial = 0
cont = 1
while numero >= cont:
    fatorial = fatorial + cont
    cont = cont + 1
print(fatorial)
