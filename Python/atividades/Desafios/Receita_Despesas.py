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