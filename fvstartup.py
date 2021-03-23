#!/usr/bin/env python3
"""
ForceView start up class. This class prompts the user for patient and data file info and returns
the data needed to startup the ForceView program.
"""

__author__ = "Aaron Diab"
__version__ = "0.1.0"
__license__ = "GPL V3"

from tkinter import *
from tkinter import ttk
from tkinter import font

class fvStartup:

    def __init__(self):
        self.root = Tk()
        self.root.title("Force View Start Up")
        #Setup prompt fonts
        self.promptFont = font.Font(family='Helvetica', name='appHighlightFont', size=15, weight='bold')
        #Create a frame to hold everything
        self.mainFrame = ttk.Frame(self.root, padding="5 5 5 5", borderwidth=5, relief="ridge")
        self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

    def promptNewUser(self):
        #Setup the new user window prompts
        nuLabel = ttk.Label(self.mainFrame, text="Are you creating a new user?", font=self.promptFont)
        nuLabel.grid(column=0, row=0, columnspan=2, sticky = (N, E, W))
        nuYButton = ttk.Button(self.mainFrame, text="YES")
        nuYButton.grid(column=0, row=1, sticky = (N, E, W))
        nuNButton = ttk.Button(self.mainFrame, text="NO")
        nuNButton.grid(column=1, row=1, sticky = (N, E, W))

    def run_startup(self):
        self.root.mainloop()

if __name__ == '__main__':
    #Make an instance of the application and run it
    su = fvStartup()
    su.promptNewUser()
    su.run_startup()
