""" Herança: Conta Corrente e Poupança
Crie uma classe ContaPoupanca que herda de ContaBancaria e adiciona um método rendimento(taxa) que aumenta o saldo.

from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def rendimento(self, taxa):
        self.saldo += self.saldo * taxa
        print(f"Rendimento aplicado! Novo saldo: R$ {self.saldo:.2f}")

# Teste
poupanca = ContaPoupanca("Maria", 1000)
poupanca.rendimento(0.05)  # 5% de rendimento
print(poupanca.exibir_saldo()) """
from exe_112_poo_conta_bancaria_publico import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def rendimento(self, taxa):
        self.saldo = self.saldo + self.saldo * taxa
        print(f'Rendimento aplicado! Novo Saldo R$ {self.saldo:.2f}.')

# teste
        
contaPoupanca = ContaPoupanca('Marks', 100)

contaPoupanca.rendimento(0.01) # 1% de rendimento
print(contaPoupanca.exibir_saldo())
