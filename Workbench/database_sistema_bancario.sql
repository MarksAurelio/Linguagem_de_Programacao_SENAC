Instruções para o Projeto Final de Banco de Dados – MySQL

Objetivo do Projeto
Você deverá criar um sistema bancário completo no MySQL, incluindo:
1. Criação do banco de dados e tabelas
2. Inserção de dados de exemplo
3. Consultas SQL para extrair informações importantes
4. Normalização de dados - Até a 3° forma normal (Atividade Extra)
5. Triggers para automatizar processos (Atividade Extra)

Requisitos Técnicos
• Todos os scripts devem ser compatíveis com MySQL
• Use o caractere ; para encerrar cada comando SQL
• Comente seu código com -- para linhas únicas ou /* */ para blocos

1. Especificações das Tabelas
a. Tabela Clientes

Armazena informações dos clientes do banco:
• cliente_id (INT, PK, AUTO_INCREMENT): Identificador único
• nome : Nome completo do cliente
• cpf : CPF formatado (ex: 123.456.789-01)
• data_nascimento (DATE): Data de nascimento
• telefone Telefone com DDD
• email E-mail do cliente
• endereco Endereço completo
• data_cadastro (DATETIME): Data/hora do cadastro (default
CURRENT_TIMESTAMP)
-- Inserir Clientes
INSERT INTO Clientes (nome, cpf, data_nascimento, telefone, email, endereco)
VALUES
('João Silva', '123.456.789-01', '1980-05-15', '(11) 98765-4321',
'joao@email.com', 'Rua A, 100 - Centro'),

b. Tabela Agencias
Armazena as agências do banco:
• agencia_id (INT, PK, AUTO_INCREMENT): Identificador único
• nome : Nome da agência
• endereco : Endereço completo
• telefone : Telefone da agência

-- Inserir Agências
INSERT INTO Agencias (nome, endereco, telefone) VALUES
('Agência Centro', 'Rua Principal, 123 - Centro', '(11) 1234-5678')

c. Tabela Contas
Armazena as contas bancárias:
• conta_id (INT, PK, AUTO_INCREMENT): Identificador único
• cliente_id : Referência ao cliente
• agencia_id : Referência à agência
• tipo_conta (ENUM): 'Corrente', 'Poupança' ou 'Salário'
• saldo : Saldo atual (default 0.00)
• data_abertura (DATE): Data de abertura da conta
• status (ENUM): 'Ativa', 'Inativa' ou 'Bloqueada' (default 'Ativa')

-- Inserir Contas
INSERT INTO Contas (cliente_id, agencia_id, tipo_conta, saldo, data_abertura, status)
VALUES
(1, 1, 'Corrente', 5000.00, '2020-01-10', 'Ativa')

d. Tabela Transacoes

Registra todas as movimentações financeiras:
• transacao_id (INT, PK, AUTO_INCREMENT): Identificador único
• conta_origem_id (INT, FK, NULL): Conta de origem (NULL para depósitos)
• conta_destino_id (INT, FK, NULL): Conta de destino (NULL para saques)
• tipo_transacao (ENUM): 'Depósito', 'Saque', 'Transferência', 'Pagamento'
• valor Valor da transação
• data_transacao (DATETIME): Data/hora (default CURRENT_TIMESTAMP)
• descricao : Descrição opcional

-- Inserir Transações
INSERT INTO Transacoes (conta_origem_id, conta_destino_id, tipo_transacao, valor,
descricao) VALUES
(1, NULL, 'Depósito', 1000.00, 'Depósito inicial'),
(NULL, 2, 'Depósito', 2000.00, 'Depósito inicial')

e. Tabela Emprestimos
Registra os empréstimos contratados:
• emprestimo_id (INT, PK, AUTO_INCREMENT): Identificador único
• conta_id (INT, FK): Conta associada ao empréstimo
• valor (DECIMAL(15,2)): Valor total do empréstimo
• taxa_juros (DECIMAL(5,2)): Taxa de juros mensal
• parcelas (INT): Número total de parcelas
• valor_parcela (DECIMAL(15,2)): Valor de cada parcela
• data_contratacao (DATE): Data de contratação
• status (ENUM): 'Ativo', 'Quitado', 'Inadimplente' (default 'Ativo')

-- Inserir Empréstimos
INSERT INTO Emprestimos (conta_id, valor, taxa_juros, parcelas, valor_parcela,
data_contratacao) VALUES
(1, 10000.00, 1.5, 12, 916.67, '2022-01-15')

f. Tabela PagamentosEmprestimos
Registra os pagamentos de empréstimos:
• pagamento_id (INT, PK, AUTO_INCREMENT): Identificador único
• emprestimo_id (INT, FK): Empréstimo associado
• numero_parcela : Número da parcela
• valor_pago : Valor efetivamente pago
• data_pagamento : Data do pagamento
•
-- Inserir Pagamentos de Empréstimos
INSERT INTO PagamentosEmprestimos (emprestimo_id, numero_parcela, valor_pago,
data_pagamento) VALUES
(1, 1, 916.67, '2022-02-15')
create database sistema_bancario;

use sistema_bancario;

