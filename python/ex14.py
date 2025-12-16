#Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
numeros = []
soma = 0

for i in range(5):  # quantidade de números
    try:
        n = int(input('Digite um número: '))
        numeros.append(n)
    except ValueError:
        print('Erro: digite apenas números inteiros')

for num in numeros:
    soma += num

print('Lista:', numeros)
print('Soma dos números:', soma)
