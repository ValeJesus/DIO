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


#utilizando if/elif/else

MAIOR_IDADE = 18

idade = int(input("Informe a sua idade: "))

if idade >=  MAIOR_IDADE:

    print("Você pode tirar a sua cnh")
elif idade == 17:
    print("ainda falta um ano pra que voce possa tirar sua cnh")

else:
    print("voce nao pode tirar a sua cnh")

# if aninhado

conta_normal = True
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 500
cheque_especial = 1000


if conta_normal:
     if saldo >= saque:
         print("saque realizado com sucesso!")
     elif saldo <= (saldo + cheque_especial ):
         print("saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("saque realizado com sucesso!")
    else:
        print("saldo insuficiente para realizar o saque!")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque!")

elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("Tipo de conta não identificado!")



#IF TERNÁRIO    



status = "Sucesso" if saldo >= saque else "Falha"

print (f"{status} ao realizar o saque!")

