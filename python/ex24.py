#Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo      
restaurante1 = Restaurante('La Bella Italia', 'Italiana')
print(f'Restaurante: {restaurante1.nome}, Categoria: {restaurante1.categoria}, Ativo: {restaurante1.ativo}')