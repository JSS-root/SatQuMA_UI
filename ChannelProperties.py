from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import Tk
from PIL import Image, ImageTk

fontcolor = '#3a346f'

class ChannelProperties(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        helv15 = font.Font(family="Helvetica",size=15,weight="bold")
        helv10 = font.Font(family="Helvetica",size=10,weight="bold")
        helv7 = font.Font(family="Helvetica",size=7,weight="bold")
        helv6 = font.Font(family="Helvetica",size=6,weight="bold")

        self.UpperTextBox = Label(self, bg = "white", relief = GROOVE, text = "Information of satellite-OGS downlink quantum channel losses", font = helv15, fg = fontcolor)
        self.UpperTextBox.place(relheight = 0.15, relwidth = 0.8, relx = 0.1, rely = 0.1)

        # Output values - row 1
        self.PxA = Label(self, bg = "white", relief = GROOVE, text = "PxA", font = helv10, fg = fontcolor)
        self.PxA.place(relheight = 0.12, relwidth = 0.2, relx = 0.1, rely = 0.3)

        self.P1 = Label(self, bg = "white", relief = GROOVE, text = "P1", font = helv10, fg = fontcolor)
        self.P1.place(relheight = 0.12, relwidth = 0.2, relx = 0.4, rely = 0.3)

        self.P2 = Label(self, bg = "white", relief = GROOVE, text = "P2", font = helv10, fg = fontcolor)
        self.P2.place(relheight = 0.12, relwidth = 0.2, relx = 0.7, rely = 0.3)

        # Row 2
        self.P3 = Label(self, bg = "white", relief = GROOVE, text = "P3", font = helv10, fg = fontcolor)
        self.P3.place(relheight = 0.12, relwidth = 0.2, relx = 0.1, rely = 0.45)