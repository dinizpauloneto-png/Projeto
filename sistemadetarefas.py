def exibir_menu():
    print(f'### Sistema de Tarefas ### \n'
          f'1. Adicionar Tarefa com prazo \n'
          f'2. Ver tarefas pendentes \n'
          f'3. Ver tarefas concluídas \n'
          f'4. Marcar tarefas como concluída \n'
          f'5. Sair')
    return input ('Escolha uma Opção:')

def adicionar_tarefa():
    tarefa = input('Digite a Tarefa que você deseja adicionar: ')
    prazo = input('Digite o prazo da tarefa (dd/mm/aaa): ')

    with open('tarefas.txt', 'a') as arquivo:
        arquivo.write(f'{tarefa},{prazo},pendente \n')

        print('Tarefa Adiconada com Sucesso!')

adicionar_tarefa()        