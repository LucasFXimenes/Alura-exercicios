frequencia = {}

for i in range(5):
    palavra = input('Digite uma palavra: ').lower()

    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)
