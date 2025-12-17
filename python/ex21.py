class Carro:
    marca = ""
    modelo = ""
    ano = 0
    cor = ""
    ativo = False

carro1 = Carro()
carro1.marca = "Toyota"
carro1.modelo = "Corolla"
carro1.ano = 2014
carro1.cor = "Prata"
carro1.ativo = True

carro2 = Carro()
carro2.marca = "Honda"
carro2.modelo = "Civic"
carro2.ano = 2019
carro2.cor = "Preto"
carro2.ativo = False

print(f"Carro 1: {carro1.marca} {carro1.modelo}, Ano: {carro1.ano}, Cor: {carro1.cor}, Ativo: {carro1.ativo}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}, Ano: {carro2.ano}, Cor: {carro2.cor}, Ativo: {carro2.ativo}")