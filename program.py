from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, Canvas, Entry, HORIZONTAL, StringVar, Label, Frame, messagebox, IntVar, Button, Radiobutton, LabelFrame
import random
from matplotlib import pyplot as plt
import numpy as np


class Grafy(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Grafy goniometrických funkcí")
        self.master.maxsize(2000, 4000)
        self.master.resizable(True, True)
        self.master.rowconfigure(0, weight=500)
        self.master.rowconfigure(1, weight=500)
        self.master.rowconfigure(2, weight=500)
        self.master.rowconfigure(3, weight=500)
        self.master.rowconfigure(4, weight=500)
        self.master.rowconfigure(5, weight=500)
        self.master.rowconfigure(6, weight=500)
        self.master.rowconfigure(7, weight=500)
        self.master.rowconfigure(8, weight=500)
        self.master.columnconfigure(0, weight=1500)
        self.master.columnconfigure(1, weight=1500)
        self.master.columnconfigure(2, weight=1500)
        self.master.columnconfigure(3, weight=1500)
        self.okno()
        
        
       

    def okno(self):
        self.f = IntVar()
        self.f.set(1)

        self.od_promenna = StringVar()
        self.do_promenna = StringVar()

        self.soubor_promenna = StringVar()

        self.fceFrame = LabelFrame(text="funkce", padx=5, pady=14, borderwidth=10)
        self.fceFrame.grid(column=0, row=1, sticky="WE")

        self.valueFrame = LabelFrame(text="hodnoty", padx=50, pady=5, borderwidth=10)
        self.valueFrame.grid(column=1, row=1, sticky="WE")

        self.souborFrame = LabelFrame(text="graf ze souboru", padx=5, pady=5, borderwidth=10)
        self.souborFrame.grid(column=0, row=5, columnspan=3, sticky="WENS")
        

        self.nadpis = Label(text="Vítej v programu na zobrazení grafů funkcí!!!")
        self.nadpis.grid(row=0, column=1, columnspan=2)

        
        self.sinus = Radiobutton(self.fceFrame, text="sinus", variable=self.f, value=1)
        self.sinus.grid(row=1, column=0, sticky="W")

        self.cosinus = Radiobutton(self.fceFrame, text="cosinus", variable=self.f, value=2)
        self.cosinus.grid(row=2, column=0, sticky="W")

        self.expo = Radiobutton(self.fceFrame, text="exp", variable=self.f, value=3)
        self.expo.grid(row=3, column=0, sticky="W")

        self.log = Radiobutton(self.fceFrame, text="log", variable=self.f, value=4)
        self.log.grid(row=4, column=0, sticky="W")

        self.od = Label(self.valueFrame, text="Od:", padx=50)
        self.od.grid(row=1, column=1, sticky="W")
        self.hodnota1 = Entry(self.valueFrame, width=15, bd=10, justify="center", textvariable=self.od_promenna)
        self.hodnota1.grid(column=1, row=2, sticky="E")

        self.do = Label(self.valueFrame, text="Do:", padx=50)
        self.do.grid(row=3, column=1, sticky="W")
        self.hodnota2 = Entry(self.valueFrame, width=15, bd=10, justify="center", textvariable=self.do_promenna)
        self.hodnota2.grid(column=1, row=4, sticky="E")
        
        self.tlacitko = Button(width=15, bd=10, justify="center", text="vytvořit", command=self.graf_fce)
        self.tlacitko.grid(row=1, column=3, rowspan=4, sticky="WENS")

        self.soubor = Label(self.souborFrame, text="soubor:", padx=50)
        self.soubor.grid(row=5, column=0, columnspan=2)
        self.vstupsoubor = Entry(self.souborFrame, width=40, bd=10, justify="center", textvariable=self.soubor_promenna)
        self.vstupsoubor.grid(row=6, column=0, columnspan=2)
    
        self.tlacitko2 = Button(width=15, bd=10, justify="center", text="vytvořit", command=self.graf_soubor)
        self.tlacitko2.grid(row=5, column=3, rowspan=4, sticky="WENS")

        self.tlacitko3 = Button(self.souborFrame, width=15, bd=10, justify="center", text="vlož soubor", command=self.vyber_soubor)
        self.tlacitko3.grid(row=7, column=0, rowspan=4, sticky="WENS")



    def graf_fce(self):
        try:
            druh_fce = self.f.get()
            od = float(self.od_promenna.get())
            do = float(self.do_promenna.get())
            x = np.linspace(od,do, 1000)
            if druh_fce == 1:
                y = np.sin(x)
            elif druh_fce == 2:
                y = np.cos(x)
            elif druh_fce == 3:
                y = np.exp(x)
            else:
                y = np.log(x)

            plt.plot(x,y)
            plt.show()
        except:
            messagebox.showerror("Chyba", "Je třeba zadat hodnoty od a do")

    def graf_soubor(self):
        if self.soubor_promenna.get():
            with open(self.soubor_promenna.get(), "r") as data:
                data = data.readlines()
                x = list()
                y = list()
                for line in data:
                    x.append(float(line.split()[0]))
                    y.append(float(line.split()[1]))
            plt.plot(x,y)
            plt.show()
        else:
            messagebox.showerror("Chyba", "zadej cestu k souboru")
    def vyber_soubor(self):
        self.soubor_promenna.set(tk.filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("text files", "*.txt"),)))
        
            


root = tk.Tk()
app = Grafy(root)
root.mainloop()
