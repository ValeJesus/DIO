idade = 19
e_estudante = True

if idade < 18:
    print("Você tem desconto pois é menor de idade")

if e_estudante == True:
    print("Você tem desconto pois é estudante")

elif e_estudante == False and idade >= 18:
    print("Você não tem desconto")
      