class Pessoa:
    
    def __init__(self, nome, idade, profissao):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao.lower()

    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade} | Profissão: {self.profissao.lower()}'

    def aniversario(self):
        self.idade += 1
        print(f'Feliz aniversário, {self.nome}\n')

    @property
    def saudacao(self):
        if self.profissao == 'developer':
            return f'Olá, {self.nome}! Seja bem-vindo(a). Que o código esteja com você.'
        else:
            return (f'Olá, {self.nome}! Seja bem-vindo(a) à nossa plataforma.')


# Testes
p1 = Pessoa('Lucas Ximenes', 21, 'Developer')
print(p1)

p1.aniversario()
print(p1)

print(p1.saudacao)
