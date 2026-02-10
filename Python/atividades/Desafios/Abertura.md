# 📈 Análise de Variação de Ações

## 📌 Descrição
Este programa foi desenvolvido para analisar a variação do preço de uma ação com base nos valores de **abertura** e **fechamento** informados pelo usuário.

A partir da comparação entre esses dois valores, o sistema determina se a ação apresentou:
- **ALTA** → quando o preço de fechamento é maior que o de abertura  
- **BAIXA** → quando o preço de fechamento é menor que o de abertura  
- **ESTÁVEL** → quando os preços são iguais  

O código foi criado como parte de um **desafio introdutório de lógica e condicionais**, sem utilização de bibliotecas externas.

---

## 🧾 Entrada
Uma única linha contendo **dois números inteiros positivos**, separados por espaço:

<preço_de_abertura> <preço_de_fechamento>

shell
Copiar código

### Exemplo de entrada:
10 15

yaml
Copiar código

---

## 📤 Saída
Uma única palavra em letras maiúsculas, conforme a comparação entre os valores:
- `"ALTA"`
- `"BAIXA"`
- `"ESTAVEL"`

### Exemplo de saída:
ALTA

yaml
Copiar código

---

## ⚙️ Lógica de Funcionamento
1. O programa lê a entrada do usuário.
2. Separa os valores de abertura e fechamento.
3. Converte os valores para inteiros.
4. Compara os preços:
   - Se abertura < fechamento → imprime **ALTA**
   - Se abertura > fechamento → imprime **BAIXA**
   - Se forem iguais → imprime **ESTAVEL**

---

## 🧠 Código-fonte

```python
# Lê a linha de entrada e separa os valores
entrada = input()
abertura_str, fechamento_str = entrada.split()

# Converte os valores para inteiros
abertura = int(abertura_str)
fechamento = int(fechamento_str)

# Compara os valores de abertura e fechamento
if abertura > fechamento:
    print("BAIXA")
elif abertura < fechamento:
    print("ALTA")
else:
    print("ESTAVEL")