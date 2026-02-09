frutas = ["laranja", "maça", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("Python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "Celtinha", 40, 20, 's']
print(carro)

#Listas aninhadas

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
    ]

matriz[0] #>>> [1, "a", 2]
matriz[0][0] #>>> 1
matriz[0][-1] #>>> 2
matriz[-1][-1] #>>> "c"

# Função enumarate

carros = ["gol", "celta", "fusca"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#formas de filtrar elementos de uma lista


# utilizando list comprehension
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
pares = [numeros for numeros in numeros if numeros % 2 == 0]
print(pares)

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# modificando valores de uma lista

numeros = [1, 2, 3, 4, 5]
quadrado = []

 for numero in numeros:
        quadrado.append(numero ** 2)

# modificando valores de uma lista pt2

numeros = [1, 2, 3, 4, 5]
quadrado = [numero ** 2 for numero in numeros]