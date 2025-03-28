/*EXERCÍCIOS – PARTE 03

SUBCONSULTA COM MAIS DE UMA TABELA

Exemplo
-- Fazer um relatório para mostrar o nome dos alunos da disciplina de
banco de dados
SELECT NOME FROM ALUNO WHERE MAT IN (SELECT MAT FROM
HISTORICO WHERE COD_DISC = 'BD');

/*1. Fazer um relatório para mostrar os dados dos alunos que tiraram
nota = 10.*/

    select 
        nome
    from alunos
    where MAT in (select MAT from historico where nota = 10);

/*2. Fazer um relatório que mostre todos os dados do aluno e do
histórico, quando a nota for maior que 7.*/

    select 
        nome
    from alunos
    where MAT in (select MAT from historico where nota > 7);

/*3. Fazer um relatório que mostre o nome dos professores e a
quantidade de turmas que eles ministram aula, somente para
quando a quantidade de turmas for maior que 1.*/

    select
        nome,
        count(COD_TURMA) as QTD_TURMAS
    from professores p
    join turma t on p.COD_PROF = t.COD_PROF 
    group by nome
    having count(COD_TURMA) > 1;

/*4. Fazer um relatório para mostrar o nome dos alunos, o código da
disciplina, a nota e a média geral, mostrar somente os dados dos
alunos que tiraram nota com valor maior ou igual a média geral.*/

    select
        MAT,
        COD_DISC,
        nota as MEDIA_GERAL
    from historico h
    where nota >= (select avg(nota) from historico where MAT = h.MAT)
    group by MAT, COD_DISC, nota;