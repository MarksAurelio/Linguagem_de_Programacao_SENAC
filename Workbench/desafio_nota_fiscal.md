-- 1. Crie, no seu banco de dados, a tabela abaixo, insira os valores apresentados e em
-- seguida escreva as consultas solicitadas abaixo.
-- OBS: Os valores em branco devem ser nulos no banco de dados.

    create database nota_fiscal;

    use nota_fiscal;

    create table vendas(

	ID_NF int not null, 
    ID_ITEM int not null,
    COD_PROD int not null,
    VALOR_UNIT decimal (10,2),
    QUANTIDADE int,
    DESCONTO int,
    primary key (ID_NF, ID_ITEM)
    );
    
    insert into vendas(ID_NF, ID_ITEM, COD_PROD, VALOR_UNIT, QUANTIDADE, DESCONTO) values

    (1, 1, 1, 25.00, 10, 5),
    (1, 2, 2, 13.50, 3, null),
    (1, 3, 3, 15.00, 2, null),
    (1, 4, 4, 10.00, 1, NULL),
    (1, 5, 5, 30.00, 1, NULL),
    (2, 1, 3, 15.00, 4, NULL),
    (2, 2, 4, 10.00, 5, NULL),
    (2, 3, 5, 30.00, 7, NULL),
    (3, 1, 1, 25.00, 5, NULL),
    (3, 2, 4, 10.00, 4, NULL),
    (3, 3, 5, 30.00, 5, NULL),
    (3, 4, 2, 13.50, 7, NULL),
    (4, 1, 5, 30.00, 10, 15),
    (4, 2, 4, 10.00, 12, 5),
    (4, 3, 1, 25.00, 13, 5),
    (4, 4, 2, 13.50, 15, 5),
    (5, 1, 3, 15.00, 3, NULL),
    (5, 2, 5, 30.00, 6, NULL),
    (6, 1, 1, 25.00, 22, 15),
    (6, 2, 3, 15.00, 25, 20),
    (7, 1, 1, 25.00, 10, 3),
    (7, 2, 2, 13.50, 10, 4),
    (7, 3, 3, 15.00, 10, 4),
    (7, 4, 5, 30.00, 10, 1);

-- a) Pesquise os itens que foram vendidos sem desconto. As colunas presentes no resultado
-- da consulta são: ID_NF, ID_ITEM, COD_PROD E VALOR_UNIT.

    select 
        ID_NF, 
        ID_ITEM, 
        COD_PROD, 
        VALOR_UNIT
    from vendas
    where desconto is null or desconto = 0;

-- b) Pesquise os itens que foram vendidos com desconto. As colunas presentes no resultado
-- da consulta são: ID_NF, ID_ITEM, COD_PROD, VALOR_UNIT E O VALOR
-- VENDIDO. OBS: O valor vendido é igual ao VALOR_UNIT -
-- (VALOR_UNIT*(DESCONTO/100)).

    select 
        ID_NF, 
        ID_ITEM, 
        COD_PROD, 
        VALOR_UNIT, round(VALOR_UNIT - (VALOR_UNIT*(DESCONTO/100)),2 AS VALOR_VENDIDO
    from vendas
    where desconto > 0;

-- c) Altere o valor do desconto (para zero) de todos os registros onde este campo é nulo.

    update vendas
    set DESCONTO = 0
    where ID_NF and ID_ITEM = DESCONTO is null;
    select * from vendas;

-- d) Pesquise os itens que foram vendidos. As colunas presentes no resultado da consulta
-- são: ID_NF, ID_ITEM, COD_PROD, VALOR_UNIT, VALOR_TOTAL, DESCONTO,
-- VALOR_VENDIDO. OBS: O VALOR_TOTAL é obtido pela fórmula: QUANTIDADE *
-- VALOR_UNIT. O VALOR_VENDIDO é igual a VALOR_UNIT - (VALOR_UNIT*(DESCONTO/100)).

    select ID_NF, 
        ID_ITEM, 
        COD_PROD, 
        VALOR_UNIT, 
        QUANTIDADE * VALOR_UNIT as VALOR_TOTAL,
        DESCONTO,
        round(VALOR_UNIT - (VALOR_UNIT * (DESCONTO / 100)),2) as VALOR_VENDIDO
    from vendas;
    
