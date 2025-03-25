-- O) Listar itens e indicar se o desconto aplicado é maior, igual ou menor que a média geral dos descontos.

/*Liste os itens vendidos, indicando se o desconto aplicado em cada item é maior, igual ou menor que a média geral dos descontos.
Utilize a função IF para esta distinção. As colunas presentes no resultado da consulta são ID_NF (Identificador da Nota Fiscal),
ID_ITEM (Identificador do Item), COD_PROD (Código do Produto), DESCONTO (Percentual de Desconto) e DESCONTO_STATUS (Status do Desconto).

Os status possíveis para o desconto são "Desconto Acima da Média", "Desconto Médio" e "Desconto Abaixo da Média". */

    select
        ID_NF,
        ID_ITEM,
        COD_PROD,
        DESCONTO,
        IF(DESCONTO > (select avg(DESCONTO)from vendas), 'Desconto Acima da Média',
        IF(DESCONTO = (select avg(DESCONTO)from vendas), 'Desconto Médio',
        IF(DESCONTO < (select avg(DESCONTO)from vendas), 'Desconto Abaixo da Média', 'Sem desconto'))) as DESCONTO_STATUS
    from vendas;