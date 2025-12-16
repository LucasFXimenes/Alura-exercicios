#- Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

n = int (input('Digite um número: '))

if n % 2 == 0:
   print (f"O número {n} é par! ")
else:
    print (f"O número {n} é impar!")