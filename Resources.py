from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import Tk
from PIL import Image, ImageTk
import webbrowser

from tkPDFViewer import tkPDFViewer as pdf

fontcolor = '#3a346f'

class Resources(Frame):
    def callback(self, url):
        webbrowser.open_new(url)

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Import the graphics to use here
        self.surfaces = ImageTk.PhotoImage(Image.open("Graphics/test.png").resize((200, 190)))
        self.capacities = ImageTk.PhotoImage(Image.open("Graphics/capacities.png").resize((200, 170)))
        self.review = ImageTk.PhotoImage(Image.open("Graphics/satellites.png").resize((200, 190)))

        helv25 = font.Font(family="Helvetica",size=25,weight="bold")
        helv10 = font.Font(family="Helvetica",size=10,weight="bold")
        helv7 = font.Font(family="Helvetica",size=7,weight="bold")
        helv6 = font.Font(family="Helvetica",size=6,weight="bold")

        self.Text1 = Label(self, bg = "white", relief = GROOVE, text = "Finite Key effects in SatQKD", font = helv10, fg = fontcolor)
        self.Text1.place(relheight = 0.1, relwidth = 0.2, relx = 0.1, rely = 0.15)

        self.Text2 = Label(self, bg = "white", relief = GROOVE, text = "Key generation capacities", font = helv10, fg = fontcolor)
        self.Text2.place(relheight = 0.1, relwidth = 0.2, relx = 0.4, rely = 0.15)

        self.Text3 = Label(self, bg = "white", relief = GROOVE, text = "Advances in space quantum communications", font = helv10, fg = fontcolor, wraplength=150, justify = CENTER)
        self.Text3.place(relheight = 0.1, relwidth = 0.2, relx = 0.7, rely = 0.15)

        self.Graphic1 = Label(self, bg = "white", relief = FLAT, text = "Graphic 1", image=self.surfaces, font = helv10, fg = fontcolor)
        self.Graphic1.place(relheight = 0.45, relwidth = 0.2, relx = 0.1, rely = 0.3)

        self.Graphic2 = Label(self, bg = "white", relief = FLAT, text = "Graphic 2", image=self.capacities, font = helv10, fg = fontcolor)
        self.Graphic2.place(relheight = 0.45, relwidth = 0.2, relx = 0.4, rely = 0.3)

        self.Graphic3 = Label(self, bg = "white", relief = FLAT, text = "Graphic 3", image=self.review, font = helv10, fg = fontcolor)
        self.Graphic3.place(relheight = 0.45, relwidth = 0.2, relx = 0.7, rely = 0.3)

        self.Hyperlink1 = Label(self, bg = "white", relief = RAISED, text = "Access paper", font = helv10, fg = fontcolor, cursor = "trek")
        self.Hyperlink1.pack()
        self.Hyperlink1.place(relheight = 0.1, relwidth = 0.2, relx = 0.1, rely = 0.8)
        self.Hyperlink1.bind("<Button-1>", lambda e: self.callback("https://www.nature.com/articles/s41534-022-00525-3"))

        self.Hyperlink2 = Label(self, bg = "white", relief = RAISED, text = "Access paper", font = helv10, fg = fontcolor, cursor = "trek")
        self.Hyperlink2.pack()
        self.Hyperlink2.place(relheight = 0.1, relwidth = 0.2, relx = 0.4, rely = 0.8)
        self.Hyperlink2.bind("<Button-1>", lambda e: self.callback("https://www.spiedigitallibrary.org/conference-proceedings-of-spie/11881/1188106/Key-generation-analysis-for-satellite-quantum-key-distribution/10.1117/12.2599044.short?SSO=1"))

        self.Hyperlink3 = Label(self, bg = "white", relief = RAISED, text = "Access paper", font = helv10, fg = fontcolor, cursor = "trek")
        self.Hyperlink3.pack()
        self.Hyperlink3.place(relheight = 0.1, relwidth = 0.2, relx = 0.7, rely = 0.8)
        self.Hyperlink3.bind("<Button-1>", lambda e: self.callback("https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/qtc2.12015"))

