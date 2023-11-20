from tkinter import ttk
from tkinter import Tk
from tkinter import *


root = Tk()
root.geometry("1920x1080")
frm = ttk.Frame(root, padding=10)
frm.grid()


ttk.Button(frm, text = "Registrar médico",  width = 30).grid(column=10, row = 1)
ttk.Button(frm, text = "Edição de dados médico",  width = 30).grid(column=10, row = 2)
ttk.Button(frm, text = "Visualização de dados médico",  width = 30).grid(column=10, row = 3)

ttk.Button(frm, text = "Registrar paciente",  width = 30).grid(column=30, row = 1)
ttk.Button(frm, text = "Edição de dados paciente", width = 30).grid(column=30, row = 2)
ttk.Button(frm, text = "Visualização de dados paciente", width = 30).grid(column=30, row = 3)

ttk.Button(frm, text = "Sair", width = 30 ,command=root.destroy).grid(column=20, row = 4)

root.mainloop()