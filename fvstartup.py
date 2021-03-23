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
        self.root.resizable(False, False)
        #Setup prompt fonts
        self.promptFont = font.Font(family='Helvetica', name='appHighlightFont', size=15, weight='bold')
        #Create a frame to hold everything
        self.mainFrame = ttk.Frame(self.root, padding="5 5 5 5", borderwidth=5, relief="ridge")
        self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

    def promptNewUser(self):
        #Setup the new user window prompts
        nuLabel = ttk.Label(self.mainFrame, text="Are you creating a new user?", font=self.promptFont)
        nuLabel.grid(column=0, row=0, columnspan=2, sticky = (N, E, W))
        nuYButton = ttk.Button(self.mainFrame, text="YES", command=self.newUser)
        nuYButton.grid(column=0, row=1, sticky = (N, E, W))
        nuNButton = ttk.Button(self.mainFrame, text="NO", command=self.userSearch)
        nuNButton.grid(column=1, row=1, sticky = (N, E, W))

    def newUser(self):
        nuWindow = Toplevel(self.root)
        nuWindow.title("New User Entry")
        nuWindow.resizable(False, False)
        nuFrame = ttk.Frame(nuWindow, padding="5 5 5 5", borderwidth=5, relief="ridge")
        nuFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        nueLabel = ttk.Label(nuFrame, text="Enter Patient Info", font=self.promptFont)
        nueLabel.grid(column=0, row=0, columnspan=2, sticky = (N, W))
        fnLabel = ttk.Label(nuFrame, text="First Name")
        fnLabel.grid(column=0, row=1, sticky = (N, W))
        fnEntry = ttk.Entry(nuFrame)
        fnEntry.grid(column=0, row=2, sticky = (N, W))
        lnLabel = ttk.Label(nuFrame, text="Last Name")
        lnLabel.grid(column=0, row=3, sticky = (N, W))
        lnEntry = ttk.Entry(nuFrame)
        lnEntry.grid(column=0, row=4, sticky = (N, W))
        dobLabel = ttk.Label(nuFrame, text="Date of birth")
        dobLabel.grid(column=0, row=5, sticky = (N, W))
        dobEntry = ttk.Entry(nuFrame)
        dobEntry.grid(column=0, row=6, sticky = (N, W))
        pidLabel = ttk.Label(nuFrame, text="Patient Identifier")
        pidLabel.grid(column=0, row=7, sticky = (N, W))
        pidEntry = ttk.Entry(nuFrame)
        pidEntry.grid(column=0, row=8, sticky = (N, W))
        nueSubmitButton = ttk.Button(nuFrame, text="SUBMIT")
        nueSubmitButton.grid(column=0, row=9, sticky = (N, E, W))
        nuCancelButton = ttk.Button(nuFrame, text="CANCEL")
        nuCancelButton.grid(column=1, row=9, sticky = (N, E, W))

    def userSearch(self):
        print("Search for user!")

    def run_startup(self):
        self.promptNewUser()
        self.root.mainloop()

if __name__ == '__main__':
    #Make an instance of the application and run it
    su = fvStartup()
    su.run_startup()
