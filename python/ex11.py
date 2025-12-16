#Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma = 0

for num in range(1, 11):
    if num % 2 != 0:
        soma += num

print(soma)
