""" Crie uma classe ContaBancaria com titular e saldo. Adicione métodos depositar(valor) e sacar(valor), que impede saldo negativo. """
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def saque(self, valor):
        if self.saldo > valor:
            self.saldo = self.saldo - valor
        else:
            print('Saldo Insuficiente.')

    def deposito(self, valor):
            self.saldo = self.saldo + valor

conta1 = ContaBancaria('Maria')
conta1.saque(50)
conta1.deposito(100)
print(f'O saldo da conta é: {conta1.saldo}')
