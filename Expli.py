import random

aleatorio = random.randint(1, 100)
vidas = 7
cont = 0

while True:
    while cont < vidas:
        palpite = int(input('Digite seu palpite: '))
        cont += 1
        if palpite > aleatorio and cont <= vidas:
            print('Seu palpite foi maior que o número aleatório!')
            
        elif palpite < aleatorio and cont <= vidas:
            print('Seu palpite é menor que o número aleatório!')
            
        elif palpite == aleatorio and cont <= vidas:
            print('Você venceu!!!')
    print('Suas chances encerraram!')
    novamente = input('Você deseja jogar novamente? (s/n)')
    if novamente == 'n':
        print('Programa Encerrado!')
        break
    else:
        cont = 0