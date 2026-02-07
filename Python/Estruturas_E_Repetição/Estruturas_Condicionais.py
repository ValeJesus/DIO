saldo = 2000.0
saque = float(input("informe o valor do saque:"))

if saldo >= saque:
    print("Realizado o saque!")

if saldo < saque:
    print("Saldo insuficiente para realizar o saque!")


#ou fazer utilizando if/else

if saldo>= saque:
    print("Realizando o saque!")
else:
    print("Saldo insuficiente para realizar o saque!")