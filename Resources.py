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


