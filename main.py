from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import Tk
from turtle import bgcolor
from PIL import Image, ImageTk
from matplotlib.dates import FR
from ChannelProperties import ChannelProperties

from PIL import Image, ImageTk
import tkinter as tk

from SatelliteOverPass import *
from SecurityProperties import *
from ChannelProperties import *
from SystemProperties import *
from Resources import *


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
from matplotlib import gridspec, ticker
import matplotlib.ticker

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{mathtools}\usepackage[T1]{fontenc}\usepackage{libertine}\usepackage{libertinust1math}\usepackage{braket}\usepackage{textgreek}')  
plt.rc('font', family='serif')

import sympy as sp
from io import BytesIO


sky_color = "white"
selectedcolor = "#e4eafa"
hoveringcolor = "#ccdee0"
backgroundcolor = '#23262b'
fontcolor = '#3a346f'

class SatQuMa_UI:
    def on_latex(self):
        expr = "$\displaystyle " + self.strvar.get() + "$"

        #This creates a ByteIO stream and saves there the output of sympy.preview
        f = BytesIO()
        the_color = "{" + self.master.cget('bg')[1:].upper()+"}"
        sp.preview(expr, euler = False, preamble = r"\documentclass{standalone}"
                   r"\usepackage{pagecolor}"
                   r"\definecolor{graybg}{HTML}" + the_color +
                   r"\pagecolor{graybg}"
                   r"\begin{document}",
                   viewer = "BytesIO", output = "ps", outputbuffer=f)
        f.seek(0)
        #Open the image as if it were a file. This works only for .ps!
        img = Image.open(f)
        img.load(scale = 10)
        img = img.resize((int(img.size[0]/2),int(img.size[1]/2)),Image.BILINEAR)
        photo = ImageTk.PhotoImage(img)
        self.label.config(image = photo)
        self.label.image = photo
        f.close()


    def __init__(self, master):
        
        # Setting up the master and setting the icon of the GUI to the SatQuMA logo
        self.master = master
        master.iconbitmap("Graphics/SatQuMA.ico")

        # Setting up some fonts to use
        helv9 = font.Font(family="Helvetica",size=9,weight="bold")
        helv15 = font.Font(family="Helvetica",size=15,weight="bold")
        helv20 = font.Font(family="Helvetica",size=20,weight="bold")
        helv35 = font.Font(family="Helvetica",size=35,weight="bold")
        helv38 = font.Font(family="Helvetica",size=38,weight="bold")

        # Image imports
        self.SatQuMAImage = ImageTk.PhotoImage(Image.open("Graphics/SatQuMA.png").resize((120, 90)))
        self.testImage = ImageTk.PhotoImage(Image.open("Graphics/earth.png").resize((120, 90)))


        # Making the style for the notebook tabs
        self.s = ttk.Style()
        self.s.theme_create( "beautiful", parent = "alt", settings ={
        "TNotebook": {
            "configure": {"tabmargins": [10, 10, 20, 10], "background":sky_color}},
        "TNotebook.Tab": {
            "configure": {"padding": [30, 15], "background": sky_color, "borderwidth":[0], "foreground":"#3a346f", "anchor":CENTER},
            "map":       {"background": [("selected", selectedcolor), ('!active', sky_color), ('active', hoveringcolor)],
                          "expand": [("selected", [1, 1, 1, 0])],
                          "foreground": [("active", "black")]}}})

        self.s.theme_use("beautiful")

        # Creating the notebook and the styles
        self.SatQuMANoteBook = ttk.Notebook(self.master)
        self.SatQuMANoteBookStyle = ttk.Style(self.master)
        self.SatQuMANoteBookTabStyle = ttk.Style(self.master)
        self.SatQuMANoteBookStyle.configure('TNotebook', tabposition = "wn")
        self.SatQuMANoteBookTabStyle.configure('TNotebook.Tab', font = helv9)

        # Placing the notebook in the frame (leave 20% of top for other logos)
        self.SatQuMANoteBook.place(relwidth = 1, relheight = 0.8, rely = 0.2)

        # Adding main banner text and image
        self.MainTitle = Label(self.master, text = "Satellite Quantum Modelling & Analysis Software UI", anchor = 'w', font = helv38, bg = 'white', fg = fontcolor)
        self.MainTitle.place(relheight = 0.2, relwidth = 0.8, relx = 0.05, rely = 0)

        self.LogoImage = Label(self.master, bg = 'white', image = self.SatQuMAImage)
        self.LogoImage.place(relheight = 0.18, relwidth = 0.1, relx = 0.85, rely = 0)

        # Creating the first tab for the GUI (Interface)
        self.InterfaceTab = Frame(self.SatQuMANoteBook, bg = 'white')

        self.PxEntryLabel = Label(self.InterfaceTab, text = "Px :", bg = 'white', fg = fontcolor, font = helv15)
        self.PxEntryLabel.place(relheight = 0.05, relwidth = 0.1, relx = 0.15, rely = 0.15) 

        self.PxEntry = Entry(self.InterfaceTab, bg = 'white', fg = fontcolor, font = helv9, justify = CENTER)
        self.PxEntry.place(relheight = 0.1, relwidth = 0.15, relx = 0.125, rely = 0.25) 

        self.Mu1EntryLabel = Label(self.InterfaceTab, text = 'Mu1 :', bg = 'white', fg = fontcolor, font = helv15)
        self.Mu1EntryLabel.place(relheight = 0.05, relwidth = 0.1, relx = 0.45, rely = 0.15) 

        self.Mu1Entry = Entry(self.InterfaceTab, bg = 'white', fg = fontcolor, font = helv9, justify = CENTER)
        self.Mu1Entry.place(relheight = 0.1, relwidth = 0.15, relx = 0.425, rely = 0.25) 

        self.Mu2EntryLabel = Label(self.InterfaceTab, text = 'Mu2 :', bg = 'white', fg = fontcolor, font = helv15)
        self.Mu2EntryLabel.place(relheight = 0.05, relwidth = 0.1, relx = 0.75, rely = 0.15) 

        self.Mu2Entry = Entry(self.InterfaceTab, bg = 'white', fg = fontcolor, font = helv9, justify = CENTER)
        self.Mu2Entry.place(relheight = 0.1, relwidth = 0.15, relx = 0.725, rely = 0.25) 

        self.RunButton = Button(self.InterfaceTab, bg = '#90ee90', text = "Run", fg = fontcolor, relief = FLAT, font = helv15, command = self.f_RunOptimisedSklCode)
        self.RunButton.place(relheight = 0.15, relwidth = 0.75, relx = 0.125, rely = 0.45)

        self.ReturnedSklOptimisedValue = Label(self.InterfaceTab, bg = 'white', relief = GROOVE, font = helv15, fg = fontcolor)
        self.ReturnedSklOptimisedValue.place(relheight = 0.15, relwidth = 0.75, relx = 0.125, rely = 0.7)

        # Add tabs from different python files
        self.SatelliteOverPassTab = SatelliteOverPass(self.SatQuMANoteBook, bg = 'white')
        self.SecurityPropertiesTab = SecurityProperties(self.SatQuMANoteBook, bg = 'white')
        self.ChannelPropertiesTab = ChannelProperties(self.SatQuMANoteBook, bg = 'white')
        self.SystemPropertiesTab = SystemProperties(self.SatQuMANoteBook, bg = 'white')
        self.ResourcesTab = Resources(self.SatQuMANoteBook, bg = 'white')

        # Adding the created tabs to the notebook
        self.SatQuMANoteBook.add(self.InterfaceTab, text = "Interface")
        self.SatQuMANoteBook.add(self.SatelliteOverPassTab, text = "Satellite Overpass")
        self.SatQuMANoteBook.add(self.SecurityPropertiesTab, text = "Security Properties")        
        self.SatQuMANoteBook.add(self.ChannelPropertiesTab, text = "Channel Properties")
        self.SatQuMANoteBook.add(self.SystemPropertiesTab, text = "System Properties")
        self.SatQuMANoteBook.add(self.ResourcesTab, text = "Resources")

    def f_RunOptimisedSklCode(self):
        
        # Checks to ensure feasible parameter values
        # First check to ensure user has entered a value
        if len(self.PxEntry.get()) == 0:
            print("Error: Please fill all entries")                                                 # This line prints out to terminal
            self.ReturnedSklOptimisedValue.config(text = "Error: Please fill out all entries")      # This line prints out in the UI
            return
        if len(self.Mu1Entry.get()) == 0:
            print("Error: Please fill all entries")
            self.ReturnedSklOptimisedValue.config(text = "Error: Please fill out all entries")
            return
        if len(self.Mu2Entry.get()) == 0:
            print("Error: Please fill all entries")
            self.ReturnedSklOptimisedValue.config(text = "Error: Please fill out all entries")
            return
        
        # Second, check to see if the user hasn't accidently entered alphabets
        if str.isalpha(self.PxEntry.get()):
            print("Error: Px must be a number")
            self.ReturnedSklOptimisedValue.config(text = "Error: Px must be a number")
            return
        if str.isalpha(self.Mu1Entry.get()):
            print("Error: Mu1 must be a number")
            self.ReturnedSklOptimisedValue.config(text = "Error: Mu1 must be a number")
            return
        if str.isalpha(self.Mu2Entry.get()):
            print("Error: Mu2 must be a number")
            self.ReturnedSklOptimisedValue.config(text = "Error: Mu2 must be a number")
            return

            print(self.PxEntry.get())
            print(type(self.PxEntry.get()))

        # Third, check to see if the values satisfy some contraints
        if float(self.PxEntry.get()) > 1.0:
            print("Error: Px must be less than or equal to 1.0")
            self.ReturnedSklOptimisedValue.config(text = "Error: Px must be less than or equal to 1.0")
            return
        if float(self.Mu1Entry.get()) > 1.0:
            print("Error: Mu1 must be less than or equal to 1.0")
            self.ReturnedSklOptimisedValue.config(text = "Error: Mu1 must be less than or equal to 1.0")
            return
        if float(self.Mu2Entry.get()) > 1.0:
            print("Error: Mu2 must be less than or equal to 1.0")
            self.ReturnedSklOptimisedValue.config(text = "Error: Mu2 must be less than or equal to 1.0")
            return    

        self.ReturnedSklOptimisedValue.config(text = "You entered Px = " + str(self.PxEntry.get()) + ", Mu1 = " + str(self.Mu1Entry.get()) + " and Mu2 = " + str(self.Mu2Entry.get()))

root=Tk()
app=SatQuMa_UI(root)
root.title('SatQuMA_Modelling_Suite')
root.geometry("1200x620")
root.configure(background='white')

# Execute tkinter
root.mainloop()