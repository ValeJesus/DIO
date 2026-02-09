frutas = ("laranja", "pera", "uva")
print(frutas[0])
print(frutas[-1])
letras = tuple("python")

numeros = tuple([1,2,3,4,5])

pais = ("Brasil",)

#tuplas aninhadas
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

matriz[0] #>>> (1, "a", 2)
matriz[0][0] #>>> 1
matriz[0][-1] #>>> 2
matriz[-1][-1] #>>> "c"