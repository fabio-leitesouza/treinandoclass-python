class Programa:
    def __init__(self, nome, genero, ano):
        self._nome = nome
        self.genero = genero
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'


class Filme(Programa):
    def __init__(self, nome, genero, ano, duracao):
        super().__init__(nome, genero, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Duração: {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, genero, ano, temporadas):
        super().__init__(nome, genero, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Temporadas: {self.temporadas} Likes: {self.likes}'

# class Playlist:
#   def __init__(self, nome, catalogo):
#     self.nome = nome
#     self.catalogo = catalogo

#   def tamanho(self):
#     return len(self.catalogo)

class Playlist():
  def __init__(self, nome, catalogo):
    self.nome = nome
    self._catalogo = catalogo

  def __getitem__(self, item):
    return self._catalogo[item]

  def __len__(self):
    return len(self._catalogo)


evil_dead = Filme("Evil Dead", "Terrir", 1984, 110)
stranger_things = Serie("Stranger", "Terror", 2022, 4)

evil_dead.dar_likes()
evil_dead.dar_likes()
evil_dead.dar_likes()
evil_dead.dar_likes()
evil_dead.dar_likes()

stranger_things.dar_likes()
stranger_things.dar_likes()
stranger_things.dar_likes()

print(stranger_things.likes)

listinha = [evil_dead, stranger_things]

for programa in listinha:
    print(programa)

play_list_fim_de_semana = Playlist("fim de semana", listinha)

for programas in play_list_fim_de_semana:
  print(programas)

print(f' Tamanho: {len(play_list_fim_de_semana._catalogo)}')



