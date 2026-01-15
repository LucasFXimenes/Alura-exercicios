# 7) Crie um método de classe para a conta `ClienteBanco`.
class ClienteBanco:
    def __init__(self,nome: str,email: str,telefone: str,endereco: str,cpf: str):
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._endereco = endereco
        self._cpf = cpf 
    @property
    def nome(self) -> str:
        return self._nome           
    @property   
    def email(self) -> str:
        return self._email  
    @property   
    def telefone(self) -> str:
        return self._telefone                   
    @property   
    def endereco(self) -> str:
        return self._endereco
    @property   
    def cpf(self) -> str:       
        return self._cpf
    def __str__(self) -> str:
        return (
            f'Nome: {self.nome} | '
            f'Email: {self.email} | '
            f'Telefone: {self.telefone} | '
            f'Endereço: {self.endereco} | '
            f'CPF: {self.cpf}\n'
        )

    @classmethod
    def criar_conta(cls, nome: str, saldo_inicial: float):
        cliente = cls(
            nome,
            email="",
            telefone="",
            endereco="",
            cpf=""
        )
        conta = ClienteBanco(titular=cliente.nome, saldo=saldo_inicial, ativo=True)
        return conta
        
# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")