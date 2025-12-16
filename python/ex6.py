#Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

nome = str (input('Digite seu nome:'))
idade = int (input('Digite sua idade: '))

if idade >= 0 and idade <= 12:
    print (f'{nome},{idade} anos (CRIANÇA)')
elif idade >=13 and idade <=18:
    print (f'{nome},{idade} anos (ADOLESCENTE) ')
elif idade >=18:
    print (f'{nome},{idade} anos (ADULTO)')
else:
    print ('Escreva uma idade valida!')