nome, idade = "Guilherme", 30

print(nome, idade)

print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = ['SP', 'RJ', 'MG', 'SC']

print(BRAZILIAN_STATES)


#conversão de float para inteiro
#1:
preco = 10.30
print(preco)

preco = int(preco)
print(preco)
#2:
preco = 10
print(preco)

print(preco / 2)
#sem as duas barras o valor fica float, com as duas barras o valor fica inteiro
print(preco // 2)

#----------------------------
#Numericos para string
preco = 10.50
idade = 28

print(str(preco))
print(str(idade))

texto = f"idade {idade} preço {preco}"
print(texto)

#----------------------------
#string pra numerico

preco = "10.50"
idade = "28"    

print(float(preco))
print(int(idade))
#----------------------------
#print type utilizado pra ver o tipo da variavel
print(type(preco))


#----------------------------

nome = input("Qual o seu nome? ")