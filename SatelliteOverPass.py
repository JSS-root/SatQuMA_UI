from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import Tk
from PIL import Image, ImageTk

fontcolor = '#3a346f'

class SatelliteOverPass(Frame):
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

        # relheight and relwidth are height and widths of item, relx and rely are the positining arguments

        # A description of the information this tab holds
        self.UpperTextBox = Label(self.second_frame, bg = "white", relief = GROOVE, text = "Information on satellite trajectory with illustrations", font = helv15, fg = fontcolor)
        self.UpperTextBox.place(relheight = 0.15, relwidth = 0.8, relx = 0.1, rely = 0.1)

        # Output values
        self.NoPasses = Label(self.second_frame, bg = "white", relief = GROOVE, text = "NoPasses", font = helv10, fg = fontcolor)
        self.NoPasses.place(relheight = 0.12, relwidth = 0.2, relx = 0.1, rely = 0.3)

        self.MinElevation = Label(self.second_frame, bg = "white", relief = GROOVE, text = "MinElevation", font = helv10, fg = fontcolor)
        self.MinElevation.place(relheight = 0.12, relwidth = 0.2, relx = 0.4, rely = 0.3)

        self.MaxElevation = Label(self.second_frame, bg = "white", relief = GROOVE, text = "MaxElevation", font = helv10, fg = fontcolor)
        self.MaxElevation.place(relheight = 0.12, relwidth = 0.2, relx = 0.7, rely = 0.3)

        # Here we can embed two graphics (Mayavi and a dynamic plot)
        self.MayaviGraphic = Label(self.second_frame, bg = "white", relief = GROOVE, text = "Mayavi Graphic", font = helv10, fg = fontcolor)
        self.MayaviGraphic.place(relheight = 0.55, relwidth = 0.38, relx = 0.1, rely = 0.45)

        self.DynamicPlot = Label(self.second_frame, bg = "white", relief = GROOVE, text = "Dynamic Plot", font = helv10, fg = fontcolor)
        self.DynamicPlot.place(relheight = 0.55, relwidth = 0.38, relx = 0.52, rely = 0.45)