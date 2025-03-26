1. Crie uma base de dados Universidade com as tabelas a seguir:

        Alunos (MAT, nome, endereço, cidade)
        
        Disciplinas (COD_DISC, nome_disc, carga_hor)
        
        Professores (COD_PROF, nome, endereço, cidade)
        
        Turma (COD_DISC, COD_TURMA, COD_PROF, ANO, horário)
        COD_DISC referencia Disciplinas
        COD_PROF referencia Professores
        
        Histórico (MAT, COD_DISC, COD_TURMA, COD_PROF, ANO, frequência, nota)
        MAT referencia Alunos
        COD_DISC, COD_TURMA, COD_PROF, ANO referencia Turma

INSIRA OS SEGUINTES REGISTROS:
ALUNOS:

    (2015010101, JORGE DE ALENCAR, RUA DAS ALMAS, NATAL)
    (2015010102, JOÃO PAULO, AVENIDA RUY CARNEIRO, JOÃO PESSOA)
    (2015010103, MARINA, RUA CARROSSEL, RECIFE)
    (2015010104, MARIA DAS DORES, RUA DAS LADEIRAS, FORTALEZA)
    (2015010105, JOSUÉ EDUARDO DOS SANTOS, CENTRO, NATAL)
    (2015010106, JOSUÉLISSON CLAUDINO DOS SANTOS, CENTRO, NATAL)

DISCIPLINAS:

    (BD, BANCO DE DADOS, 100)
    (POO, PROGRAMAÇÃO COM ACESSO A BANCO DE DADOS, 100)
    (WEB, AUTORIA WEB, 50)
    (ENG, ENGENHARIA DE SOFTWARE, 80)

PROFESSORES:

    (212131, NICKERSON FERREIRA, RUA MANAÍRA, JOÃO PESSOA)
    (122135, ADORILSON BEZERRA, AVENIDA SALGADO FILHO, NATAL)
    (192011, DIEGO OLIVEIRA, AVENIDA ROBERTO FREIRE, NATAL)
    TURMA:
    (BD, 1, 212131, 2015, 11H-12H)
    (BD, 2, 212131, 2015, 13H-14H)
    (POO, 1, 192011, 2015, 08H-09H)
    (WEB, 1, 192011, 2015, 07H-08H)
    (ENG, 1, 122135, 2015, 10H-11H)

