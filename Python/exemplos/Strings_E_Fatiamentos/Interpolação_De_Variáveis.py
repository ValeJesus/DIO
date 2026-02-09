nome = "Joao"
idade = 28
profissao = "Analista de Dados"
linguagem= "Python"

dados = {"Nome": "Joao", "idade": 17}

print("Nome:  %s Idade : %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1} ".format(nome, idade))
print("Nome: {n} Idade: {i} Nome {1} {1}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {idade}".format(age=idade, name=nome))
