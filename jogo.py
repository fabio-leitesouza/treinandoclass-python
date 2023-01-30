class Jogo:

  def __init__(self, titulo, ano, plaforma, genero):
    self.titulo = titulo
    self.ano = ano
    self.plataforma = plaforma
    self.genero = genero

zelda = Jogo("Zelda", 1986, "Nintendinho", "Aventura")

print(zelda.titulo)
