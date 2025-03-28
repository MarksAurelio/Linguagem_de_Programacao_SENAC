/*Exercícios de SQL com INNER JOIN
(Banco de Dados: Universidade)

/*1. Liste o nome dos alunos, a disciplina e a nota, para todos os alunos que tiveram nota
maior que 7 em qualquer disciplina no ano de 2015.*/

    select
        a.nome,
        h.MAT,
        h.COD_DISC,
        h.nota,
        h.ano
    from historico h
    join disciplinas d on d.COD_DISC = h.COD_DISC
    join alunos a on a.MAT = h.MAT
    where h.nota > 7 and ano = 2015
    group by h.MAT, h.COD_DISC, h.nota, h.ano;

/*2. Mostre o nome do professor, o nome da disciplina e o horário das turmas que cada
professor ministrou em 2015.*/

    select 
        p.nome,
        d.nome_disc,
        t.horario,
        t.ano
    from professores p
    join turma t on p.COD_PROF = t.COD_PROF
    join disciplinas d on t.COD_DISC = d.COD_DISC
    where t.ano = 2015
    group by p.nome, d.nome_disc, t.horario;
	

/*3. Encontre todos os alunos que estudaram com o professor Nickerson Ferreira,
mostrando o nome do aluno, a disciplina e o ano.*/

    select
        p.nome as NOME_DISC,
        a.nome as NOME_ALUNO,
        d.nome_disc,
        t.ano
    from alunos a
    join historico h on a.MAT = h.MAT
    join disciplinas d on h.COD_DISC = d.COD_DISC
    join turma t on d.COD_DISC = t.COD_DISC
    join professores p on t.COD_PROF = p.COD_PROF
    where p.nome = 'NICKERSON FERREIRA'
    group by p.nome, a.nome, d.nome_disc, t.ano;

/*4. Liste os alunos de Natal que tiveram frequência menor que 5 em qualquer disciplina,
mostrando o nome do aluno, nome da disciplina e a frequência.*/

    select
        a.nome as NOME_ALUNO,
        d.NOME_DISC,
        h.frequencia
    from historico h
    join alunos a on h.MAT = a.MAT
    join disciplinas d on h.COD_DISC = d.COD_DISC
    where h.frequencia < 5
    group by a.nome, d.NOME_DISC, h.frequencia;

/*5. Mostre a média de notas por disciplina para cada cidade de origem dos alunos,
ordenado pela disciplina e depois pela média decrescente.*/

    select
        d.nome_disc,
        avg(nota) as MEDIA_NOTAS,
        a.cidade as CIDADE_ALUNO
    from historico h
    join disciplinas d on h.COD_DISC = d.COD_DISC
    join alunos a on h.MAT = a.MAT
    group by CIDADE_ALUNO, d.nome_disc
    order by CIDADE_ALUNO, avg(nota) desc;
        
/*6. Encontre os professores que ministraram disciplinas com carga horária superior a 70
horas, mostrando o nome do professor e o nome da disciplina.*/

/*7. Liste todos os alunos que tiveram nota acima da média em Banco de Dados,
mostrando o nome do aluno e a nota.*/

/*8. Mostre a quantidade de alunos por professor em 2015, ordenado pela quantidade em
ordem decrescente.*/

/*9. Encontre os alunos que cursaram mais de uma disciplina com o mesmo professor,
mostrando o nome do aluno, nome do professor e a quantidade de disciplinas.*/

/*10. Liste as disciplinas que tiveram alunos de todas as cidades representadas no banco
de dados, mostrando o nome da disciplina.*/

/*Observações:
• Todas as consultas devem utilizar INNER JOIN para relacionar as tabelas.
• Considere a estrutura do banco de dados "Universidade" conforme definido
anteriormente.*/