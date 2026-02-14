# 💰 Saldo Diário de Receitas e Despesas

## 📌 Descrição
Este programa foi desenvolvido para organizar e processar os lançamentos diários de receitas e despesas de um banco. Cada lançamento é registrado com um tipo (R para receita ou D para despesa) seguido do valor em reais.

O sistema calcula automaticamente o **saldo final do dia**, que é a soma de todas as receitas menos a soma de todas as despesas. O resultado é apresentado com exatamente duas casas decimais, mesmo que o valor seja inteiro.

O código foi criado como parte de um **desafio de processamento de strings e manipulação de dados**, sem utilização de bibliotecas externas.

---

## 🧾 Entrada
Uma única linha contendo **lançamentos separados por vírgula**. Cada lançamento é composto por:
- Uma letra: `R` (receita) ou `D` (despesa)
- Um espaço
- Um valor decimal positivo

### Exemplo de entrada:
```
R 100.00,D 50.00,R 20.00
```

---

## 📤 Saída
Uma única linha contendo o **saldo final do dia com duas casas decimais**.

O saldo pode ser:
- **Positivo** → quando os recebimentos superam as despesas
- **Negativo** → quando as despesas superam os recebimentos
- **Zero** → quando receitas e despesas se equilibram

### Exemplo de saída:
```
70.00
```

---

## ⚙️ Lógica de Funcionamento
1. O programa lê a linha contendo os lançamentos.
2. Divide os lançamentos pela vírgula.
3. Para cada lançamento:
   - Extrai o tipo (R ou D) e o valor
   - Se for receita (R), **soma** o valor ao saldo
   - Se for despesa (D), **subtrai** o valor do saldo
4. Exibe o saldo final com exatamente 2 casas decimais

---

## 📊 Exemplos de Teste

| Entrada | Saída |
|---------|-------|
| `R 100.00,D 50.00,R 20.00` | `70.00` |
| `R 10.00,R 25.50,R 14.50` | `50.00` |
| `R 200.00` | `200.00` |
| `D 100.00,D 50.00` | `-150.00` |

---

## 🧠 Código-fonte

```python
# Lê a linha de lançamentos do stdin
entrada = input().strip()

# Inicialize o saldo do dia
saldo = 0.0

# Divide os lançamentos pela vírgula
lancamentos = entrada.split(',')

for lancamento in lancamentos:
    tipo, valor = lancamento.strip().split()
    valor = float(valor)
    if tipo == 'R':
        saldo += valor
    elif tipo == 'D':
        saldo -= valor

# Imprima o saldo final com duas casas decimais
print(f"{saldo:.2f}")
```
