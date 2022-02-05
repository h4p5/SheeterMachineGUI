# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:54:01 2021

@author: HAPS
"""

import tkinter as tk
import tkinter.font as font

class CompletedFrame(tk.Frame):    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(background="#E4E8CD")
        self.pack()
        self.create_widgets()
        self.show_img()
        self.show_tags()
        self.show_info()
        
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
        self.btnStart = tk.Button(self, text="VOLVER A INICIO", relief=tk.FLAT) #COMMAND->main
        self.btnStart['font']=font.Font(size=15)
        self.btnStart.grid(column=1, row=11, padx=50, pady=22)
        
    def show_img(self):
        self.stop = tk.PhotoImage(file="IMGS/Done.png")
        self.imgStop = tk.Canvas(self, width=800, height=260, highlightthickness=0, bg="#E4E8CD")
        self.imgStop.create_image(0,0, anchor='nw', image=self.stop)
        self.imgStop.grid(row=1, columnspan=3, pady=14)
        
    def show_tags(self):
        self.lblG0 = tk.Label(self, text="CICLOS REALIZADOS", bg="#E4E8CD")
        self.lblG0['font']=font.Font(size=12)
        self.lblG0.grid(row=2)
        self.lblGA = tk.Label(self, text="TIEMPO TRANSCURRIDO", bg="#E4E8CD")
        self.lblGA['font']=font.Font(size=12)
        self.lblGA.grid(column=1, row=2)
        self.lblGF = tk.Label(self, text="GROSOR FINAL", bg="#E4E8CD")
        self.lblGF['font']=font.Font(size=12)
        self.lblGF.grid(column=2, row=2)
        
    def show_info(self):
        self.lblG0i = tk.Label(self, text="###", bg="#E4E8CD") #DATA
        self.lblG0i['font']=font.Font(size=11)
        self.lblG0i.grid(row=3)
        self.lblGAi = tk.Label(self, text="### MINUTOS", bg="#E4E8CD") #DATA
        self.lblGAi['font']=font.Font(size=11)
        self.lblGAi.grid(column=1, row=3)
        self.lblGFi = tk.Label(self, text="### mm", bg="#E4E8CD") #DATA
        self.lblGFi['font']=font.Font(size=11)
        self.lblGFi.grid(column=2, row=3)
        
root = tk.Tk()
app = CompletedFrame(master=root)
app.master.title("Laminadora - Main")
app.master.geometry("800x480")
app.mainloop()