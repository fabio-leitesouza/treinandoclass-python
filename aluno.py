class Aluno:
  def __init__(self, nome, matricula, nascimento, genero, nota = 0):
    self.__nome = nome
    self.__matricula = matricula
    self.__nascimento = nascimento
    self.__genero = genero
    self.__nota = nota

  @property
  def nome(self):
    print("Chamando @property nome()")
    return self.__nome

  @nome.setter
  def nome(self, nome):
    print("Chamando setter")
    self.__nome = nome
    
  @property
  def genero(self):
    print("Chamando @property nome()")
    return self.__genero

  @genero.setter
  def genero(self, genero):
    print("Chamando setter")
    self.__nome = genero  

  def __pode_reduzir(self, valor_reducao):
    nota_positiva = self.__nota
    return valor_reducao <= nota_positiva

  def reduzir_nota(self, reducao):
    if(self.__pode_reduzir(reducao)):
      self.__nota -= reducao
    else:
      print("valor maior que a nota atual")      
 
  def get_nota(self):
    return self.__nota

  def get_genero(self):
    return self.__genero

  def set_nota(self, valor):
    self.__nota += valor
    
  @staticmethod
  def escola():
    return {"Senac em Minas": "Itajubá"}


cris = Aluno("Cris", 2501, "01/01/2004", "F")

cris.set_nota(20)
print(cris.get_nota())

cris.nome = "Marcão"
cris.genero = "M"
print(cris.get_genero())

print(cris.nome)

cris.reduzir_nota(5)
print(cris.get_nota())  