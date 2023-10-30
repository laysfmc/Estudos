import tkinter as tk
import sqlite3

def cad_dev():
    #cria e conecta o banco de dados 
    conexao = sqlite3.connect("accioDev.db")
    cursor = conexao.cursor()

    # cria a tabela dev 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dev (
            id INTEGER  PRIMARY KEY AUTOINCREMENT, 
            nome TEXT NOT NULL,
            dataNasc TEXT NOT NULL,
            cidade TEXT, 
            uf TEXT, 
            tel TEXT NOT NULL,
            email TEXT NOT NULL
              
        )
    ''')

    # Inserir dados na tabela
  
    nome = nomeDev.get()
    dataNasc = dataNascDev.get()
    cidade = cidadeDev.get() 
    uf = ufDev.get()
    tel = telDev.get()
    email = emailDev.get()

    cursor.execute("INSERT INTO dev ( nome, dataNasc, cidade, uf, tel, email) VALUES (?, ?, ?, ?, ?, ?)", (nome, dataNasc, cidade, uf, tel, email))

    # Commit e fechar a conexão
    conexao.commit()
    conexao.close()

    # Limpar campos de entrada
    nomeDev.delete(0, 'end')
    dataNascDev.delete(0, 'end')
    cidadeDev.delete(0, 'end')
    ufDev.delete(0, 'end')
    telDev.delete (0, 'end')
    emailDev.delete (0, 'end')

def fechar_janela():
    janela.destroy()

janela = tk.Tk()
janela.title("ACCIO DEVS")


# Labels e campos de entrada
label_nome = tk.Label(janela, text="Nome:")
label_dataNascDev = tk.Label(janela, text="Data de Nascimento:")
label_telDev = tk.Label(janela, text="Telefone:")
label_cidadeDev = tk.Label(janela, text="Cidade:")
label_ufDev = tk.Label(janela, text="UF:")
label_emailDev = tk.Label(janela, text="E-mail:")


nomeDev = tk.Entry(janela)
dataNascDev = tk.Entry(janela)
cidadeDev = tk.Entry(janela)
ufDev = tk.Entry(janela)
telDev = tk.Entry(janela)
emailDev = tk.Entry(janela)


label_nome.grid(row=0, column=0)
label_dataNascDev.grid(row=1, column=0)
label_telDev.grid(row=2, column=0)
label_cidadeDev.grid(row=3, column=0)
label_ufDev.grid(row=4, column=0)
label_emailDev.grid(row=5, column=0)

nomeDev.grid(row=0, column=1)
dataNascDev.grid(row=1, column=1)
cidadeDev.grid(row=2, column=1)
ufDev.grid(row=3, column=1)
telDev.grid(row=4, column=1)
emailDev.grid(row=5, column=1)



# Botões para salvar e fechar
botao_salvar = tk.Button(janela, text="Salvar", command=cad_dev)
botao_fechar = tk.Button(janela, text="Fechar", command=fechar_janela)

botao_salvar.grid(row=6, column=0)
botao_fechar.grid(row=6, column=1)

janela.mainloop()
