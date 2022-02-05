# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:02:38 2021

@author: HAPS
"""

import tkinter as tk
import tkinter.font as font

class StartFrame(tk.Frame):    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(background="#E4E8CD")
        self.pack()
        self.create_widgets()
        self.portion = 200
        self.hBloque = 25
        self.create_form()
        self.show_data()
        
    def create_widgets(self):
        self.btnHistory = tk.Button(self, text="HISTORIAL", relief=tk.FLAT) #COMMAND_HISTORY
        self.btnHistory['font']=font.Font(size=15)
        self.btnHistory.grid(column=0, row=0, padx=60, pady=10)
        self.lblStatus = tk.Label(self, text="", bg="#E4E8CD", width=15)
        self.lblStatus['font']=font.Font(size=15)
        self.lblStatus.grid(column=1, row=0, padx=60, pady=10)
        self.btnTemp = tk.Button(self, text="TEMPERATURA", relief=tk.FLAT) #COMMAND_TEMPERATURE & DATA
        self.btnTemp['font']=font.Font(size=15)
        self.btnTemp.grid(column=2, row=0, padx=50, pady=10)
        self.btnStart = tk.Button(self, text="CONFIRMAR", relief=tk.FLAT, bg="#BDF271") #COMMAND->main
        self.btnStart['font']=font.Font(size=15)
        self.btnStart.grid(column=1, row=12, padx=50, pady=22)
        
    def create_form(self):
        #
        self.someSpace = tk.Canvas(self, width=1, height=1, bg="#E4E8CD", highlightthickness=0)
        self.someSpace.grid(row=1, columnspan=3, pady=7)
        #
        self.lblTPorcion = tk.Label(self, text="TAMAÑO DE PORCIÓN: ", bg="#E4E8CD")
        self.lblTPorcion['font']=font.Font(size=12)
        self.lblTPorcion.grid(row=2, pady=15, sticky="e")
        self.btnDPorcion = tk.Button(self, text="DISMINUIR", bg="#E4E8CD")
        self.btnDPorcion['font']=font.Font(size=10)
        self.btnDPorcion.grid(column=1, row=2, sticky="w", padx="45")
        self.btnUPorcion = tk.Button(self, text="AUMENTAR", bg="#E4E8CD")
        self.btnUPorcion['font']=font.Font(size=10)
        self.btnUPorcion.grid(column=1, row=2, sticky="e", padx="45")
        self.lbliPorcion = tk.Label(self, text="* < 250 GRS", bg="#E4E8CD")
        self.lbliPorcion['font']=font.Font(size=12)
        self.lbliPorcion.grid(column=2, row=2, sticky="w")        
        self.lblHBloque = tk.Label(self, text="ALTURA DE LA PASTA: ", bg="#E4E8CD")
        self.lblHBloque['font']=font.Font(size=12)
        self.lblHBloque.grid(row=3, pady=15, sticky="e")
        self.btnDHBloque = tk.Button(self, text="DISMINUIR", bg="#E4E8CD")
        self.btnDHBloque['font']=font.Font(size=10)
        self.btnDHBloque.grid(column=1, row=3, sticky="w", padx="45")
        self.btnUHBloque = tk.Button(self, text="AUMENTAR", bg="#E4E8CD")
        self.btnUHBloque['font']=font.Font(size=10)
        self.btnUHBloque.grid(column=1, row=3, sticky="e", padx="45")
        self.lblAUnits = tk.Label(self, text="* < 30 MM", bg="#E4E8CD")
        self.lblAUnits['font']=font.Font(size=12)
        self.lblAUnits.grid(column=2, row=3, sticky="w")
        self.lblHFinal = tk.Label(self, text="ALTURA FINAL: ", bg="#E4E8CD")
        self.lblHFinal['font']=font.Font(size=12)
        self.lblHFinal.grid(row=4, columnspan="3", pady=15)
        self.btnHB3 = tk.Button(self, text="  3  MM  ", bg="#E4E8CD")
        self.btnHB3['font']=font.Font(size=10)
        self.btnHB3.grid(column=0, row=5, padx="45", sticky="e")
        self.btnHB5 = tk.Button(self, text="  5  MM  ", bg="#E4E8CD")
        self.btnHB5['font']=font.Font(size=10)
        self.btnHB5.grid(column=1, row=5, padx="45", sticky="w")
        self.btnHB8 = tk.Button(self, text="  8  MM  ", bg="#E4E8CD")
        self.btnHB8['font']=font.Font(size=10)
        self.btnHB8.grid(column=1, row=5, padx="45", sticky="e")
        self.btnHB10 = tk.Button(self, text="  10 MM  ", bg="#E4E8CD")
        self.btnHB10['font']=font.Font(size=10)
        self.btnHB10.grid(column=2, row=5, padx="45", sticky="w")
        
    def show_data(self):
        #
        self.someSpace = tk.Canvas(self, width=1, height=1, bg="#E4E8CD", highlightthickness=0)
        self.someSpace.grid(row=6, columnspan=3, pady=10)
        #
        self.lblCycles = tk.Label(self, text="NÚMERO DE CICLOS ESPERADOS:", bg="#E4E8CD")
        self.lblCycles['font']=font.Font(size=12)
        self.lblCycles.grid(row=7, columnspan=3)
        self.lblCyclesi = tk.Label(self, text="### CICLOS", bg="#E4E8CD")
        self.lblCyclesi['font']=font.Font(size=12, weight="bold")
        self.lblCyclesi.grid(row=8, columnspan=3)
        #
        self.someSpace = tk.Canvas(self, width=1, height=1, bg="#E4E8CD", highlightthickness=0)
        self.someSpace.grid(row=9, columnspan=3, pady=5)
        #
        self.lblTime = tk.Label(self, text="TIEMPO DE LAMINACIÓN APROXIMADO:", bg="#E4E8CD")
        self.lblTime['font']=font.Font(size=12)
        self.lblTime.grid(row=10, columnspan=3)
        self.lblTimei = tk.Label(self, text="### MINUTOS", bg="#E4E8CD")
        self.lblTimei['font']=font.Font(size=12, weight="bold")
        self.lblTimei.grid(row=11, columnspan=3)
        
    def portion_inc(self):
        
        
root = tk.Tk()
app = StartFrame(master=root)
app.master.title("Laminadora - Main")
app.master.geometry("800x480")
app.mainloop()