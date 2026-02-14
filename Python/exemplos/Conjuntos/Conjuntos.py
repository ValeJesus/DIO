# sets -> conjuntos
# não possuem valores duplicados

set ([1, 2, 3, 4, 5, 5, 5]) #>>> {1, 2, 3, 4, 5}    

print(set([1, 2, 3, 4, 5, 5, 5]))

set("abacaxi") #>>> {'a', 'b', 'c', 'x', 'i'}

set (("palio", "gol", "celta", "palio")) #>>> {'Palio', 'gol', 'celta'}

# acessando os dados

numeros = {1, 2, 3, 4, 5}

numeros = list(numeros)

print(numeros[0]) #>>> 1

#Função enumerate]

carros = {"gol", "celta", "fusca"}
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#Métodos da classe set

#union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)    #>>> {1, 2, 3, 4}

#intersection

conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}
conjunto_c.intersection(conjunto_d) #>>> {2, 3}

#diferença

conjunto_e = {1, 2, 3}
conjunto_f = {2, 3, 4}

conjunto_e.difference(conjunto_f) #>>> {1}
conjunto_f.difference(conjunto_e) #>>> {4}

#symemtric difference

conjunto_g = {1, 2, 3}
conjunto_h = {2, 3, 4}

conjunto_g.symmetric_difference(conjunto_h) #>>> {1, 4}

#issubset

conjunto_i = {1, 2}
conjunto_j = {1, 2, 3, 4}

conjunto_i.issubset(conjunto_j) #>>> True
conjunto_j.issubset(conjunto_i) #>>> False

#issuperset

conjunto_k = {1, 2, 3, 4}
conjunto_l = {1, 2}

conjunto_k.issuperset(conjunto_l) #>>> True
conjunto_l.issuperset(conjunto_k) #>>> False

#idisjoint

conjunto_m = {1, 2, 3}
conjunto_n = {4, 5, 6}
conjunto_o = {3, 4, 5}

conjunto_m.isdisjoint(conjunto_n) #>>> True
conjunto_m.isdisjoint(conjunto_o) #>>> False

# .add

conjunto_p = {1, 2, 3}
conjunto_p.add(4) #>>> {1, 2, 3, 4}

#clear 