#Recebe do unuário um valor inteiro e guarda na variável 'numero'
numero = int(input("Digite um número inteiro: "))

#Variável 'contabem' que armazena o valor inicial 1
contagem = 1

#Mostra na tela qual foi o número escolhido pelo usuário
print(f" Tabuaba de {numero}:")

#Enquanto o valor contagem for menor que 10, executa as linhas abaixo
while contagem <= 10:
    print (f"{numero} x {contagem} = {numero * contagem}")
    #soma acumulada
    contagem += 1



