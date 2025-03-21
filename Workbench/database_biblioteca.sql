create database biblioteca;
 
use biblioteca;

create table autores(
autor_id int auto_increment primary key,
nome varchar(100) not null,
pais_origem varchar(50)
);

create table livros(
livro_id int auto_increment primary key,
titulo varchar(100) not null,
ano_publicacao int,
genero varchar(20),
fk_autor_id INT NULL,
foreign key (fk_autor_id) references autores(autor_id)
);
