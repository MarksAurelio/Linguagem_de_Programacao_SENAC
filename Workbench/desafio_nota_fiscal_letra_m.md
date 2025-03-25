-- m) Identificação de Itens com e sem Desconto Utilizando IF:

/* Identifique os itens vendidos, indicando se cada item possui ou não desconto. Utilize a função IF para esta distinção.
As colunas presentes no resultado da consulta são ID_NF (Identificador da Nota Fiscal), ID_ITEM (Identificador do Item),
COD_PROD (Código do Produto), VALOR_UNIT (Valor Unitário do Produto),
QUANTIDADE (Quantidade Vendida), STATUS_DESCONTO (Indicação de Desconto) e
VALOR_VENDIDO (Valor Vendido Considerando o Desconto, se aplicável).*/

    select
        ID_NF,
        ID_ITEM,
        COD_PROD,
        VALOR_UNIT,
        QUANTIDADE,
        IF (DESCONTO > 0, 'COM DESCONTO', 'SEM DESCONTO') as STATUS_DESCONTO,
        (VALOR_UNIT * QUANTIDADE) as VALOR_VENDIDO
    from vendas;
