linguagens = ["Python", "Java", "C#", "JavaScript", "Ruby"]

print(linguagens.index("Java"))
print(linguagens.index("C#"))

# copy [] -> cria uma nova lista com os mesmos elementos da lista original

lista = [1, 2, 3, 4, 5]

l2  = lista.copy()

print(lista)
print(id(l2), id(lista))

#count [] -> conta quantas vezes um elemento aparece na lista
cores = ["vermelho", "azul", "verde", "amarelo", "azul"]

cores.count ("azul") #>>> 2
cores.count ("vermelho") #>>> 1

#extend [] -> estende a lista com os elementos de outra lista

linguagens2 = ["Go", "Rust", "Kotlin"]

print(linguagens2) #>>> ['Go', 'Rust', 'Kotlin']

linguagens2.extend(["Swift", "Dart"])

print(linguagens2) # >>> ['Go', 'Rust', 'Kotlin', 'Swift', 'Dart']

#index [] -> retorna o índice da primeira ocorrência de um elemento na lista

linguagens3 = ["Python", "Java", "C#", "JavaScript", "Ruby"]

linguagens3.index("Java") #>>> 1
linguagens3.index("C#") #>>> 2
linguagens3.index("Python") #>>> 0

#pop [] -> remove e retorna o elemento de um índice específico da lista

linguagens4 = ["Python", "Java", "C#", "JavaScript", "Ruby"]

linguagens4.pop(1) #>>> 'Java'
linguagens4.pop() #>>> 'Ruby'
linguagens4.pop() #>>> 'JavaScript'


#remove [] -> remove a primeira ocorrência de um elemento específico da lista

linguagens5 = ["Python", "Java", "C#", "JavaScript", "Ruby"]

linguagens5.remove("C#") #>>> ['Python', "Java", "JavaScript", "Ruby"]

#sort

linguagens6 = ["python", "java", "c#", "javascript", "ruby"]
linguagens6.sort()
print(linguagens6) #>>> ['c#', 'java', 'javascript', 'python', 'ruby']

linguagens7 = ["python", "java", "c#", "javascript", "ruby"]
linguagens7.sort(reverse=True)
print(linguagens7) #>>> ['ruby', 'python', 'javascript', 'java', 'c#']

linguagens8 = ["python", "java", "c#", "javascript", "ruby"]
linguagens8.sort(key=lambda x: len(x))
print(linguagens8) #>>> ['c#', 'java', 'ruby', 'python', 'javascript']

linguagens9 = ["python", "java", "c#", "javascript", "ruby"]
linguagens9.sort(key=lambda x: len(x), reverse=True)
print(linguagens9) #>>> ['javascript', 'python', 'ruby', 'java', 'c#']

#len

linguagens10 = ["python", "java", "c#", "javascript", "ruby"]

len(linguagens10) #>>> 5

#sorted

linguagens11 = ["python", "java", "c#", "javascript", "ruby"]   

sorted(linguagens11, key=lambda x: len(x))
sorted(linguagens11, key=lambda x: len(x), reverse=True)