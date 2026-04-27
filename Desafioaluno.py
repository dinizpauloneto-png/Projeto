#Criando uma lista para guardar os dados dos alunos
alunos = []
while True:
    print(f' ### Sistema de gestão escolar ### \n'
         f'1. Adcionar Novo Aluno \n'
         f'2. Ver Alunos Cadastrados \n'
         f'3. Finalizar Programa')
    
    opcao = int(input ('Informe qual tarefa deseja realizar (1,2,3): ')) 
    if opcao == 1:
        #Receber o nome do Aluno
        nome = input ('Nome do Aluno:')
        #Criando lista vazia para armazenar as notas do aluno
        notas = []
        #Loop que se repete três vezes para pegar a nota 
        for i in range (1,4):
            #Recebendo a nota do aluno 
            nota = float(input (f'Informe a {i}º do Aluno:'))
            #Adicionando variável nota dentro da lista notas    
            notas.append(nota)
        #Somando lista notas e divindo por 3 para média aritmétrica  
        media = sum(notas)/3    

        alunos.append((nome, notas, media))
        #Mostrando mensagem de confirmação
        print (f'O aluno {nome} foi cadastrado com sucesso!')

    #Verifica se o professor escolheu a opção 2
    elif opcao == 2:
        #Verifica se exixte algo na lista Alunos
        if alunos:
            print('### Lista de Alunos###')
        #Percorrer a lista e mostrar item por intem
            for aluno in alunos:
                #Desfragmentar a lista da posição 
                nome, nota,  media = aluno
                print(f' Aluno: {nome} \n'
                f' Notas: {nota} \n'
                f' Média: {media} \n') # :. 2f controla casa decimal
            else:
                print('não há alunos cadastrados!')
    #Verufuca se o professor escolheu opção 3
    elif opcao == 3:
        print ('Programa Finanlizado!')
        break #Para o While Tue inicial evitando programa infinito
    else: 
        print('Você digitou uma opção inválida. Tente novamente!')