-- e) Pesquise o valor total das NF e ordene o resultado do maior valor para o menor. As
-- colunas presentes no resultado da consulta são: ID_NF, VALOR_TOTAL. OBS: O
-- VALOR_TOTAL é obtido pela fórmula: ∑ QUANTIDADE * VALOR_UNIT. Agrupe o
-- resultado da consulta por ID_NF.

    select
        ID_NF,
        sum(QUANTIDADE * VALOR_UNIT) as VALOR_TOTAL
    from vendas
    group by ID_NF
    order by VALOR_TOTAL desc;
    
-- f) Pesquise o valor vendido das NF e ordene o resultado do maior valor para o menor. As
-- colunas presentes no resultado da consulta são: ID_NF, VALOR_VENDIDO. OBS: O
-- VALOR_TOTAL é obtido pela fórmula: ∑ QUANTIDADE * VALOR_UNIT. O
-- VALOR_VENDIDO é igual a ∑ VALOR_UNIT - (VALOR_UNIT*(DESCONTO/100)). Agrupe o
-- resultado da consulta por ID_NF.
 
    select
        ID_NF,
        sum(VALOR_UNIT - (VALOR_UNIT*(DESCONTO/100))) as VALOR_VENDIDO
    from vendas
    group by ID_NF
    order by VALOR_VENDIDO desc;

-- g) Consulte o produto que mais vendeu no geral. As colunas presentes no resultado da
-- consulta são: COD_PROD, QUANTIDADE. Agrupe o resultado da consulta por
-- COD_PROD.

    select 
        COD_PROD, 
        sum(QUANTIDADE) as QUANTIDADE
    from vendas
    group by COD_PROD
    order by QUANTIDADE desc
    limit 1;

-- h) Consulte as NF que foram vendidas mais de 10 unidades de pelo menos um produto. As
-- colunas presentes no resultado da consulta são: ID_NF, COD_PROD, QUANTIDADE.
-- Agrupe o resultado da consulta por ID_NF, COD_PROD.

    select 
        ID_NF, 
        COD_PROD, 
        sum(QUANTIDADE) as QUANTIDADE
    from vendas
    where QUANTIDADE > 10
    group by ID_NF, COD_PROD;

-- i) Pesquise o valor total das NF, onde esse valor seja maior que 500, e ordene o resultado
-- do maior valor para o menor. As colunas presentes no resultado da consulta são: ID_NF,
-- VALOR_TOTAL. OBS: O VALOR_TOTAL é obtido pela fórmula: ∑ QUANTIDADE *
-- VALOR_UNIT. Agrupe o resultado da consulta por ID_NF.

    select
        ID_NF,
        sum(QUANTIDADE * VALOR_UNIT) as VALOR_TOTAL
    from vendas
    group by ID_NF
    having sum(QUANTIDADE * VALOR_UNIT) > 500
    order by VALOR_TOTAL desc;

-- j) Qual o valor médio dos descontos dados por produto. As colunas presentes no resultado
-- da consulta são: COD_PROD, MEDIA. Agrupe o resultado da consulta por COD_PROD.

    select 
        COD_PROD,
        avg(DESCONTO) as MEDIA
    from vendas
    group by COD_PROD;

-- k) Qual o menor, maior e o valor médio dos descontos dados por produto. As colunas
-- presentes no resultado da consulta são: COD_PROD, MENOR, MAIOR, MEDIA. Agrupe o
-- resultado da consulta por COD_PROD.

    select 
        COD_PROD,
        min(DESCONTO) as MENOR,
        max(DESCONTO) as MAIOR,
        avg(DESCONTO) AS MEDIA
    from vendas
    group by COD_PROD;

-- l) Quais as NF que possuem mais de 3 itens vendidos. As colunas presentes no resultado
-- da consulta são: ID_NF, QTD_ITENS. OBS:: NÃO ESTÁ RELACIONADO A QUANTIDADE
-- VENDIDA DO ITEM E SIM A QUANTIDADE DE ITENS POR NOTA FISCAL. Agrupe o
-- resultado da consulta por ID_NF.

    select
        ID_NF,
        count(ID_ITEM) as QTS_ITENS
    from vendas
    group by ID_NF
    having count(ID_ITEM) > 3;

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
        IF(DESCONTO < (select avg(DESCONTO)from vendas) and DESCONTO > 0, 'Desconto Abaixo da Média', 'Sem desconto'))) as DESCONTO_STATUS
    from vendas;
