class Cliente:
    def __init__(self, nome, idade, email, id):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.id = id

    def __str__(self):
        return f'Cliente: {self.nome}, Idade: {self.idade}, Email: {self.email}, ID: {self.id}'


lista_clientes = [
    Cliente('Lucas Ximenes', 21, 'lucas123@email.com', 1),
    Cliente('Ana Silva', 30, 'ana@gmail.com', 2),
    Cliente('Juliana Costa', 25, 'juliana@gmail.com', 3)
]

for cliente in lista_clientes:
    print(f'{cliente} \n')
