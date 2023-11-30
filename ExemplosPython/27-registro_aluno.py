#Classe de cadastro do aluno
class Aluno:
    def __init__ (self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

#Classe para armazenar os registros de alunos
class RegistroAlunos:
    def __init__(self):
        self.alunos = [] #lista/vetor para armazenar os alunos cadastrados

    def adicionar_alunos(self, aluno):
        self.alunos.append(aluno)

    def exibir_alunos(self):
        for aluno in self.alunos:
            print(f'Nome: {aluno.nome}\tIdade: {aluno.idade}\tCurso: {aluno.curso}')

#Instância do tipo clase RegistroAlunos
registro = RegistroAlunos()

#Criar instâncias da classe Aluno adicionando dados (registros)
aluno1 = Aluno("João", 21, "Sistemas de Informação")
aluno2 = Aluno("Maria", 23, "Arquitetura")
aluno3 = Aluno("Paulo", 33, "Matemática")

registro.adicionar_alunos(aluno1)
registro.adicionar_alunos(aluno2)
registro.adicionar_alunos(aluno3)

registro.exibir_alunos()