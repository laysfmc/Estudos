"""
Desafio2:Você vai construir um software para auxiliar no cadastro e no controle dos alunos de uma 
academia esportiva. Para isso crie o banco de dados da academia, crie a tabela cadastro com os dados 
de código do aluno, nome, texto e idade. Insira os seus dados e do professor, que irão começar a malhar
na próxima semana. Ixxi, mas o professor desistiu, agora exclua o nome dele.

"""

import sqlite3

#Conecta ao banco de dados
conexao = sqlite3.connect('gymDB.db')

#cria um cursor para executar os comandos
cursor = conexao.cursor()


#Deleta dados do professor
excluir = 1
cursor.execute('DELETE FROM Cadastro WHERE id = ?', (excluir,))


#Salva e fecha o banco de dados 
conexao.commit()
conexao.close()

#print 
print ("Dados excluídos com sucesso!!!")