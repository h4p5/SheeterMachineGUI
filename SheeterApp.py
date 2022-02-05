# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:04:43 2021

@author: HAPS
"""

import tkinter as tk
import tkinter.font as font

class App(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title_font = font.Font(family='Helvetica', size=18, weight="bold", slant="italic") #**
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, WelcomeFrame, StartFrame, MainFrame, StopFrame, AlarmFrame, CompletedFrame, 
                  HistoryFrame, TemperatureFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button0 = tk.Button(self, text="Go to WelcomeFrame", command=lambda: controller.show_frame("WelcomeFrame"))
        button1 = tk.Button(self, text="Go to StartFrame", command=lambda: controller.show_frame("StartFrame"))
        button2 = tk.Button(self, text="Go to MainFrame", command=lambda: controller.show_frame("MainFrame"))
        button3 = tk.Button(self, text="Go to StopFrame", command=lambda: controller.show_frame("StopFrame"))
        button4 = tk.Button(self, text="Go to AlarmFrame", command=lambda: controller.show_frame("AlarmFrame"))
        button5 = tk.Button(self, text="Go to CompletedFrame", command=lambda: controller.show_frame("CompletedFrame"))
        button6 = tk.Button(self, text="Go to HistoryFrame", command=lambda: controller.show_frame("HistoryFrame"))
        button7 = tk.Button(self, text="Go to TemperatureFrame", command=lambda: controller.show_frame("TemperatureFrame"))
        button0.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack()

class WelcomeFrame(tk.Frame):    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#E4E8CD")
        self.create_widgets()
        
    def create_widgets(self):
        self.welcome = tk.PhotoImage(file="IMGS/Bienvenido.png")
        self.imgWelcome = tk.Canvas(self, width=584, height=226, bg="#E4E8CD", highlightthickness=0)
        self.imgWelcome.create_image(0,0, anchor='nw', image=self.welcome)
        self.imgWelcome.grid(row=0, columnspan=3, padx=105, pady=50)
        self.btnHistory = tk.Button(self, text="INICIO", relief=tk.FLAT, 
                                    command=lambda: self.controller.show_frame("StartFrame"))
        self.btnHistory['font']=font.Font(size=18)
        self.btnHistory.grid(column=1, row=1, padx=60, pady=52)

class StartFrame(tk.Frame):    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#E4E8CD")
        self.create_widgets()
        self.create_form()
        self.show_data()
        
    def create_widgets(self):
        self.btnHistory = tk.Button(self, text="HISTORIAL", relief=tk.FLAT, 
                                    command=lambda: self.controller.show_frame("HistoryFrame"))
        self.btnHistory['font']=font.Font(size=15)
        self.btnHistory.grid(column=0, row=0, padx=60, pady=10)
        self.lblStatus = tk.Label(self, text="", bg="#E4E8CD", width=15)
        self.lblStatus['font']=font.Font(size=15)
        self.lblStatus.grid(column=1, row=0, padx=60, pady=10)
        self.btnTemp = tk.Button(self, text="TEMPERATURA", relief=tk.FLAT, 
                                 command=lambda: self.controller.show_frame("TemperatureFrame"))
        self.btnTemp['font']=font.Font(size=15)
        self.btnTemp.grid(column=2, row=0, padx=50, pady=10)
        self.btnStart = tk.Button(self, text="CONFIRMAR", relief=tk.FLAT, bg="#BDF271", 
                                  command=lambda: self.controller.show_frame("MainFrame"))
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
        self.btnHB10 = tk.Button(self, text="  10  MM  ", bg="#E4E8CD")
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
        
    def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#E4E8CD")
        self.create_widgets()
        
    def create_widgets(self):
        self.btnHistory = tk.Button(self, text="HISTORIAL", relief=tk.FLAT, 
                                    command=lambda: self.controller.show_frame("HistoryFrame"))
        self.btnHistory['font']=font.Font(size=15)
        self.btnHistory.grid(column=0, row=0, padx=60, pady=10)
        self.lblStatus = tk.Label(self, text="STATUS", bg="#BDF271", width=15)
        self.lblStatus['font']=font.Font(size=15)
        self.lblStatus.grid(column=1, row=0, padx=60, pady=10)
        self.btnTemp = tk.Button(self, text="TEMPERATURA", relief=tk.FLAT, 
                                 command=lambda: self.controller.show_frame("TemperatureFrame"))
        self.btnTemp['font']=font.Font(size=15)
        self.btnTemp.grid(column=2, row=0, padx=50, pady=10)
        self.right_imgs()  #MUST BE IF
        self.show_tags()
        self.show_info()
        
    def right_imgs(self):
        self.masaDerecha = tk.PhotoImage(file="IMGS/MasaDD.png")
        self.imgMasa = tk.Canvas(self, width=441, height=185, bg="#E4E8CD", highlightthickness=0)
        self.imgMasa.create_image(0,0, anchor='nw', image=self.masaDerecha)
        self.imgMasa.grid(row=1, columnspan=3)
        self.flechaD = tk.PhotoImage(file="IMGS/FlechaD.png")
        self.imgflecha = tk.Canvas(self, width=100, height=86, bg="#E4E8CD", highlightthickness=0)
        self.imgflecha.create_image(0,0, anchor='nw', image=self.flechaD)
        self.imgflecha.grid(row=2, columnspan=3, pady=13)
    
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

class StopFrame(tk.Frame):    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#E4E8CD")
        self.create_widgets()
        
    def create_widgets(self):
        self.btnHistory = tk.Button(self, text="HISTORIAL", relief=tk.FLAT, 
                                    command=lambda: self.controller.show_frame("HistoryFrame"))
        self.btnHistory['font']=font.Font(size=15)
        self.btnHistory.grid(column=0, row=0, padx=60, pady=10)
        self.lblStatus = tk.Label(self, text="STATUS", bg="#FF0000", width=15)
        self.lblStatus['font']=font.Font(size=15)
        self.lblStatus.grid(column=1, row=0, padx=60, pady=10)
        self.btnTemp = tk.Button(self, text="TEMPERATURA", relief=tk.FLAT, 
                                 command=lambda: self.controller.show_frame("TemperatureFrame"))
        self.btnTemp['font']=font.Font(size=15)
        self.btnTemp.grid(column=2, row=0, padx=50, pady=10)
        self.stop_alert()
        self.show_tags()
        self.show_info()
        
    def stop_alert(self):
        self.stop = tk.PhotoImage(file="IMGS/Stop1.png")
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
        
class AlarmFrame(tk.Frame):    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#E4E8CD")
        self.create_widgets()
        
    def create_widgets(self):
        self.btnHistory = tk.Button(self, text="HISTORIAL", relief=tk.FLAT, 
                                    command=lambda: self.controller.show_frame("HistoryFrame"))
        self.btnHistory['font']=font.Font(size=15)
        self.btnHistory.grid(column=0, row=0, padx=60, pady=10)
        self.lblStatus = tk.Label(self, text="STATUS", bg="#FF0000", width=15)
        self.lblStatus['font']=font.Font(size=15)
        self.lblStatus.grid(column=1, row=0, padx=60, pady=10)
        self.btnTemp = tk.Button(self, text="TEMPERATURA", relief=tk.FLAT, 
                                 command=lambda: self.controller.show_frame("TemperatureFrame"))
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
        
class CompletedFrame(tk.Frame):    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#E4E8CD")
        self.create_widgets()
        self.show_img()
        self.show_tags()
        self.show_info()
        
    def create_widgets(self):
        self.btnHistory = tk.Button(self, text="HISTORIAL", relief=tk.FLAT, 
                                    command=lambda: self.controller.show_frame("HistoryFrame"))
        self.btnHistory['font']=font.Font(size=15)
        self.btnHistory.grid(column=0, row=0, padx=60, pady=10)
        self.lblStatus = tk.Label(self, text="", bg="#E4E8CD", width=15)
        self.lblStatus['font']=font.Font(size=15)
        self.lblStatus.grid(column=1, row=0, padx=60, pady=10)
        self.btnTemp = tk.Button(self, text="TEMPERATURA", relief=tk.FLAT, 
                                 command=lambda: self.controller.show_frame("TemperatureFrame"))
        self.btnTemp['font']=font.Font(size=15)
        self.btnTemp.grid(column=2, row=0, padx=50, pady=10)
        self.btnStart = tk.Button(self, text="VOLVER A INICIO", relief=tk.FLAT, 
                                  command=lambda: self.controller.show_frame("StartFrame"))
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

class HistoryFrame(tk.Frame):    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#E4E8CD")
        self.create_widgets()
        self.show_data()
        
    def create_widgets(self):
        self.lblHistory = tk.Label(self, text="HISTORIAL", width=15, bg="#E4E8CD")
        self.lblHistory['font']=font.Font(size=25, weight="bold")
        self.lblHistory.grid(columnspan=4, row=0, pady=15)
        self.lblDate = tk.Label(self, text="FECHA", bg="#E4E8CD")
        self.lblDate['font']=font.Font(size=12, weight="bold")
        self.lblDate.grid(row=1, padx=50, pady=10)
        self.lblTime = tk.Label(self, text="HORA", bg="#E4E8CD")
        self.lblTime['font']=font.Font(size=12, weight="bold")
        self.lblTime.grid(column=1, row=1, padx=50, pady=10)
        self.lblG0 = tk.Label(self, text="GROSOR INICIAL", bg="#E4E8CD")
        self.lblG0['font']=font.Font(size=12, weight="bold")
        self.lblG0.grid(column=2, row=1, padx=50, pady=10)
        self.lblGF = tk.Label(self, text="GROSOR FINAL", bg="#E4E8CD")
        self.lblGF['font']=font.Font(size=12, weight="bold")
        self.lblGF.grid(column=3, row=1, padx=50, pady=10)
        self.btnHistory = tk.Button(self, text="INICIO", relief=tk.FLAT, 
                                    command=lambda: self.controller.show_frame("MainFrame")) #COMMAND_BACK
        self.btnHistory['font']=font.Font(size=14)
        self.btnHistory.grid(columnspan=4, row=13, pady=20)
        
    def show_data(self):
        for cRow in range(10):
            for cCol in range(4):
                self.lblt = tk.Label(self, text="###", bg="#E4E8CD")
                self.lblt['font']=font.Font(size=10)
                self.lblt.grid(column=cCol, row=2+cRow, pady=3)
        
class TemperatureFrame(tk.Frame):    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#E4E8CD")
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
        self.btnHistory = tk.Button(self, text="INICIO", relief=tk.FLAT, 
                                    command=lambda: self.controller.show_frame("MainFrame"))#COMMAND_BACK
        self.btnHistory['font']=font.Font(size=14)
        self.btnHistory.grid(columnspan=2, row=13, pady=20)
        
    def show_data(self):
        for cRow in range(10):
            for cCol in range(2):
                self.lblt = tk.Label(self, text="###", bg="#E4E8CD")
                self.lblt['font']=font.Font(size=10)
                self.lblt.grid(column=cCol, row=2+cRow, pady=3)

if __name__ == "__main__":
    app = App()
    app.title("Laminadora - Main")
    app.geometry("800x480")
    app.mainloop()