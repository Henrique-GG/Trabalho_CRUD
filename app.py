import customtkinter as ctk
import mysql.connector
from tkinter import messagebox, END

# =============================
# CONFIGURAÇÃO DO CUSTOMTKINTER
# =============================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("cor.json")

# =============================
# CONEXÃO COM O BANCO
# =============================
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Henrique1109",  # coloque sua senha se tiver
        database="crud_gui"
    )

# =============================
# FUNÇÕES CRUD
# =============================
def carregar_registros():
    for linha in tabela.get_children():
        tabela.delete(linha)

    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM cursos")
    for row in cursor.fetchall():
        tabela.insert("", END, values=row)
    con.close()

def adicionar():
    nome = entry_nome.get()
    if nome == "":
        messagebox.showwarning("Aviso", "Digite o nome do curso.")
        return
    
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO cursos (nome) VALUES (%s)", (nome,))
    con.commit()
    con.close()
    entry_nome.delete(0, END)
    carregar_registros()
    messagebox.showinfo("Sucesso", "Curso inserido!")

def selecionar_item(event):
    item = tabela.focus()
    if item:
        valores = tabela.item(item)["values"]
        entry_id.delete(0, END)
        entry_nome.delete(0, END)
        entry_id.insert(0, valores[0])
        entry_nome.insert(0, valores[1])

def atualizar():
    id_curso = entry_id.get()
    nome = entry_nome.get()
    
    if id_curso == "":
        messagebox.showwarning("Aviso", "Selecione um curso na lista.")
        return

    con = conectar()
    cursor = con.cursor()
    cursor.execute("UPDATE cursos SET nome=%s WHERE id=%s", (nome, id_curso))
    con.commit()
    con.close()
    carregar_registros()
    messagebox.showinfo("Sucesso", "Curso atualizado!")

def deletar():
    id_curso = entry_id.get()
    
    if id_curso == "":
        messagebox.showwarning("Aviso", "Selecione um curso para excluir.")
        return

    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM cursos WHERE id=%s", (id_curso,))
    con.commit()
    con.close()
    carregar_registros()
    entry_id.delete(0, END)
    entry_nome.delete(0, END)
    messagebox.showinfo("Sucesso", "Curso excluído!")

# =============================
# INTERFACE GRÁFICA
# =============================
app = ctk.CTk()
app.title("CRUD - Cursos (customtkinter + MySQL)")
app.geometry("600x500")

frame = ctk.CTkFrame(app)
frame.pack(pady=20)

# Campos
ctk.CTkLabel(frame, text="ID").grid(row=0, column=0)
entry_id = ctk.CTkEntry(frame, width=100)
entry_id.grid(row=0, column=1, padx=10, pady=5)

ctk.CTkLabel(frame, text="Nome do Curso").grid(row=1, column=0)
entry_nome = ctk.CTkEntry(frame, width=200)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

# Botões
btn_add = ctk.CTkButton(frame, text="Adicionar", command=adicionar)
btn_add.grid(row=2, column=0, pady=10)

btn_update = ctk.CTkButton(frame, text="Atualizar", command=atualizar)
btn_update.grid(row=2, column=1, pady=10)

btn_del = ctk.CTkButton(frame, text="Deletar", command=deletar)
btn_del.grid(row=2, column=2, pady=10)

# tabela (Treeview)
from tkinter import ttk

tabela = ttk.Treeview(app, columns=("ID", "Nome"), show="headings")
tabela.heading("ID", text="ID")
tabela.heading("Nome", text="Nome")
tabela.pack(pady=20)

tabela.bind("<ButtonRelease-1>", selecionar_item)

# Carregar dados no início
carregar_registros()

app.mainloop()
