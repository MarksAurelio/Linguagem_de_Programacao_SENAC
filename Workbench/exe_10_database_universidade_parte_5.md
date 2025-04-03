/*Lista 1: Exercícios com INNER JOIN
/*1. Liste o nome dos alunos, a disciplina e a nota para alunos com nota > 7 em 2015.*/

    select
        a.nome as NOME_ALUNO,
        d.nome_disc as NOME_DISC,
        h.nota as NOTA,
        h.ano as ANO
    from historico h
    join alunos a on h.MAT = a.MAT
    join disciplinas d on h.COD_DISC = d.COD_DISC
    where h.nota > 7 
    and h.ano = 2015
    group by 1, 2, 3;
        
/*2. Mostre professores, disciplinas e horários das turmas de 2015.*/

    select 
        p.nome as NOME_PROF,
        d.nome_disc as NOME_DISC,
        t.horario as HORARIO_TURMA,
        h.ano as ANO
    from historico h
    join professores p on h.COD_PROF = p.COD_PROF
    join disciplinas d on h.COD_DISC = d.COD_DISC
    join turma t on h.COD_TURMA = t.COD_TURMA
    where h.ano = 2015 
    group by 1, 2, 3;

/*3. Encontre alunos que estudaram com o professor "Nickerson Ferreira".*/

    select
        a.nome as NOME_ALUNO,
        p.nome as NOME_PROF
    from historico h
    join alunos a on h.MAT = a.MAT
    join professores p on h.COD_PROF
    where p.nome = 'NICKERSON FERREIRA'
    group by 1, 2;

/*4. Calcule a média de notas por disciplina e cidade de origem, ordenando por disciplina e média.*/

    select
        d.nome_disc as NOME_DISC,
        a.cidade as CIDADE_ORIGEM,
        round(avg(h.nota)) as MEDIA_NOTA
    from historico h
    join alunos a on h.MAT = a.MAT
    join disciplinas d on h.COD_DISC = d.COD_DISC
    group by 1, 2
    order by avg(h.nota);

/*5. Liste professores que ministraram disciplinas com carga horária > 70 horas.*/

    select 
        p.nome as NOME_PROF,
        d.nome_disc as NOME_DISC,
        d.carga_hor as CARGA_HORARIA
    from turma t
    join professores p on t.COD_PROF = p.COD_PROF
    join disciplinas d on t.COD_DISC = d.COD_DISC
    where d.carga_hor > 70
    group by 1, 2, 3;

/*Lista 2: Exercícios com LEFT JOIN*/

/*1. Liste todos os alunos e suas disciplinas (incluindo quem não cursou nenhuma).*/

    select 
        a.nome as NOME_ALUNO,
        d.nome_disc as NOME_DISC
    from alunos a
    left join historico h on a.MAT = h.MAT
    left join turma t on h.COD_TURMA = h.COD_TURMA
    left join disciplinas d on t.COD_DISC = d.COD_DISC
    group by 1, 2;

/*2. Mostre todos os professores e as disciplinas que ministraram (incluindo quem
não ministrou).*/

    select
        p.nome as NOME_PROF,
        d.nome_disc as NOME_DISC
    from professores p
    left join historico h on h.COD_PROF = p.COD_PROF
    left join disciplinas d on h.COD_DISC = d.COD_DISC
    group by 1 ,2
    order by 1, 2;

/*3. Liste todas as disciplinas e alunos que as cursaram (incluindo disciplinas sem
alunos).*/

    select 
        d.nome_disc as NOME_DISC,
        a.nome as NOME_ALUNO
    from disciplinas d
    left join historico h on h.COD_DISC = d.COD_DISC
    left join alunos a on h.MAT = a.MAT
    group by 1, 2;

/*Lista 3: Exercícios com RIGHT JOIN*/

/*1. Mostre todas as disciplinas e seus professores (incluindo disciplinas não
ministradas).*/

    select
        p.nome as NOME_PROF,
        d.nome_disc as NOME_DISC
        
    from professores p
    right join historico h on h.COD_PROF = p.COD_PROF
    right join disciplinas d on h.COD_DISC = d.COD_DISC
    group by 1, 2;

/*2. Liste registros de histórico com dados completos dos alunos (incluindo
históricos sem aluno, se houver).*/

    select 
        a.MAT as MATRI_ALUNO,
        a.nome as NOME_ALUNO,
        a.endereco as END_ALUNO,
        a.cidade as CIDADE_ALUNO
    from historico h
    right join alunos a on h.MAT = a.MAT
    group by 1, 2;
    
/*Lista 4: Exercícios com FULL OUTER JOIN (simulado)*/

