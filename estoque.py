#FUNÇÃO PARA EXIBIR MENU
def exibir_menu():
    print("""
1. Adicionar Produto
2. Ver Produtos em Estoque
3. Atualizar quantidade de um produto
4. Sair                                       
          """)
    return input ('Digite a atividade que deseja realizar:')
#FUNÇÃO PARA ADICIONAR PRODUTO AO ESTOQUE 
def adicionar_produtos():
    nome = input('Informe o Produto:')
    quantidade = input('Digite a quantidade:')
    preco = input('Informe o Preço:')

    with open('estoque.txt', 'a') as arquivo:
        arquivo.write(f'{nome};{quantidade};{preco}\n')
    print('Produto Cadastrado!')

#FUNÇÃO PARA VER OS PRODUTOS CADASTRADOS
def ver_produtos():
    print('--- Destalhamento de Estoque ---')
    try:
        with open('estoque.txt', 'r') as arquivo:
            produtos = arquivo.readlines()
            if produtos:
                for i, produto  in enumerate (produtos, start=1):
                    nome, quantidade, preco = produto.strip().split(';')
                    print(f'{i}. {nome} - QTD: {quantidade} - Preço: R$ {preco}')
            else:
                print('Nenhum produto cadastrado!')  
    except FileNotFoundError:
     print ('Banco de Dados Não Localizado!')   

#FUNÇÃO PARA ATUALIZAR A QUANTIDADE DE UM PRODUTO
def atualizar_produto():
    nome_atualizar = input ('Digite o nome do Produto para Atulizar:')
    qtd_atualizar = input('Digie quantidade atualizada:')

    produtos_atualizados = []
    econtrado = False

    try: 
        with open ('estoque.txt', 'r') as arquivo:
            produtos = arquivo.readlines()

            for produto in produtos:
                 nome, quantidade, preco = produto.strip().split(';')
                 if nome == nome_atualizar:
                    produtos_atualizados.append(f' {nome}; {qtd_atualizar}; {preco} \n')
                    encontrado = True
                 else: 
                    produtos_atualizados(produto)
                
        with open ('estoque.txt', 'w') as arquivo:
         arquivo.writelines(produtos_atualizados)

        if encontrado:
          print('PRODUTO ATUALIZADO')
        else:
          print ('Produto não localizado!') 

    except FileNotFoundError:
       print('Banco de dados não encontrado!')


#FUNÇÃO PRINCICAL PARA O SISTEMA
def sistema_geral():
   while True:
      opcao = exibir_menu()

      if opcao == '1':
       adicionar_produtos()
      elif opcao =='2':
        ver_produtos()
      elif opcao =='3':
        atualizar_produto()
      elif opcao =='4':
        print('Você encerrou o sistema!')
        break
      else:
        print ('Você digitou uma opção inválida, bobão!')



#FUNÇÃO DO SISTEMA
sistema_geral()
