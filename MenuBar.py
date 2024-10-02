# which are needed
from tkinter import *
from tkinter.ttk import *
import tkinter as tk

class MenuBar(tk.Menu):
    def __init__(self, root):
        super().__init__(root)
        self.fileMenu = tk.Menu(self)
        self.viewMenu = tk.Menu(self)
        self.playMenu = tk.Menu(self)
        self.helpMenu = tk.Menu(self)

        self.fileMenu.add_command(label ='Open File', command = None)
        self.fileMenu.add_command(label ='Subtitles.', command = None)
        self.fileMenu.add_command(label ='Properties', command = None)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label ='Exit', command = None)

        self.viewMenu.add_command(label ='Full Screen', command = None)
        self.viewMenu.add_command(label ='Zoom', command = None)
        self.viewMenu.add_separator()
        self.viewMenu.add_command(label ='Playlist', command = None)


        self.playMenu.add_command(label ='Play/Pause', command = None)
        self.playMenu.add_command(label='Audio Track', command=None)
        self.playMenu.add_separator()
        self.playMenu.add_command(label='Reset Rate', command=None)

        self.helpMenu.add_command(label='Home Page', command=None)
        self.helpMenu.add_command(label='Check for updates', command=None)
        self.helpMenu.add_separator()
        self.helpMenu.add_command(label='About...', command=None)

        self.add_cascade(label='File', menu=self.fileMenu)
        self.add_cascade(label='View', menu=self.viewMenu)
        self.add_cascade(label='Play', menu=self.playMenu)
        self.add_cascade(label='Help', menu=self.helpMenu)