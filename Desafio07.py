print ('#### Verificador de Idade ####')

idade = int(input('Digite sua idade:'))

if idade <= 18:
    print(f'Você tem {idade} anos, é menor!')
elif idade >= 60:
    print(f'Você tem {idade} anos, pode ser aposentar!')
else: 
    print(f'Você tem {idade} anos, é maior!')