lista = []
soma = 0
for i in range (0,3):
    try:
        numero = int (input('Digite um número: '))
        lista.append(numero)
        soma += numero
    except:
        print('você não digitou um valor valido')

media = soma / len(lista)
print('Números digitados:', lista)
print('Média:', media)
    
 