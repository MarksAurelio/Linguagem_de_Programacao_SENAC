""" Crie uma classe chamada ContaBancaria que possua os seguintes atributos:

titular (público): nome do titular da conta.
__saldo (privado): saldo da conta.
Implemente um método chamado exibir_saldo() que retorne o saldo formatado.
No código principal, crie uma instância de ContaBancaria e exiba o saldo usando o método, demonstrando que o atributo privado não pode ser acessado diretamente.
Atributo Protegido (com um único underscore _saldo): Pode ser acessado diretamente pela classe e suas subclasses. É recomendado apenas não acessá-lo diretamente fora da classe para evitar modificações indesejadas.
Atributo Privado (com dois underscores __saldo): Não pode ser acessado diretamente fora da classe. Só pode ser manipulado através de métodos da própria classe. """
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def exibir_saldo(self):
        return self.__saldo
    
contaBancaria = ContaBancaria('Marks', 200.0)

print(contaBancaria.titular)
print(contaBancaria.exibir_saldo())
