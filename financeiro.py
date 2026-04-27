#Criando uma lista vazia para armazenar as informações de receita e despesas.
transacoes = []
#BLOCO QUE VAI FAZER REPETIR 
while True:
    #MONSTRANDO UM MENU DE OPÇÕES AO USUÁRIO
    print(f' #### Sistema financeiro#### \n'
          f' 1. Registrar Receita \n'
          f' 2. Registrar Despesas \n'
          f' 3. Ver Transações \n'
          f' 4. Ver Saldo \n'
          f' 5. Sair \n')
    
    #Variavel que armazena qual função usuário quer realizar
    opcao = int(input('Informe o Nº da opção que deseja realizar:'))

    if opcao == 1:
        descricao = input('Descreva a Receita Gerada:')

        while True:
            try:
                valor = float(input('Informe o Valor da Receira:'))
                if valor > 0:
                    transacoes.append(('Receita:', descricao, valor))
                    print ('Receita registrada com sucesso!')
                    break
                else:
                    print('Você digitou um número inválido')
            except ValueError:
               print('Informação digitada é inválida!')
    elif opcao == 2:
        descricao = input('Descreva a Despesa Gerada:')

        while True:
            try:
                valor = float(input('Informe o Valor da Despesa:'))
                if valor > 0:
                    transacoes.append(('Despesa:', descricao, valor))
                    print ('Despesa registrada com sucesso!')
                    break
                else:
                    print('Você digitou um número inválido')
            except ValueError:
               print('Informação digitada é inválida!') 
    elif opcao == 3:
        if transacoes:
            print('#### Registro Financeiro ####')

            for transacao in transacoes:
                tipo, descricao, valor = transacao
                print(f' Tipo: {tipo} {descricao} - Valor (R$): {valor}')
    elif opcao == 4:
        saldo = 0
        for transacao in transacoes:
            tipo, descricao, valor = transacao
            if tipo == 'Receita:':
                saldo += valor
            else:
                saldo -= valor
        print(f' O Saldo atual é: {saldo}')        
    elif opcao == 5:
        print('Programa encerrado!')
        break
    else:
        print('Você digitou uma opção inválida!')            