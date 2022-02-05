# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 23:40:25 2021

@author: HAPS
"""

import tkinter as tk
import tkinter.font as font

class TemperatureFrame(tk.Frame):    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(background="#E4E8CD")
        self.pack()
        self.create_widgets()
        self.show_data()
        
    def create_widgets(self):
        self.lblHistory = tk.Label(self, text="TEMPERATURAS", width=15, bg="#E4E8CD")
        self.lblHistory['font']=font.Font(size=25, weight="bold")
        self.lblHistory.grid(columnspan=2, row=0, padx=245, pady=15)
        self.lblTime = tk.Label(self, text="HORA", bg="#E4E8CD")
        self.lblTime['font']=font.Font(size=12, weight="bold")
        self.lblTime.grid(row=1, padx=50, pady=10)
        self.lblG0 = tk.Label(self, text="TEMPERATURA", bg="#E4E8CD")
        self.lblG0['font']=font.Font(size=12, weight="bold")
        self.lblG0.grid(column=1, row=1, padx=50, pady=10)
        #
        self.btnHistory = tk.Button(self, text="INICIO", relief=tk.FLAT) #COMMAND_HISTORY
        self.btnHistory['font']=font.Font(size=14)
        self.btnHistory.grid(columnspan=2, row=13, pady=20)
        
    def show_data(self):
        for cRow in range(10):
            for cCol in range(2):
                self.lblt = tk.Label(self, text="###", bg="#E4E8CD")
                self.lblt['font']=font.Font(size=10)
                self.lblt.grid(column=cCol, row=2+cRow, pady=3)
            
        
root = tk.Tk()
app = TemperatureFrame(master=root)
app.master.title("Laminadora - Main")
app.master.geometry("800x480")
app.mainloop()