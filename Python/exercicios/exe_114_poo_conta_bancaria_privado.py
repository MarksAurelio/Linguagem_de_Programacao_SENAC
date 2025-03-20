""" Crie uma classe ContaBancaria com atributos públicos saldo e titular.
Crie métodos depositar(valor) e sacar(valor), verificando se há saldo suficiente.
Crie um método exibir_saldo() que retorna o saldo formatado.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor} realizado.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_saldo(self):
        return f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}"

# Teste
conta = ContaBancaria("João", 500)
conta.depositar(300)
conta.sacar(200)
print(conta.exibir_saldo())


Herança: Conta Corrente e Poupança
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
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo = self.__saldo + valor
            print(f'Depósito de R$ {valor}.')
        else:
            print('Valor inválido.')

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo = self.__saldo - valor
            print(f'Saque de R$ {valor}.')
        else:
            print('Saldo Insuficiente.')

    def exibir_saldo(self):
        return f'Titular: {self.titular} | Saldo: R$ {self.__saldo:.2f}'
    
contaBancaria = ContaBancaria('Marks', 200.00)

contaBancaria.titular
contaBancaria.depositar(100.00)
contaBancaria.sacar(50.00)
print(contaBancaria.exibir_saldo())
