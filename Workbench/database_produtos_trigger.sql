Sintaxe da Trigger

    CREATE TRIGGER nome momento evento(BEFORE (antes)
    e AFTER (depois))
    ON tabela
    FOR EACH ROW
    BEGIN
    /*corpo do código*/
    END

Os registros NEW e OLD
Os triggers, são executados em conjunto com operações de inclusão
e exclusão, esse acesso é feito através das palavras NEW e OLD.
A palavra reservada NEW dá acesso ao novo registro. Pode-se
acessar as colunas da tabela como atributo do registro NEW.
O operador OLD dá acesso ao registro que está sendo removido.

    DELIMITER //
    altera o delimitador atual para //, que no nosso caso é o;

    1. Criar as tabelas que serão utilizadas
    CREATE DATABASE Produto;
    USE Produto;
    CREATE TABLE Produtos
    (
    Codigo VARCHAR(3) PRIMARY KEY,
    Descricao VARCHAR(50) UNIQUE,
    Estoque INT NOT NULL DEFAULT 0
    );
    INSERT INTO Produtos VALUES ('001', 'Computador', 15);
    INSERT INTO Produtos VALUES ('002', 'Monitor', 25);
    INSERT INTO Produtos VALUES ('003', 'Teclado', 45);
    CREATE TABLE ItensVenda
    (
    Venda INT,
    Cod_Produto VARCHAR(3),
    Quantidade INT
    );

2. Criar um Trigger que ao inserir um registro da tabela
ItensVenda, o estoque do produto referenciado deve ser
alterado na tabela Produtos
Resposta

        DELIMITER $
        CREATE TRIGGER Tgr_ItensVenda_Insert AFTER INSERT
        ON ItensVenda
        FOR EACH ROW
        BEGIN
        UPDATE Produtos SET Estoque = Estoque - NEW.Quantidade
        WHERE Codigo = NEW.Cod_Produto;
        END$
        DELIMITER;

Testando os valores do estoque

        INSERT INTO ItensVenda VALUES (1, '002',3);
        INSERT INTO ItensVenda VALUES (1, '002',1);
        INSERT INTO ItensVenda VALUES (1, '003',5);
        
/*3. Completar a TRIGGER
Criar um Trigger que ao inserir ou excluir um registro
da tabela ItensVenda, o estoque do produto referenciado
deve ser alterado na tabela Produtos*/

		DELIMITER $
        CREATE TRIGGER Tgr_ItensVenda_Delete AFTER DELETE
        ON ItensVenda
        FOR EACH ROW
        BEGIN
        UPDATE Produtos SET Estoque = Estoque + OLD.Quantidade
        WHERE Codigo = OLD.Cod_Produto;
        END$
        DELIMITER ;
        