HISTÓRICO:
INSIRA VALORES PARA TODOS OS ALUNOS EM TODAS AS DISCIPLINAS

        (2015010101,'BD',1,212131,2015,5,9.00),
        (2015010101,'ENG',1,122135,2015,1,10.00),
        (2015010101,'POO',1,192011,2015,4,8.00),
        (2015010101,'WEB',1,192011,2015,2,9.00),
        (2015010102,'BD',1,212131,2015,3,7.00),
        (2015010102,'ENG',1,122135,2015,7,6.90),
        (2015010102,'POO',1,192011,2015,1,6.00),
        (2015010102,'WEB',1,192011,2015,1,9.00),
        (2015010103,'BD',1,212131,2015,10,4.00),
        (2015010103,'ENG',1,122135,2015,4,7.50),
        (2015010103,'POO',1,192011,2015,5,8.50),
        (2015010103,'WEB',1,192011,2015,2,9.50),
        (2015010104,'BD',1,212131,2015,2,7.00),
        (2015010104,'ENG',1,122135,2015,6,8.50),
        (2015010104,'POO',1,192011,2015,1,6.00),
        (2015010104,'WEB',1,192011,2015,2,8.40),
        (2015010105,'BD',1,212131,2015,4,5.50),
        (2015010105,'ENG',1,122135,2015,8,6.00),
        (2015010105,'POO',1,192011,2015,3,8.00),
        (2015010105,'WEB',1,192011,2015,2,6.00),
        (2015010106,'BD',1,212131,2015,2,4.90),
        (2015010106,'ENG',1,122135,2015,1,10.00),
        (2015010106,'POO',1,192011,2015,1,6.00),
        (2015010106,'WEB',1,192011,2015,2,7.00);

    create database universidade;

    use universidade;

    create table alunos(
        MAT int primary key not null,
        nome varchar(50) not null,
        endereco varchar(100),
        cidade varchar(50)
        );
        
    create table disciplinas(
        COD_DISC varchar(5) primary key not null,
        nome_disc varchar(50) not null,
        carga_hor int
        );
    
    create table professores(
        COD_PROF int primary key not null,
        nome varchar(50) not null,
        endereco varchar(100),
        cidade varchar(50)
        );
        
    create table turma(
        COD_TURMA int,
        COD_DISC varchar(5),
        COD_PROF int,
        ano int,
        horario varchar(20),
        primary key (COD_DISC, COD_TURMA, COD_PROF, ano),
        foreign key (COD_DISC) references disciplinas(COD_DISC),
        foreign key (COD_PROF) references professores(COD_PROF)
        );
    
    create table historico(
        MAT int,
        COD_DISC varchar(5),
        COD_TURMA int,
        COD_PROF int,
        ano int,
        frequencia int,
        nota decimal(5, 2),
        primary key (MAT, COD_DISC, COD_TURMA, COD_PROF, ano),
        foreign key (MAT) references alunos(MAT),
        foreign key (COD_DISC, COD_TURMA, COD_PROF, ano) references turma(COD_DISC, COD_TURMA, COD_PROF, ano)
        );
        
    insert into alunos(MAT, nome, endereco, cidade) values
        (2015010101, 'JORGE DE ALENCAR', 'RUA DAS ALMAS', 'NATAL'),
        (2015010102, 'JOÃO PAULO', 'AVENIDA RUY CARNEIRO', 'JOÃO PESSOA'),
        (2015010103, 'MARINA', 'RUA CARROSSEL', 'RECIFE'),
        (2015010104, 'MARIA DAS DORES', 'RUA DAS LADEIRAS', 'FORTALEZA'),
        (2015010105, 'JOSUÉ EDUARDO DOS SANTOS', 'CENTRO', 'NATAL'),
        (2015010106, 'JOSUÉLISSON CLAUDINO DOS SANTOS', 'CENTRO', 'NATAL');

    insert into disciplinas(COD_DISC, nome_disc, carga_hor) values
        ('BD', 'BANCO DE DADOS', 100),
        ('POO', 'PROGRAMAÇÃO COM ACESSO A BANCO DE DADOS', 100),
        ('WEB', 'AUTORIA WEB', 50),
        ('ENG', 'ENGENHARIA DE SOFTWARE', 80);

    insert into professores(COD_PROF, nome, endereco, cidade) values
        (212131, 'NICKERSON FERREIRA', 'RUA MANAÍRA', 'JOÃO PESSOA'),
        (122135, 'ADORILSON BEZERRA', 'AVENIDA SALGADO FILHO', 'NATAL'),
        (192011, 'DIEGO OLIVEIRA', 'AVENIDA ROBERTO FREIRE', 'NATAL');

    insert into turma(COD_DISC, COD_TURMA, COD_PROF, ANO, horario) values
        ('BD', 1, 212131, 2015, '11H-12H'),
        ('BD', 2, 212131, 2015, '13H-14H'),
        ('POO', 1, 192011, 2015, '08H-09H'),
        ('WEB', 1, 192011, 2015, '07H-08H'),
        ('ENG', 1, 122135, 2015, '10H-11H');

    insert into historico(MAT, COD_DISC, COD_TURMA, COD_PROF, ANO, frequencia, nota) values
        (2015010101,'BD',1,212131,2015,5,9.00),
        (2015010101,'ENG',1,122135,2015,1,10.00),
        (2015010101,'POO',1,192011,2015,4,8.00),
        (2015010101,'WEB',1,192011,2015,2,9.00),
        (2015010102,'BD',1,212131,2015,3,7.00),
        (2015010102,'ENG',1,122135,2015,7,6.90),
        (2015010102,'POO',1,192011,2015,1,6.00),
        (2015010102,'WEB',1,192011,2015,1,9.00),
        (2015010103,'BD',1,212131,2015,10,4.00),
        (2015010103,'ENG',1,122135,2015,4,7.50),
        (2015010103,'POO',1,192011,2015,5,8.50),
        (2015010103,'WEB',1,192011,2015,2,9.50),
        (2015010104,'BD',1,212131,2015,2,7.00),
        (2015010104,'ENG',1,122135,2015,6,8.50),
        (2015010104,'POO',1,192011,2015,1,6.00),
        (2015010104,'WEB',1,192011,2015,2,8.40),
        (2015010105,'BD',1,212131,2015,4,5.50),
        (2015010105,'ENG',1,122135,2015,8,6.00),
        (2015010105,'POO',1,192011,2015,3,8.00),
        (2015010105,'WEB',1,192011,2015,2,6.00),
        (2015010106,'BD',1,212131,2015,2,4.90),
        (2015010106,'ENG',1,122135,2015,1,10.00),
        (2015010106,'POO',1,192011,2015,1,6.00),
        (2015010106,'WEB',1,192011,2015,2,7.00);
        
/*a) Encontre a MAT dos alunos com nota em BD em 2015 menor que 5 (obs: BD =
código da disciplina).*/

    SELECT 
        MAT
    from historico h
    join disciplinas d on h.COD_DISC = d.COD_DISC
    where d.COD_DISC = 'BD'
    and h.ano = 2015
    and h.nota < 5;
    
/*b) Encontre a MAT e calcule a média das notas dos alunos na disciplina de POO
em 2015.*/

    select 
        MAT,
        round(avg(h.nota)) as MEDIA_NOTAS
    from historico h
    join disciplinas d on h.COD_DISC = d.COD_DISC
    where d.COD_DISC = 'POO'
    and h.ano = 2015
    group by h.MAT;

/*c) Encontre a MAT e calcule a média das notas dos alunos na disciplina de POO
em 2015 e que esta média seja superior a 6.*/

    select 
        MAT,
        round(avg(h.nota)) as MEDIA_NOTAS
    from historico h
    join disciplinas d on h.COD_DISC = d.COD_DISC
    where d.COD_DISC = 'POO'
    and h.ano = 2015
    and nota > 6
    group by h.MAT;

/*d) Encontre quantos alunos não são de Natal.*/

    select
        count(MAT) as QTD_ALUNOS
    from alunos
    where cidade != 'NATAL';
