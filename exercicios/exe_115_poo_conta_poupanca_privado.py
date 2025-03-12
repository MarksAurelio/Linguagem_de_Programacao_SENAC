""" Herança: Conta Corrente e Poupança
Crie uma classe ContaPoupanca que herda de ContaBancaria e adiciona um método rendimento(taxa) que aumenta o saldo. """
from exe_114_poo_conta_bancaria_privado import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def rendimento(self, taxa):
        rendimento = self._ContaBancaria__saldo * taxa
        self.depositar(rendimento)
        print(f'Rendimento aplicado! Novo Saldo R$ {self._ContaBancaria__saldo:.2f}.')

# teste
        
contaPoupanca = ContaPoupanca('Marks', 100)

contaPoupanca.rendimento(0.01) # 1% de rendimento
print(contaPoupanca.exibir_saldo())
