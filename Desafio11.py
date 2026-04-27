import random

aleatorio = random.randint(1,100)

usuario = int(input('Digite o seu palpite:'))

#Repete o comando input até que o usuário digite um 
#Papilte igual ao núm  aleatório
while usuario != aleatorio:
    if usuario < aleatorio:
        usuario = int(input ('Voce errou, digite um palpite maior:'))
    elif usuario > aleatorio:
        usuario = int(input('Voce errou, digite um palpite menor:'))
print ('Voce acertou, parabens!')
