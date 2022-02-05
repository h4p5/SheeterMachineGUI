# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:48:19 2021

@author: HAPS
"""

import tkinter as tk
import tkinter.font as font

class AlarmFrame(tk.Frame):    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(background="#E4E8CD")
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.btnHistory = tk.Button(self, text="HISTORIAL", relief=tk.FLAT) #COMMAND_HISTORY
        self.btnHistory['font']=font.Font(size=15)
        self.btnHistory.grid(column=0, row=0, padx=60, pady=10)
        self.lblStatus = tk.Label(self, text="STATUS", bg="#FF0000", width=15)
        self.lblStatus['font']=font.Font(size=15)
        self.lblStatus.grid(column=1, row=0, padx=60, pady=10)
        self.btnTemp = tk.Button(self, text="TEMPERATURA", relief=tk.FLAT) #COMMAND_TEMPERATURE & DATA
        self.btnTemp['font']=font.Font(size=15)
        self.btnTemp.grid(column=2, row=0, padx=50, pady=10)
        self.show_alert()
        self.show_tags()
        self.show_info()
        
    def show_alert(self):
        self.stop = tk.PhotoImage(file="IMGS/Alarm.png")
        self.imgStop = tk.Canvas(self, width=800, height=260, highlightthickness=0, bg="#E4E8CD")
        self.imgStop.create_image(0,0, anchor='nw', image=self.stop)
        self.imgStop.grid(row=1, columnspan=3, rowspan=2, pady=19)
    
    def show_tags(self):
        self.lblG0 = tk.Label(self, text="GROSOR INICIAL", bg="#E4E8CD")
        self.lblG0['font']=font.Font(size=12)
        self.lblG0.grid(row=3)
        self.lblGA = tk.Label(self, text="GROSOR ACTUAL", bg="#E4E8CD")
        self.lblGA['font']=font.Font(size=12)
        self.lblGA.grid(column=1, row=3)
        self.lblGF = tk.Label(self, text="GROSOR FINAL", bg="#E4E8CD")
        self.lblGF['font']=font.Font(size=12)
        self.lblGF.grid(column=2, row=3)
        self.br = tk.PhotoImage(file="IMGS/br.png")
        self.imgBr = tk.Canvas(self, width=700, height=3, bg="#E4E8CD", highlightthickness=0)
        self.imgBr.create_image(0,0, anchor='nw', image=self.br)
        self.imgBr.grid(row=5, columnspan=3, pady=12)
        self.lblCR = tk.Label(self, text="CICLOS REALIZADOS", bg="#E4E8CD")
        self.lblCR['font']=font.Font(size=12)
        self.lblCR.grid(row=6) #padx=50
        self.lblCA = tk.Label(self, text="CICLO ACTUAL", bg="#E4E8CD")
        self.lblCA['font']=font.Font(size=12)
        self.lblCA.grid(column=1, row=6)
        self.lblCRe = tk.Label(self, text="CICLOS RESTANTES", bg="#E4E8CD")
        self.lblCRe['font']=font.Font(size=12)
        self.lblCRe.grid(column=2, row=6)
    
    def show_info(self):
        self.lblG0i = tk.Label(self, text="### mm", bg="#E4E8CD") #DATA
        self.lblG0i['font']=font.Font(size=11)
        self.lblG0i.grid(row=4)
        self.lblGAi = tk.Label(self, text="### mm", bg="#E4E8CD") #DATA
        self.lblGAi['font']=font.Font(size=11)
        self.lblGAi.grid(column=1, row=4)
        self.lblGFi = tk.Label(self, text="### mm", bg="#E4E8CD") #DATA
        self.lblGFi['font']=font.Font(size=11)
        self.lblGFi.grid(column=2, row=4)
        self.lblCRi = tk.Label(self, text="###", bg="#E4E8CD") #DATA
        self.lblCRi['font']=font.Font(size=11)
        self.lblCRi.grid(row=7)
        self.lblCAi = tk.Label(self, text="###", bg="#E4E8CD") #DATA
        self.lblCAi['font']=font.Font(size=11)
        self.lblCAi.grid(column=1, row=7)
        self.lblCRei = tk.Label(self, text="###", bg="#E4E8CD") #DATA
        self.lblCRei['font']=font.Font(size=11)
        self.lblCRei.grid(column=2, row=7)
        
root = tk.Tk()
app = AlarmFrame(master=root)
app.master.title("Laminadora - Main")
app.master.geometry("800x480")
app.mainloop()