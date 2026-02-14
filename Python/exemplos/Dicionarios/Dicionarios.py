# Exemplo 1, valores mutaveis


pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

pessoa = dict(nome="João", idade=30, cidade="São Paulo")

pessoa["nome"] = "Joao"

# acessar os dados

dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

dados["nome"]
dados["idade"]
dados["cidade"]


# dicionario aninhado

contatos = {
    "João": {"telefone": "123456789", "email": "joao@example.com"},
    "Maria": {"telefone": "987654321", "email": "maria@example.com" }
}

contatos["João"]["telefone"] #>>> "123456789"
contatos["Maria"]["email"] #>>> "maria@example.com"


# Anotacoes: metodos da classe dict
# Os exemplos abaixo mostram o efeito mais comum de cada metodo.

dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# get: retorna o valor ou um padrao se a chave nao existir
dados.get("nome") #>>> "João"
dados.get("cpf") #>>> None
dados.get("cpf", "nao informado") #>>> "nao informado"

# keys / values / items: visoes (views) dinamicas
dados.keys() #>>> dict_keys(["nome", "idade", "cidade"])
dados.values() #>>> dict_values(["João", 30, "São Paulo"])
dados.items() #>>> dict_items([("nome", "João"), ("idade", 30), ("cidade", "São Paulo")])

# update: mescla outro dict ou iteravel de pares
dados.update({"idade": 31, "pais": "Brasil"})

# setdefault: retorna o valor; se nao existir, cria com o padrao
dados.setdefault("estado", "SP") #>>> "SP"
dados.setdefault("cidade", "RJ") #>>> "São Paulo"

# pop: remove e retorna o valor da chave
dados.pop("idade") #>>> 31

# popitem: remove e retorna o ultimo par inserido (LIFO no CPython)
dados.popitem() #>>> ("estado", "SP")

# clear: remove todos os itens
dados.clear() #>>> {}

# copy: copia rasa (shallow copy)
origem = {"numeros": [1, 2, 3]}
clone = origem.copy()
clone["numeros"].append(4)  s
origem #>>> {"numeros": [1, 2, 3, 4]}

# fromkeys: cria dict com as chaves e um valor padrao compartilhado
chaves = ["a", "b", "c"]
dict.fromkeys(chaves, 0) #>>> {"a": 0, "b": 0, "c": 0}

# in: verifica existencia de chave
"nome" in dados #>>> False (dados foi limpo)