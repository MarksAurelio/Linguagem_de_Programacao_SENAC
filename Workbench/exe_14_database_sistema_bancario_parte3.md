use sistema_bancario;

/*Instruções para o Projeto Final de Banco de Dados – MySQL*/

/*2. Trigger
• Criar: Trigger para atualizar o saldo da conta após uma transação

Após, verifique os saldos atuais das contas que serão usadas nos testes:
SELECT conta_id, cliente_id, saldo FROM Contas;

-- Inserir um depósito na conta 1 (sem conta de origem)
INSERT INTO Transacoes (conta_destino_id, tipo_transacao, valor, descricao)
VALUES (1, 'Depósito', 500.00, 'Depósito teste trigger');

-- Verificar se o saldo foi atualizado
SELECT conta_id, saldo FROM Contas WHERE conta_id = 1;*/

		DELIMITER $
        CREATE TRIGGER Tgr_Contas_Atualizar_Saldo AFTER INSERT
        ON transacoes
        FOR EACH ROW
        BEGIN
        UPDATE contas SET saldo = saldo + NEW.valor
        WHERE conta_id = NEW.conta_destino_id;
        END$
        DELIMITER ;
-- Após, verifique os saldos atuais das contas que serão usadas nos testes:

        SELECT conta_id, cliente_id, saldo FROM Contas;

-- Inserir um depósito na conta 1 (sem conta de origem)  

        INSERT INTO Transacoes (conta_destino_id, tipo_transacao, valor, descricao) VALUES 
        (1, 'Depósito', 500.00, 'Depósito teste trigger');

-- Verificar se o saldo foi atualizado   

        SELECT conta_id, saldo FROM Contas WHERE conta_id = 1;
        
-- Deletar o saldo antes acrescido criando uma nova Trigger

        DELIMITER $
        CREATE TRIGGER Tgr_Contas_Deletar_Saldo AFTER DELETE
        ON transacoes
        FOR EACH ROW
        BEGIN
        UPDATE contas SET saldo = saldo - OLD.valor
        WHERE conta_id = OLD.conta_destino_id;
        END$
        DELIMITER ;

-- Consultar transações

        select * from transacoes;
        
-- Deletar transacao (depósito) antes realizado

        delete from transacoes where transacao_id = 5;
        