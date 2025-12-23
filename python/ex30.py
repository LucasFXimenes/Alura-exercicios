class ContaBancaria:
    def __init__(self, titular: str, saldo: float, ativo: bool = False):
        self._titular = titular
        self._saldo = saldo
        self._ativo = ativo

    @property
    def titular(self) -> str:
        return self._titular

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def ativo(self) -> bool:
        return self._ativo

    @ativo.setter
    def ativo(self, valor: bool):
        if not isinstance(valor, bool):
            raise ValueError("O atributo 'ativo' deve ser booleano")
        self._ativo = valor

    def __str__(self) -> str:
        return (
            f'Titular: {self.titular} | '
            f'Saldo: R$ {self.saldo:.2f} | '
            f'Ativo: {self.ativo}'
        )


conta1 = ContaBancaria('Lucas Freitas', 10000)
print(conta1)

conta1.ativo = True
print(conta1)
