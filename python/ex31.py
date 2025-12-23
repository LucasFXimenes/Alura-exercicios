class ClienteBanco:
    def __init__(
        self,
        nome: str,
        email: str,
        telefone: str,
        endereco: str,
        cpf: str
    ):
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


cliente1 = ClienteBanco(
    'Lucas Freitas',
    'lucas@gmail.com',
    '(11) 91234-5678',
    'Rua das Acácias, 123',
    '123.456.789-00'
)

cliente2 = ClienteBanco(
    'Raphael Junior',
    'raphaeljr@gmail.com',
    '(21) 98765-4321',
    'Avenida Brasil, 456',
    '987.654.321-00'
)

cliente3 = ClienteBanco(
    'Ana Silva',
    'anasilva@gmail.com',
    '(31) 99876-5432',
    'Praça da Liberdade, 789',
    '456.789.123-00'
)

print(cliente1)
print(cliente2)
print(cliente3)
