# exemplo sem repetiçao
# Repetição dos dois proximos números

a = int(input("Digite um número: "))
print(a)

a+= 1
print(a)

a+= 1
print(a)

# exemplo com repetição

b = int(input("Informe um número: "))
print(b)

repita 2 vezes:
   b += 1
   print(b)

#for 

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ") #end=" " para imprimir as vogais na mesma linha, separadas por espaço

print() #adiciona uma quebra de linha

#FUNÇÃO RANGE

#range(stop) -> range object
#range(start, stop[, step])-> range object

list(range(4))
#>>> [0, 1, 2, 3]

#utilizando range com for

for numero in range (0, 11):
    print(numero, end=" ")

#>>> 0 1 2 3 4 5 6 7 8 9 10

#exibindo a tabuada do 5

for numero in range(0, 51, 5):
    print(numero, end=" ")

#>>> 0 5 10 15 20 25 30 35 40 45 50

#exibindo a tabuada do 2

for numero in range(0, 21, 2):
    print(numero, end=" ")

#>>> 0 2 4 6 8 10 12 14 16 18 20

# WHILE

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2]Extrado \n[0]Sair\n"))

    if opcao == 1:
        print("Saque selecionado!")
    elif opcao == 2:
        print("mostrando extrado!")
        
else:
    print("Obrigado por ser nosso cliente, volte sempre!")


#-----

while True:
    numero = int(input("Digite um número: "))

    if numero == 10:
        break

    print(numero)

#Faz usar o "for" quando sabemos o número exato de vezes que o nosso bloco de código deve ser executado,
# e usamos while quando nao sabemos o número exato
 