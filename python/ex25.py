#Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo

    def __str__(self):
        return f'Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}'
    
restaurante1 = Restaurante('La Bella Italia', 'Italiana')
restaurante1.ativo = True

restaurante2 =  Restaurante('Xami Xami','Comida Chinesa')

print(restaurante1)
print(restaurante2)