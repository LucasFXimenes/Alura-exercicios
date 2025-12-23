class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def ativar_conta(self):
        self.ativo = True

    def desativar_conta(self):
        self.ativo = False

    def __str__(self):
        return f'Titular: {self.titular} | Saldo: R$ {self.saldo} | Ativo: {self.ativo}'


conta1 = ContaBancaria('Lucas Freitas', 10000)
conta2 = ContaBancaria('Raphael Junior',5000)
print(conta1)

validacao = input('Deseja ativar a conta? (sim/não): ').lower()

if validacao == 'sim':
    conta1.ativar_conta()
elif validacao == 'não':
    conta1.desativar_conta()
else:
    print('Digite um valor válido')

print(conta1)
