import os 

restaurantes = [{'nome': 'Rochesenha', 'categoria':'Ratatouille (vende ratos)', 'ativo': False  },
                {'nome': 'Restaurante da Nana!', 'categoria':'Fritas','ativo': True },
                {'nome': 'pizion', 'categoria':'Pizzaria', 'ativo': False},
                {'nome': 'Pizzarô', 'categoria':'Pizzaria', 'ativo': True },
                {'nome': 'Bom redondo', 'categoria': 'galinhas', 'ativo': False },
                {'nome': 'Pizza Mia! Co.', 'categoria': 'Pizzaria', 'ativo': True},
                {'nome': 'busgo', 'categoria': 'Gostas d`àgua', 'ativo': True} ]


#'Rochesenha', 'Restaurante da Nana!','pizion', 'Pizzarô', 'Pizza Mia! Co.'


def exibir_nome_do_programa():
    print("""
          
    SABOR EXPRESS                                                        
      
    """)

def exibir_opcoes():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Ativar restaurante')
      print('4. Sair\n')
     
def finalizar_app():
    os.system('cls')
    
    print('Finalizando o app\n')

def opcao_invalida():
    print('Opcao invalida!\n')
    voltar_menu()

def cadastrar_novo_restaurante():
   os.system('cls')
   print('Cadastro de novos restaurantes\n')
   nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
   categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante} : ')
   dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
   restaurantes.append(dados_do_restaurante)
   print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
   
   voltar_menu()

def listar_restaurantes():
   os.system('cls')
   print('Listar todos os restaurantes')

   for restaurante in restaurantes:
      nome_restaurante = restaurante['nome']
      categoria = restaurante['categoria']
      ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'

      print(f'- Nome do restaurante:  {nome_restaurante} | categoria/Vende oque: {categoria} | status: {ativo} ')
 
   voltar_menu()

def alternar_estado_restaurante():
   print('Alterando estado do restaurante')
   nome_restaurante = input('Digite o nome do restaurante que deseja ativar: ')
   restaurante_encontrado = False

   for restaurante in restaurantes:
      if nome_restaurante == restaurante['nome']:
         restaurante_encontrado = True
         restaurante['ativo'] = not restaurante['ativo']
         mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
         print(mensagem)
         voltar_menu()
      if not restaurante_encontrado:
         print('Restaurante não encontrado')
         voltar_menu()

         

   
def voltar_menu():
   
   input('\nDigite uma tecla para voltar ao menu principal')
   main()  

def escolher_opcao():
    try:
      opcao_escolhida = int(input('Escola uma opção: '))
      #opcao_escolhida = int(opcao_escolhida)

      if opcao_escolhida == 1 :
        cadastrar_novo_restaurante()
      elif opcao_escolhida == 2 :
        listar_restaurantes() 
      elif opcao_escolhida == 3 :
        alternar_estado_restaurante()
      elif opcao_escolhida == 4:
        finalizar_app()
      else :
        opcao_invalida()
    except:
       opcao_invalida()

def main():
    
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
      main()
