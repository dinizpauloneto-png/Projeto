senha = input('Digite uma senha:')
confirmar = input('Confime sua senha:')

while senha != confirmar:
    confirmar = input ('Você digitou senhas diferentes! Digite novamente:')

print('Acesso liberado!')