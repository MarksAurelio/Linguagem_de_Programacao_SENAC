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
    