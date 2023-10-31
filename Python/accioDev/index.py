import tkinter as tk
import sqlite3
from tkinter import filedialog
import os


def cad_dev():
    
    # Janela Dev
    janelaDev = tk.Toplevel(janela)
    janelaDev.title("Cadastro de Devs:")
    
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
            email TEXT NOT NULL, 
            experiencias TEXT, 
            habilidades TEXT, 
            linkedin TEXT, 
            curriculo BLOB
              
        )
    ''')

    # Inserir dados na tabela
  
    nome = nomeDev.get()
    dataNasc = dataNascDev.get()
    cidade = cidadeDev.get() 
    uf = ufDev.get()
    tel = telDev.get()
    email = emailDev.get()
    experiencias = expDev.get()
    habilidades = habDev.get()
    linkedin = linkedinDev.get()
    

 # Lê o arquivo PDF e converte-o para binário
    curriculo_path = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    if curriculo_path:
        with open(curriculo_path, "rb") as curriculo_file:
            curriculo = curriculo_file.read()
            
    cursor.execute("INSERT INTO dev ( nome, dataNasc, cidade, uf, tel, email, experiencias, habilidades, linkedin, curriculo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (nome, dataNasc, cidade, uf, tel, email, experiencias, habilidades, linkedin, curriculo))

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
    expDev.delete(0, 'end')
    habDev.delete (0, 'end')
    linkedinDev.delete (0, 'end')


def recrutador():
    
    # Janela
    janelaRec = tk.Toplevel(janela)
    janelaRec.title("ACCIO DEVS")
    
    # Conexão
    conexao = sqlite3.connect("accioDev.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM dev")
    dadosDevs = cursor.fetchall()
    
    # Vizualização de dados
    for dados in dadosDevs:
        
        label_dev = tk.Label(janelaRec, text=f"Nome: {dados[1]},  Email: {dados[6]}, Telefone: {dados[5]} ")
        label_dev.pack()
    
    conexao.close()
    



def fechar_janela():
    janela.destroy()

janela = tk.Tk()
janela.title("ACCIO DEVS")


# Criação de um menu
menuAD = tk.Menu(janela)
janela.config(menu=menuAD)
 
menu = tk.Menu(menuAD)
menu.add_cascade(label="MENU", menu=menuAD)
menuAD.add_command(label="Cadastro de Devs")#, command=cad_dev)
menuAD.add_command(label="Vizualizar Devs", command=recrutador)


# Labels e campos de entrada
label_nome = tk.Label(janela, text="Nome:")
label_dataNascDev = tk.Label(janela, text="Data de Nascimento:")
label_telDev = tk.Label(janela, text="Telefone:")
label_cidadeDev = tk.Label(janela, text="Cidade:")
label_ufDev = tk.Label(janela, text="UF:")
label_emailDev = tk.Label(janela, text="E-mail:")
label_expDev = tk.Label(janela, text="Experiencias Profissionais:")
label_habDev = tk.Label(janela, text="Habilidades:")
label_linkedinDev = tk.Label(janela, text="URL LinkedIn:")


nomeDev = tk.Entry(janela)
dataNascDev = tk.Entry(janela)
cidadeDev = tk.Entry(janela)
ufDev = tk.Entry(janela)
telDev = tk.Entry(janela)
emailDev = tk.Entry(janela)
expDev = tk.Entry(janela)
habDev = tk.Entry(janela)
linkedinDev = tk.Entry(janela)

#Tentando deixar bonitinho
fonte = (30)
tk.Label(janela, text="Cadastro", font= fonte).grid (column=0 , row=0)


#Dados Básicos (coluna um e dois)
label_nome.grid(row=1, column=0)
label_dataNascDev.grid(row=2, column=0)
label_telDev.grid(row=3, column=0)
label_cidadeDev.grid(row=4, column=0)
label_ufDev.grid(row=5, column=0)
label_emailDev.grid(row=6, column=0)

nomeDev.grid(row=1, column=1)
dataNascDev.grid(row=2, column=1)
cidadeDev.grid(row=3, column=1)
ufDev.grid(row=4, column=1)
telDev.grid(row=5, column=1)
emailDev.grid(row=6, column=1)


# curriculo (coluna 3 e 4)
label_expDev.grid(row=1, column=4)
label_habDev.grid(row=2, column=4)
label_linkedinDev.grid(row=3, column=4)

expDev.grid(row=1, column=5 )
habDev.grid(row=2, column=5)
linkedinDev.grid(row=3, column=5)

# Botão para fazer o upload do currículo em PDF
botao_upload_curriculo = tk.Button(janela, text="Upload do Currículo (PDF)", command=cad_dev)
botao_upload_curriculo.grid(row=4, column=5)

# Botões para salvar e fechar
botao_salvar = tk.Button(janela, text="Salvar", command=cad_dev)
botao_fechar = tk.Button(janela, text="Fechar", command=fechar_janela)

botao_salvar.grid(row=10, column=1)
botao_fechar.grid(row=10, column=4)

janela.mainloop()
