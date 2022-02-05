# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:11:20 2021

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
        self.btnStart.grid(column=1, row=11, padx=50, pady=22)
        
    def create_form(self):
        #
        self.someSpace = tk.Canvas(self, width=1, height=1, bg="#E4E8CD", highlightthickness=0)
        self.someSpace.grid(row=1, columnspan=3, pady=20)
        #
        self.lblTPorcion = tk.Label(self, text="TAMAÑO DE PORCIÓN: ", bg="#E4E8CD")
        self.lblTPorcion['font']=font.Font(size=12)
        self.lblTPorcion.grid(row=2, pady=15, sticky="e")
        vcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.inPorcion = tk.Entry(self, validate = 'key', validatecommand = vcmd)
        self.inPorcion['font']=font.Font(size=12)
        self.inPorcion.grid(column=1, row=2)
        self.lblPUnits = tk.Label(self, text="* < 250 GRS", bg="#E4E8CD")
        self.lblPUnits['font']=font.Font(size=12)
        self.lblPUnits.grid(column=2, row=2, sticky="w")
        self.lblHBloque = tk.Label(self, text="ALTURA DE LA PASTA: ", bg="#E4E8CD")
        self.lblHBloque['font']=font.Font(size=12)
        self.lblHBloque.grid(row=3, pady=15, sticky="e")
        self.inAltura0 = tk.Entry(self, validate = 'key', validatecommand = vcmd)
        self.inAltura0['font']=font.Font(size=12)
        self.inAltura0.grid(column=1, row=3)
        self.lblAUnits = tk.Label(self, text="* < 30 MM", bg="#E4E8CD")
        self.lblAUnits['font']=font.Font(size=12)
        self.lblAUnits.grid(column=2, row=3, sticky="w")
        self.lblHFinal = tk.Label(self, text="ALTURA FINAL: ", bg="#E4E8CD")
        self.lblHFinal['font']=font.Font(size=12)
        self.lblHFinal.grid(row=4, pady=15, sticky="e")
        self.inAlturaF = tk.Entry(self, validate = 'key', validatecommand = vcmd)
        self.inAlturaF['font']=font.Font(size=12)
        self.inAlturaF.grid(column=1, row=4)
        self.lblAFUnits = tk.Label(self, text="* > 3 MM", bg="#E4E8CD")
        self.lblAFUnits['font']=font.Font(size=12)
        self.lblAFUnits.grid(column=2, row=4, sticky="w")
        
    def show_data(self):
        #
        self.someSpace = tk.Canvas(self, width=1, height=1, bg="#E4E8CD", highlightthickness=0)
        self.someSpace.grid(row=5, columnspan=3, pady=10)
        #
        self.lblCycles = tk.Label(self, text="NÚMERO DE CICLOS ESPERADOS:", bg="#E4E8CD")
        self.lblCycles['font']=font.Font(size=12)
        self.lblCycles.grid(row=6, columnspan=3)
        self.lblCyclesi = tk.Label(self, text="### CICLOS", bg="#E4E8CD")
        self.lblCyclesi['font']=font.Font(size=12, weight="bold")
        self.lblCyclesi.grid(row=7, columnspan=3)
        #
        self.someSpace = tk.Canvas(self, width=1, height=1, bg="#E4E8CD", highlightthickness=0)
        self.someSpace.grid(row=8, columnspan=3, pady=5)
        #
        self.lblTime = tk.Label(self, text="TIEMPO DE LAMINACIÓN APROXIMADO:", bg="#E4E8CD")
        self.lblTime['font']=font.Font(size=12)
        self.lblTime.grid(row=9, columnspan=3)
        self.lblTimei = tk.Label(self, text="### MINUTOS", bg="#E4E8CD")
        self.lblTimei['font']=font.Font(size=12, weight="bold")
        self.lblTimei.grid(row=10, columnspan=3)
        
    def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False
        
root = tk.Tk()
app = StartFrame(master=root)
app.master.title("Laminadora - Main")
app.master.geometry("800x480")
app.mainloop()