/*1. Liste todos os alunos e todas as disciplinas, mostrando relações existentes.*/

    select
        a.nome as NOME_ALUNO,
        d.nome_disc as NOME_DISC
    from alunos a
    left join historico h on h.MAT = a.MAT
    left join disciplinas d on h.COD_DISC = d.COD_DISC
    union
    select
        a.nome as NOME_ALUNO,
        d.nome_disc as NOME_DISC
    from alunos a
    right join historico h on h.MAT = a.MAT
    right join disciplinas d on h.COD_DISC = d.COD_DISC
    group by 1, 2;

/*Lista 5: Exercícios com CROSS JOIN*/
/*1. Crie uma lista de todas as combinações possíveis entre alunos e disciplinas.*/
    select
        a.nome as NOME_ALUNO,
        d.nome_disc as NOME_DISC
    from alunos a
    cross join disciplinas d;

/*Lista 6: Exercícios com SELF JOIN*/
/*1. Encontre alunos que moram na mesma cidade (pares distintos).*/

    select
        a.MAT as MAT_ALUNO_1, 
        a.nome as NOME_ALUNO_1,
        a2.MAT as MAT_ALUNO_2,
        a2.nome as NOME_ALUNO_2,
        a.cidade as CIDADE_ALUNO
    from alunos a
    join alunos a2 on a.cidade = a2.cidade 
    and a.MAT < a2.MAT; -- evitando duplicações (se o aluno A e B moram na mesma cidade, sera listado o aluno A e B, mas não o aluno B e A).

/*Lista 7: Exercícios Combinados (Múltiplos JOINs)*/

/*1. Liste alunos, disciplinas cursadas e professores (incluindo alunos sem
disciplinas).*/

    select 
        a.MAT as MAT_ALUNO,
        a.nome as NOME_ALUNO,
        d.COD_DISC as COD_DISC,
        d.nome_disc as NOME_DISC,
        p.COD_PROF as COD_PROF,
        p.nome as NOME_PROF
    from historico h
    left join alunos a on h.MAT = a.MAT
    left join disciplinas d on h.COD_DISC = d.COD_DISC
    left join professores p on h.COD_PROF = p.COD_PROF
    group by 1, 2, 3, 4, 5;

    select 
        a.MAT as MAT_ALUNO,
        a.nome as NOME_ALUNO,
        d.COD_DISC as COD_DISC,
        d.nome_disc as NOME_DISC,
        p.COD_PROF as COD_PROF,
        p.nome as NOME_PROF
    from historico h
    right join alunos a on h.MAT = a.MAT
    right join disciplinas d on h.COD_DISC = d.COD_DISC
    right join professores p on h.COD_PROF = p.COD_PROF
    group by 1, 2, 3, 4, 5;

    select 
        a.MAT as MAT_ALUNO,
        a.nome as NOME_ALUNO,
        d.COD_DISC as COD_DISC,
        d.nome_disc as NOME_DISC,
        p.COD_PROF as COD_PROF,
        p.nome as NOME_PROF
    from historico h
    left join alunos a on h.MAT = a.MAT
    left join disciplinas d on h.COD_DISC = d.COD_DISC
    left join professores p on h.COD_PROF = p.COD_PROF
    union
    select 
        a.MAT as MAT_ALUNO,
        a.nome as NOME_ALUNO,
        d.COD_DISC as COD_DISC,
        d.nome_disc as NOME_DISC,
        p.COD_PROF as COD_PROF,
        p.nome as NOME_PROF
    from historico h
    right join alunos a on h.MAT = a.MAT
    right join disciplinas d on h.COD_DISC = d.COD_DISC
    right join professores p on h.COD_PROF = p.COD_PROF
    group by 1, 2, 3, 4, 5, 6;

/*2. Mostre todas as disciplinas, professores que poderiam ministrá-las e turmas já
formadas.*/

    select 
        d.nome_disc as NOME_DISC,
        p.nome as NOME_PROF,
        t.COD_TURMA as COD_TURMA
    from disciplinas d
    cross join professores p
    left join historico h on h.COD_DISC = d.COD_DISC and h.COD_PROF = p.COD_PROF
    left join turma t on h.COD_TURMA = t.COD_TURMA
    group by 1, 2, 3;

    /*3. Liste todas as combinações professor-disciplina, marcando quais já ocorreram.*/

    select
        p.nome as NOME_PROF,
        d.nome_disc as NOME_DISC

/*Como usar:
1. Para soluções, utilize a estrutura do banco "Universidade" definida
anteriormente.
2. Dica: Em MySQL, substitua FULL OUTER JOIN por UNION de LEFT e RIGHT
JOIN.*/