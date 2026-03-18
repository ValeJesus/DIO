# 🔤 Padronização de Nome do Destinatário

## 📌 Descrição
Este programa foi desenvolvido para padronizar o nome do destinatário de uma transferência bancária, convertendo todas as letras para **maiúsculas**.

No contexto de um banco digital, essa padronização ajuda a evitar erros de digitação e inconsistências nos registros, garantindo que nomes sejam tratados de forma uniforme pelos sistemas automatizados, independentemente de como o cliente os digitou.

O programa **não utiliza bibliotecas externas** e preserva espaços, números e caracteres especiais, alterando apenas letras minúsculas para maiúsculas.

---

## 🧾 Entrada
Uma única linha contendo uma **string** que representa o nome do destinatário da transferência.

A string pode conter:
- Letras
- Números
- Espaços
- Outros caracteres não alfabéticos

### Exemplo de entrada:
joao silva

yaml
Copiar código

---

## 📤 Saída
Uma única linha contendo a **mesma string da entrada**, porém com **todas as letras convertidas para maiúsculas**.

### Exemplo de saída:
JOAO SILVA

yaml
Copiar código

---

## ⚙️ Lógica de Funcionamento
1. O programa lê o nome do destinatário digitado pelo usuário.
2. Utiliza o método `.upper()` da linguagem Python.
3. Converte todas as letras minúsculas em maiúsculas.
4. Mantém inalterados números, espaços e outros caracteres.
5. Imprime o resultado final.

---

## 🧠 Código-fonte

```python
# Lê o nome do destinatário da transferência
nome_destinatario = input()

# Converte todas as letras para maiúsculas e imprime o resultado
print(nome_destinatario.upper())