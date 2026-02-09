#Bloco em java

#void sacar( double valor ) {
   
   #if (this.saldo >= valor) {
       
    #     this.saldo -= valor;

   #}

#}

#Bloco em python

def sacar(self, valor: float) -> None: # início do bloco do método

    if self.saldo >= valor: # início do bloco if

        self.saldo -= valor 

        # fim do bloco if

# fim do bloco do método

def sacar2(valor):
    saldo = 200

    if saldo >= valor:
          print("valor sacado!")
          print("retire o seu dinheiro na boca do caixa")

    print("Obrigado por ser nosso cliente, volte sempre")


def depositar(valor):
         saldo = 500
         saldo += valor



sacar2(1000)