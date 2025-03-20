""" Escreva um programa em Python que utilize o método format() para formatar uma mensagem 
com informações sobre um produto. 
Você deve criar variáveis para armazenar as seguintes informações """

""" Em seguida, utilize o método format() para imprimir uma mensagem no seguinte formato: "Produto: [Nome], 
Preço: R$[Preço], Quantidade disponível: [Quantidade]. O valor total do estoque é R$[ValorEstoque].", 
onde [Nome], [Preço] 
e [Quantidade] são espaços reservados que devem ser substituídos pelas informações corretas. 
Além disso, [ValorEstoque] representa o valor total do estoque, 
calculado multiplicando o preço pela quantidade disponível. """
nome_produto = 'Camiseta'
preco = 29.99
quantidade = 100
multiplicacao = preco * quantidade
mensagem = 'Produto: {}, Preço: {}, Quantidade disponível: {}. O valor total do estoque é R$ {:.2f}'.format(nome_produto, preco, quantidade, multiplicacao)
print(mensagem)
