create database cliente;

use cliente;

create table cliente(
	id_cliente int auto_increment primary key,
    nome_cliente varchar(50) not null
);

create table pedido(
	id_pedido int auto_increment primary key,
    descricao_pedido varchar(50) not null,
    fk_id_cliente int,
    foreign key (fk_id_cliente) references cliente(id_cliente)
);
