#Usuário Digitar 5 nomes
nomes = []

for a in range (1, 6):
    nome = input(f'Digite o {a}º nome:')
    nomes.append(nome)

arquivo = open('nomes.txt', 'w')    

for nome in nomes:
    arquivo.write(nome +'\n')
arquivo.close()    

arquivo = open('nomes.txt', 'r')
conteudo = arquivo.read()

print(f'Os nomes são: \n {conteudo}')