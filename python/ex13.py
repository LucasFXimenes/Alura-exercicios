#Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
num = int(input('Digite um número: '))

for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')
