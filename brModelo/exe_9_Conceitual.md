Situação: Você está projetando um sistema para uma concessionária de veículos. Eles desejam armazenar informações sobre os veículos em seu estoque, que incluem carros e caminhões. Cada veículo possui informações gerais, mas carros e caminhões têm atributos específicos. Como você estruturaria o banco de dados para atender a esses requisitos?
 O Diagrama de Entidade-Relacionamento (DER) mostraria a tabela "Veículo" como a entidade principal, com linhas para "Carro" e "Caminhão" conectadas a ela com linhas de especialização.
- Especialização:
- Entidades:
- Veículo
- Carro
- Caminhão
- Relacionamentos:
Especialização: Veículo se especializa em Carro e Caminhão

Atributos:

Veículo: ID_Veículo (PK), Marca, Modelo, Ano, etc.

Carro: ID_Carro (PK, FK referenciando Veículo), Número de
Portas, Cor, etc.

Caminhão: ID_Caminhão (PK, FK referenciando Veículo), Tipo
de Carroceria, Capacidade de Carga, etc.

![Alt text](Conceitual_9.png)