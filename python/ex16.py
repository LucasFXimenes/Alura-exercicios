#Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
dados = {'nome':'Lucas','idade':26,'email':'devlucasfreitas@outlook.com','cidade':'SP'}
print(dados)


#Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
dados['idade'] = 24 
print (dados)
#Adicione um campo de profissão para essa pessoa;
dados['profissao'] = 'developer'
print(dados)
#Remova um item do dicionário.
dados.pop('email')
print(dados)
