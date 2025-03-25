-- n) Listar itens e indicar se a quantidade vendida é maior ou igual a 10.
/*Liste os itens vendidos, indicando se a quantidade vendida de cada item é maior ou igual a 10.
Utilize a função IF para esta distinção. As colunas presentes no resultado da consulta são ID_NF (Identificador da Nota Fiscal),
ID_ITEM (Identificador do Item), COD_PROD (Código do Produto), QUANTIDADE (Quantidade Vendida) e QUANTIDADE_STATUS (Status da Quantidade Vendida).

Os status possíveis para quantidade são "Quantidade Alta" (>= 10) e "Quantidade Baixa" (< 10).*/

    select
        ID_NF,
        ID_ITEM,
        COD_PROD,
        QUANTIDADE,
        IF (QUANTIDADE >= 10, 'Quantidade Alta', 'Quantidade Baixa') as QUANTIDADE_STATUS
    from vendas;