#Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self,nome,categoria,ativo,endereco,telefone):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.endereco = endereco
        self.telefone = telefone

restaurante1 = Restaurante('Sabores da terra','Comida Brasileira',True,'Rua das Flores 1079','(11) 98765-4321')

print(f'Restaurente: {restaurante1.nome}, Categoria: {restaurante1.categoria}, Ativo: {restaurante1.ativo}, Endereço: {restaurante1.endereco}, Telefone: {restaurante1.telefone}')