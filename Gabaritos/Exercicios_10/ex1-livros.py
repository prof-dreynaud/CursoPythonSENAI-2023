#Exercício 1:
#Crie uma classe chamada Livro com os seguintes campos: título, autor e ano de publicação. 
#Em seguida, crie três instâncias dessa classe para representar três livros diferentes e exiba as informações de cada livro.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro3 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)

print("Informações do livro 1:")
print("Título:", livro1.titulo)
print("Autor:", livro1.autor)
print("Ano de Publicação:", livro1.ano_publicacao)
print()

print("Informações do livro 2:")
print("Título:", livro2.titulo)
print("Autor:", livro2.autor)
print("Ano de Publicação:", livro2.ano_publicacao)
print()

print("Informações do livro 3:")
print("Título:", livro3.titulo)
print("Autor:", livro3.autor)
print("Ano de Publicação:", livro3.ano_publicacao)