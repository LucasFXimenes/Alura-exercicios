
from ex34 import Livro

# criando livros
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Hobbit", "Tolkien", 1937)

# emprestar
livro1.emprestar()

print("Após empréstimo:")
print(livro1)

# verificar por ano
disponiveis = Livro.verificar_disponibilidade(1937)

print("\nLivros disponíveis de 1937:")
for livro in disponiveis:
    print(livro)
