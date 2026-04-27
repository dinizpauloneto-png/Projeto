import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="sistema_tarefas"
        )
        return conexao
    except Error as e:
        print('Erro ao se comunicar ao MySQL:', e)
        return None

if __name__== "__main__":
    conexao = conectar()
    if conexao:
        print ('Conexão Estabelecida com Sucesso!')
    else:
        print ('Falha ao conectar com base de Dados!')