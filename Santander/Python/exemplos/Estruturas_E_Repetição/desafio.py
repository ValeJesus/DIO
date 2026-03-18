entrada = int(input ("Digite o valor: "))
fechamento = int(input ("Digite o valor de fechamento: "))

if entrada > fechamento:
    print("BAIXA")
elif entrada < fechamento:
    print("ALTA")
else:
    print("ESTAVEL")