# Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
quadrados = {}

for numero in range(1, 6):
    quadrados[numero] = numero ** 2

print(quadrados)