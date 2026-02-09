#Operadores aritmeticos

print (1 + 1) #soma
#-
print (2 - 1) #subtração
#-
print (2 * 3) #multiplicação
#-
print (10 / 2) #divisão
#-  
print (10 % 3) # modulo
#-
print (2 ** 3) #exponenciação

#OPERADORES DECOMPARAÇÃO    

#igualdade
saldo = 450
saque = 200

print ( saldo == saque)

#diferença
print (saldo != saque)
#maior que / maior ou igual

print (saque > saldo)
print (saque >= saldo)

#menor que / menor ou igual
print (saque < saldo)
print (saque <= saldo)

#operadores de atribuição



saldo2 = 500 #atribuição simples
saldo2 += 200 #atribuição com adição
saldo2 -= 100 #atribuição com subtração
saldo2 *= 2 #atribuição com multiplicação
saldo2 /= 2 #atribuição com divisão
saldo2 %= 3 #atribuição com módulo
saldo2 **= 2 #atribuição com exponenciação

#OPERADORES LOGICOS

saldo3 = 1000
saque3 = 200
limite = 100

saldo >= saque
# retorna true
saldo <= limite
# retorna false



#OPERADOR "E"

# saldo é maior ou igual a saque E saldo é menor ou igual a limite
saldo3 >= saque3 and saldo3 <= limite
#retorna false

#OPERADOR "OU"

# saldo é maior ou igual a saque OU saque é menor ou igual a limite
saldo3 >= saque3 or saque3 <= limite
#retorna true

#OPERADOR NEGAÇÃO
# o not é o inverso da verdade, ou seja, se a expressão for verdadeira, o not retorna 
# falso, e se a expressão for falsa, o not retorna verdadeiro.

contatos_emergencia = []

not 1000 > 1500
#retorna true

not contatos_emergencia
#retorna true

not "saque 1500;"
#retorna false

not ""
#retorna true


# PARÊNTESES

saldo4 = 1000
saque4 = 250
limite4 = 200
conta_especial4 = True

#saldo é maior ou igual a saque E saque é menor ou igual a limite OU conta_especial e saldo é maior ou igual a saldo
saldo4 >= saque4 and saque4 <= limite4 or conta_especial4 and saldo4 >= saque4
#retorna true

# (saldo é maior ou igual a saque E saqueé menor ou igual a limite)
#OU
# (conta especial E saldo é maior ou igual a saque)
(saldo4 >= saque4 and saque4 <= limite4) or (conta_especial4 and saldo4 >= saque4)
#retorna true

#TESTES DO AND E OR

print(True and True and True) #retorna true
print(True and False and True) #retorna false
print(False and False and False) #retorna false

print(True or True or True) #retorna true
print(True or False or False) #retorna true
print(False or False or False) #retorna false

#OPERADORES DE IDENTIDADE

curso = "Curso de Python"
nome_curso = curso
saldo5 = 200
limite5 = 200

print(curso is nome_curso)
#retorna true

print (curso is not nome_curso)
#retorna false

print(saldo5 is limite5)
#retorna true
print(saldo5 is not limite5)
#retorna false


#OPERADORES DE ASSOCIAÇÃO
curso2 = "Curso de Python2"
frutas = ["laranja", "uva", "limão"]
saques = [100, 1500]

print ("Python2" in curso2)
#retorna true
print ("maça" not in frutas)
#retorna true
print (200 in saques)
#retorna false