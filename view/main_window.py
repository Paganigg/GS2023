from tkinter import *

LARGURA = 40
COLUNA_1 = 1
COLUNA_2 = 3

root = Tk()
root.title("Global Solution 2023")
largura_da_tela = root.winfo_screenwidth()
altura_da_tela = root.winfo_screenheight()
RESOLUCAO = f"{largura_da_tela}x{altura_da_tela}"
root.geometry(RESOLUCAO)

frm = Frame(root)
frm.grid()

def open():
    top = Toplevel()
    top.geometry(RESOLUCAO)
    top.title("Registro médico")
    Button(top, text= "Sair", width= LARGURA, command=top.destroy).pack(pady=520)

botao1 = Button(frm, text = "Registrar médico",  width = LARGURA, height = 5, command = open).grid(column=COLUNA_1, row = 1)
botao2 = Button(frm, text = "Edição de dados médico",  width = LARGURA, command = open).grid(column=COLUNA_1, row = 2)
botao3 = Button(frm, text = "Visualização de dados médico",  width = LARGURA, command = open).grid(column=COLUNA_1, row = 3)

def open():
    top = Toplevel()
    top.geometry(RESOLUCAO)
    top.title("Registro Paciente")
    Button(top, text= "Sair", width= LARGURA, command=top.destroy).pack(pady=520)


botao4 = Button(frm, text = "Registrar paciente",  width = LARGURA, command = open).grid(column=COLUNA_2, row = 1)
botao5 = Button(frm, text = "Edição de dados paciente", width = LARGURA, command = open).grid(column=COLUNA_2, row = 2)
botao6 = Button(frm, text = "Visualização de dados paciente", width = LARGURA, command = open).grid(column=COLUNA_2, row = 3)

botao7 = Button(frm, text = "Sair", width = LARGURA,command=root.destroy).grid(column = 2, row = 4)

root.mainloop()