from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import Tk
from PIL import Image, ImageTk

fontcolor = '#3a346f'

class SystemProperties(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        helv15 = font.Font(family="Helvetica",size=15,weight="bold")
        helv10 = font.Font(family="Helvetica",size=10,weight="bold")
        helv7 = font.Font(family="Helvetica",size=7,weight="bold")
        helv6 = font.Font(family="Helvetica",size=6,weight="bold")

        # A description of the information this tab holds
        self.UpperTextBox = Label(self, bg = "white", relief = GROOVE, text = "Information on system (source) transmission", font = helv15, fg = fontcolor)
        self.UpperTextBox.place(relheight = 0.15, relwidth = 0.8, relx = 0.1, rely = 0.1)

        # Output values - row 1
        self.SysLoss = Label(self, bg = "white", relief = GROOVE, text = "SysLoss", font = helv10, fg = fontcolor)
        self.SysLoss.place(relheight = 0.12, relwidth = 0.2, relx = 0.1, rely = 0.3)

        self.dt = Label(self, bg = "white", relief = GROOVE, text = "dt", font = helv10, fg = fontcolor)
        self.dt.place(relheight = 0.12, relwidth = 0.2, relx = 0.4, rely = 0.3)

        self.QBERI = Label(self, bg = "white", relief = GROOVE, text = "QBERI", font = helv10, fg = fontcolor)
        self.QBERI.place(relheight = 0.12, relwidth = 0.2, relx = 0.7, rely = 0.3)

        # Row 2
        self.Pec = Label(self, bg = "white", relief = GROOVE, text = "Pec", font = helv10, fg = fontcolor)
        self.Pec.place(relheight = 0.12, relwidth = 0.2, relx = 0.1, rely = 0.45)

        self.Pap = Label(self, bg = "white", relief = GROOVE, text = "Pap", font = helv10, fg = fontcolor)
        self.Pap.place(relheight = 0.12, relwidth = 0.2, relx = 0.4, rely = 0.45)




