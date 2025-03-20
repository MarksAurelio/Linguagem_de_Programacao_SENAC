 create database aluno;
 
 use aluno;
 
 create table aluno(
	pk_cod_aluno int auto_increment primary key,
    nome varchar(60) not null
    
    );
create table trabalho(
	pk_cod_trabalho int auto_increment primary key,
    descricao varchar(50) not null,
    fk_cod_aluno int,
    foreign key (fk_cod_aluno) references aluno(pk_cod_aluno)
);
