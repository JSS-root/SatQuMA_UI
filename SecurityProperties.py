from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import Tk
from PIL import Image, ImageTk

import platform

fontcolor = '#3a346f'

class SecurityProperties(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Set up scroll bar
        self.main_frame = Frame(self, bg = "white")
        self.main_frame.pack(fill=BOTH, expand=1)

        self.my_canvas = Canvas(self.main_frame, bg = "white")
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.my_scrollbar=ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all")))

        self.second_frame = Frame(self.my_canvas, width=1000, height=500, bg = "white")
        self.my_canvas.create_window((0,0), window=self.second_frame, anchor= "nw")
        
        helv15 = font.Font(family="Helvetica",size=15,weight="bold")
        helv10 = font.Font(family="Helvetica",size=10,weight="bold")
        helv7 = font.Font(family="Helvetica",size=7,weight="bold")
        helv6 = font.Font(family="Helvetica",size=6,weight="bold")

        # A description of the information this tab holds
        self.UpperTextBox = Label(self.second_frame, bg = "white", relief = GROOVE, text = "Information on channel characteristics and security of finite keys", font = helv15, fg = fontcolor)
        self.UpperTextBox.place(relheight = 0.15, relwidth = 0.8, relx = 0.1, rely = 0.1)

        # Output values - Row 1
        self.QBER = Label(self.second_frame, bg = "white", relief = GROOVE, text = "QBER", font = helv10, fg = fontcolor)
        self.QBER.place(relheight = 0.12, relwidth = 0.2, relx = 0.1, rely = 0.3)

        self.PhiX = Label(self.second_frame, bg = "white", relief = GROOVE, text = "PhiX", font = helv10, fg = fontcolor)
        self.PhiX.place(relheight = 0.12, relwidth = 0.2, relx = 0.4, rely = 0.3)

        self.nX = Label(self.second_frame, bg = "white", relief = GROOVE, text = "nX", font = helv10, fg = fontcolor)
        self.nX.place(relheight = 0.12, relwidth = 0.2, relx = 0.7, rely = 0.3)

        # Row 2
        self.nZ = Label(self.second_frame, bg = "white", relief = GROOVE, text = "nZ", font = helv10, fg = fontcolor)
        self.nZ.place(relheight = 0.12, relwidth = 0.2, relx = 0.1, rely = 0.45)

        self.ErrorCorrection = Label(self.second_frame, bg = "white", relief = GROOVE, text = "ErrorCorrection", font = helv10, fg = fontcolor)
        self.ErrorCorrection.place(relheight = 0.12, relwidth = 0.2, relx = 0.4, rely = 0.45)

        self.sX0 = Label(self.second_frame, bg = "white", relief = GROOVE, text = "sX0", font = helv10, fg = fontcolor)
        self.sX0.place(relheight = 0.12, relwidth = 0.2, relx = 0.7, rely = 0.45)

        # Row 3
        self.sX1 = Label(self.second_frame, bg = "white", relief = GROOVE, text = "sX1", font = helv10, fg = fontcolor)
        self.sX1.place(relheight = 0.12, relwidth = 0.2, relx = 0.1, rely = 0.6)

        self.vZ1 = Label(self.second_frame, bg = "white", relief = GROOVE, text = "vZ1", font = helv10, fg = fontcolor)
        self.vZ1.place(relheight = 0.12, relwidth = 0.2, relx = 0.4, rely = 0.6)

        self.sZ1 = Label(self.second_frame, bg = "white", relief = GROOVE, text = "sZ1", font = helv10, fg = fontcolor)
        self.sZ1.place(relheight = 0.12, relwidth = 0.2, relx = 0.7, rely = 0.6)

        # Row 4
        self.epsC = Label(self.second_frame, bg = "white", relief = GROOVE, text = "eps_c", font = helv10, fg = fontcolor)
        self.epsC.place(relheight = 0.12, relwidth = 0.2, relx = 0.1, rely = 0.75)

        self.epsS = Label(self.second_frame, bg = "white", relief = GROOVE, text = "eps_s", font = helv10, fg = fontcolor)
        self.epsS.place(relheight = 0.12, relwidth = 0.2, relx = 0.4, rely = 0.75)