create table clientes(
	cliente_id int primary key auto_increment,
    nome varchar(200),
    cpf varchar(50),
    data_nascimento date,
    telefone varchar(20),
    email varchar(100),
    endereco varchar(100),
    data_cadastro datetime default current_timestamp
    );

    -- Inserir Clientes
    
    insert into clientes (nome, cpf, data_nascimento, telefone, email, endereco) values
	('João da Silva', '12345678901', '1980-05-15', 11999999999, 'joao.silva@email.com', 'Rua A, 123, São Paulo, SP'),
	('Maria Souza', '98765432109', '1992-10-20', 21988888888, 'maria.souza@email.com', 'Avenida B, 456, Rio de Janeiro, RJ'),
	('Carlos Oliveira', '56789012345', '1975-03-08', 31977777777, 'carlos.oliveira@email.com', 'Rua C, 789, Belo Horizonte, MG'),
	('Ana Pereira', '43210987654', '2001-12-01', 41966666666, 'ana.pereira@email.com', 'Avenida D, 1011, Curitiba, PR'),
	('Pedro Rodrigues', '89012345678', '1988-07-25', 51955555555, 'pedro.rodrigues@email.com', 'Rua E, 1213, Porto Alegre, RS');
    
create table agencias(
	agencia_id int primary key auto_increment,
    nome varchar(200),
    endereco varchar(100),
    telefone varchar(20)
    );
    
    -- Inserir Agências
    
    insert into agencias(nome, endereco, telefone) values
    ('Agência Central', 'Rua Principal, 100, São Paulo, SP', 1122223333),
	('Agência Filial A', 'Avenida Secundária, 200, Rio de Janeiro, RJ', 2133334444),
	('Agência Filial B', 'Rua Lateral, 300, Belo Horizonte, MG', 3144445555),
	('Agência Filial C', 'Avenida Transversal, 400, Porto Alegre, RS', 5155556666),
	('Agência Filial D', 'Rua Diagonal, 500, Salvador, BA', 7166667777);
    
create table contas(
	conta_id int primary key auto_increment,
    cliente_id int,
    agencia_id int, 
    tipo_conta enum ('Corrente', 'Poupança', 'Salário'),
    saldo decimal(10, 2) default 0.00,
    data_abertura date,
    status enum ('Ativa', 'Inativa', 'Bloqueada') default 'Ativa',
    foreign key (cliente_id) references clientes(cliente_id),
    foreign key (agencia_id) references agencias(agencia_id)
    );
    
    -- Inserir Contas
    
    insert into contas(cliente_id, agencia_id, tipo_conta, saldo, data_abertura, status) values
	(1, 1, 'Corrente', 1500.00, '2023-01-10', 'Ativa'),
	(2, 2, 'Poupança', 5000.00, '2022-05-22', 'Ativa'),
	(3, 1, 'Salário', 2000.00, '2023-03-15', 'Ativa'),
	(4, 3, 'Corrente', 1000.00, '2023-02-01', 'Bloqueada'),
	(5, 2, 'Poupança', 10000.00, '2022-11-08', 'Inativa');
    
create table transacoes(
	transacao_id int primary key auto_increment,
    conta_origem_id int null,
    conta_destino_id int null,
    tipo_transacao enum ('Depósito', 'Saque', 'Transferência', 'Pagamento'),
    valor decimal(10, 2),
    data_transacao datetime default current_timestamp,
    descricao varchar(200),
    foreign key (conta_origem_id) references contas(conta_id),
    foreign key (conta_destino_id) references contas(conta_id)
    );
    
    -- Inserir Transações
    
    insert into transacoes(conta_origem_id, conta_destino_id, tipo_transacao, valor, descricao) values
    (1, NULL, 'Depósito', 1000.00, 'Depósito inicial'),
	(2, NULL, 'Saque', 500.00, 'Saque para despesas'),
	(1, 2, 'Transferência', 300.00, 'Transferência entre contas'),
	(3, NULL, 'Pagamento', 150.00, 'Pagamento de conta de luz');
    
create table emprestimos(
	emprestimo_id int primary key auto_increment,
    conta_id int,
    valor decimal(15, 2),
    taxa_juros decimal(5, 2),
    parcelas int,
    valor_parcela decimal(15, 2),
    data_contratacao date, 
    status enum ('Ativo', 'Quitado', 'Inadimplente') default 'Ativo',
    foreign key (conta_id) references contas(conta_id)
    );
    
    -- Inserir Empréstimos
    
    insert into emprestimos(conta_id, valor, taxa_juros, parcelas, valor_parcela, data_contratacao, status) values
	(1, 10000.00, 5.00, 12, 856.07, '2023-01-15', 'Ativo'),
	(2, 5000.00, 4.50, 6, 853.48, '2023-02-20', 'Ativo'),
	(3, 20000.00, 6.00, 24, 960.64, '2022-11-01', 'Quitado'),
	(4, 8000.00, 5.50, 18, 555.56, '2023-03-10', 'Inadimplente'),
	(5, 12000.00, 4.80, 15, 878.91, '2023-04-05', 'Ativo');
    
create table pagamentos_emprestimos(
	pagamento_id int primary key auto_increment,
    emprestimo_id int,
    numero_parcela int, 
    valor_pago decimal(10, 2),
    data_pagamento date,
    foreign key (emprestimo_id) references emprestimos(emprestimo_id)
    );

	-- Inserir Pagamentos de Empréstimos
    
	insert into pagamentos_emprestimos(emprestimo_id, numero_parcela, valor_pago, data_pagamento) values
    (1, 1, 856.07, '2023-02-15'),
	(1, 2, 856.07, '2023-03-15'),
	(2, 1, 853.48, '2023-03-20'),
	(3, 1, 960.64, '2022-12-01'),
	(4, 1, 555.56, '2023-04-10'),
	(5, 1, 878.91, '2023-05-05');
    