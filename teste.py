def criar_aluno(ra, nome, nascimento, nota):
  aluno = {"ra": ra, "nome": nome, "nascimento": nascimento, "nota": nota}
  return aluno

def atribuir_nota(nota, valor):
  nota["nota"] += valor

def remover_nota(nota, valor):
  nota["nota"] -= valor

def exibir_nota(ra):
  print("A nota é {}".format(aluno["nota"]))
  