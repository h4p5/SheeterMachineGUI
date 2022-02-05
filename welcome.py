# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 17:29:56 2021

@author: HAPS
"""

import tkinter as tk
import tkinter.font as font

class WelcomeFrame(tk.Frame):    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(background="#E4E8CD")
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.welcome = tk.PhotoImage(file="IMGS/Bienvenido.png")
        self.imgWelcome = tk.Canvas(self, width=584, height=226, bg="#E4E8CD", highlightthickness=0)
        self.imgWelcome.create_image(0,0, anchor='nw', image=self.welcome)
        self.imgWelcome.grid(row=0, columnspan=3, padx=105, pady=50)
        self.btnHistory = tk.Button(self, text="INICIO", relief=tk.FLAT) #COMMAND_HISTORY
        self.btnHistory['font']=font.Font(size=18)
        self.btnHistory.grid(column=1, row=1, padx=60, pady=52)
        
root = tk.Tk()
app = WelcomeFrame(master=root)
app.master.title("Laminadora - Main")
app.master.geometry("800x480")
app.mainloop()