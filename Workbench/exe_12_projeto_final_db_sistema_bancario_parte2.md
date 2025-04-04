use sistema_bancario;

  /* Instruções para o Projeto Final de Banco de Dados – MySQL*/

-- 3. Consultas

/*a) Liste todos os clientes com suas contas e saldos totais*/

    select 
        cli.nome as NOME_CLIENTE,
        con.conta_id as CONTA_CLIENTE,
        con.saldo as SALDO_CLIENTE
    from clientes cli, contas con;
    
/*b) Mostre o saldo médio por tipo de conta*/

    select
        round(avg(con.saldo)) as SALDO_MEDIO,
        con.conta_id as CONTA_CLIENTE,
        con.tipo_conta as TIPO_CONTA
    from contas con
    group by conta_id;

/*c) Liste todas as transações de uma conta específica (use o ID 1 como
exemplo)*/

    select
        cli.cliente_id as ID_CLIENTE,
        conta_origem_id as CONTA_ORIGEM,
        conta_destino_id as CONTA_DESTINO,
        cli.nome as NOME_CLIENTE,
        t.tipo_transacao as TIPO_TRANSACAO
    from transacoes t
    join clientes cli on t.conta_destino_id = cli.cliente_id
    where conta_origem_id = 1 or conta_destino_id = 1
    union
    select
        cli.cliente_id as ID_CLIENTE,
        conta_origem_id as CONTA_ORIGEM,
        conta_destino_id as CONTA_DESTINO,
        cli.nome as NOME_CLIENTE,
        t.tipo_transacao as TIPO_TRANSACAO
    from transacoes t
    join clientes cli on t.conta_destino_id = cli.cliente_id
    where conta_destino_id = 1;
    
/*d) Calcule o total de transações por tipo no último mês*/

/*e) Liste os clientes que têm mais de uma conta*/

/*f) Mostre o total de empréstimos por agência*/

/*g) Liste os empréstimos ativos com parcelas em atraso (considerando que hoje
é a data (Questão extra)*/
