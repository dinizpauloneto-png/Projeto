num1 = int(input('Digite o pirmeiro numero:'))
num2 = int(input('Digite o segundo numero:'))

opera = input ('Digite a Operação que deseja realizar:')

if opera == '+':
    resul = num1 + num2
    print (f'O resultado de {num1} + {num2} = {resul}')
elif opera == '-':
    resul = num1 - num2
    print (f' O resultado de {num1} - {num2} = {resul}')
elif opera == '*':
    resul = num1 * num2
    print (f' O resultado de {num1} * {num2} = {resul}')
else:     
    result = num1 / num2
    print(f'O resultado de {num1} / {num2} = {result}')