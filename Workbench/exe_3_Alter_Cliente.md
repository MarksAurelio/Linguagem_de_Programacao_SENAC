Adição de Nova Coluna para Pontos de Fidelidade

Realizaremos essa atividade prática para explorar como fazer alterações em um banco de dados MySQL. Nosso objetivo é adicionar uma nova coluna para acompanhar os pontos de fidelidade dos clientes na tabela já existente (cliente). Sempre que um cliente for adicionado, por padrão será atribuído o valor zero para a nova coluna criada.

Objetivo:
- Compreender e praticar a adição de uma nova coluna a uma tabela existente em um banco de dados MySQL.
- Reconhecer a importância de planejar e executar alterações no esquema do banco de dados para atender às necessidades do sistema.

Novos campos da Tabela Cliente:

Cliente
- id_cliente (chave primária),
- nome_cliente
- pontos_fidelidade

 Instruções

Sem valor padrão:

ALTER TABLE nomeTabela
ADD COLUMN novoNomeColuna VARCHAR(20);

Com valor padrão(DEFAULT):

ALTER TABLE nomeTabela
ADD COLUMN novoNovemColuna VARCHAR(20) DEFAULT 'regular';

![Alt text](Alter_Cliente.png)