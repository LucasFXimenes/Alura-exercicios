#Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.
import time

x = int (input('Digite a coordenada X: '))
y = int (input('Digite a coordenada Y: '))

print('Verificando em qual quadrante do plano cartesiano estão as coordenadas...')
time.sleep(3)

def verificar():
    if x > 0 and y > 0:
        print (f'As coordenadas X:{x} e Y:{y} são do 1° quadrante do plano cartesiano. ')
    elif x < 0 and y > 0:
        print (f'As coordenadas X:{x} e Y:{y} são do 2° quadrante do plano cartesiano.')
    elif x < 0 and y < 0:
        print(f'As coordenadas X:{x} e Y:{y} são do 3° quadrante do plano cartesiano.')
    elif x > 0 and y < 0:
        print(f'As coordenadas X:{x} e Y:{y} são do 4° quadrante do plano cartesiano.')
    else:
        print(f'As coordenadas X:{x} e Y:{y} estão no eixo ou origem.')
verificar()
    