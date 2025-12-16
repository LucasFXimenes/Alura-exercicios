import time

name = 'Lucas'
passw = '12345'

def dados():
    global nome, senha  # <- deixa as variáveis acessíveis fora da função
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    print('Dados coletados com sucesso!')

dados()

print('Validando dados...')
time.sleep(2)

def comparar():
    if nome == name and senha == passw:
        print('Login realizado!')
    else:
        print('Dados inválidos!')

comparar()


