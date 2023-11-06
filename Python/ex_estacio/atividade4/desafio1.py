"""
Desafio1: Você vai construir um software para auxiliar no cadastro e no controle dos alunos de uma academia esportiva. 
Para isso crie o banco de dados da academia, crie a tabela cadastro com os dados de código do aluno, nome,
texto e idade. Insira os seus dados e do professor, que irão começar a malhar na próxima semana.
"""
import sqlite3


#Conecta ao banco de dados
conexao = sqlite3.connect('gymDB.db')

#cria um cursor para executar os comandos
cursor = conexao.cursor()

#cria tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cadastro (
        id INTEGER  PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        texto TEXT, 
        idade INTERGER
    )              
''')

#Insere dados do professor
cursor.execute('INSERT INTO Cadastro (nome, texto, idade) VALUES (?, ?, ?)', ('Professor', 'Instrutor', 30))

#Insere dados do usuário 
cursor.execute('INSERT INTO Cadastro (nome, texto, idade) VALUES (?, ?, ?)', ('Lays Fernandes', 'Aluno', 22))

#Salva e fecha o banco de dados 
conexao.commit()
conexao.close()

#print 
print ("Dados inseridos com sucesso!!!")
