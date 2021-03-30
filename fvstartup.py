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
import dbhandler as dh

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

    def promptNewPatient(self):
        #Setup the new patient window prompts
        npLabel = ttk.Label(self.mainFrame, text="Are you creating a new patient?", font=self.promptFont)
        npLabel.grid(column=0, row=0, columnspan=2, sticky = (N, E, W))
        npYButton = ttk.Button(self.mainFrame, text="YES", command=self.newPatient)
        npYButton.grid(column=0, row=1, sticky = (N, E, W))
        npNButton = ttk.Button(self.mainFrame, text="NO", command=self.patientSearch)
        npNButton.grid(column=1, row=1, sticky = (N, E, W))

    def newPatient(self):
        npWindow = Toplevel(self.root)
        npWindow.title("New Patient Entry")
        npWindow.resizable(False, False)
        npFrame = ttk.Frame(npWindow, padding="5 5 5 5", borderwidth=5, relief="ridge")
        npFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        npeLabel = ttk.Label(npFrame, text="Enter Patient Info", font=self.promptFont)
        npeLabel.grid(column=0, row=0, columnspan=2, sticky = (N, W))
        fnLabel = ttk.Label(npFrame, text="First Name")
        fnLabel.grid(column=0, row=1, sticky = (N, W))
        fnEntry = ttk.Entry(npFrame)
        fnEntry.grid(column=0, row=2, sticky = (N, W))
        lnLabel = ttk.Label(npFrame, text="Last Name")
        lnLabel.grid(column=0, row=3, sticky = (N, W))
        lnEntry = ttk.Entry(npFrame)
        lnEntry.grid(column=0, row=4, sticky = (N, W))
        dobLabel = ttk.Label(npFrame, text="Date of birth")
        dobLabel.grid(column=0, row=5, sticky = (N, W))
        dobEntry = ttk.Entry(npFrame)
        dobEntry.grid(column=0, row=6, sticky = (N, W))
        pidLabel = ttk.Label(npFrame, text="Patient Identifier")
        pidLabel.grid(column=0, row=7, sticky = (N, W))
        pidEntry = ttk.Entry(npFrame)
        pidEntry.grid(column=0, row=8, sticky = (N, W))
        npeSubmitButton = ttk.Button(npFrame, text="SUBMIT")
        npeSubmitButton.grid(column=0, row=9, sticky = (N, E, W))
        npCancelButton = ttk.Button(npFrame, text="CANCEL", command=npWindow.destroy)
        npCancelButton.grid(column=1, row=9, sticky = (N, E, W))

    def patientSearch(self):
        spWindow = Toplevel(self.root)
        spWindow.title("Patient Search")
        spWindow.resizable(False, False)
        spFrame = ttk.Frame(spWindow, padding="5 5 5 5", borderwidth=5, relief="ridge")
        spFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        speLabel = ttk.Label(spFrame, text="Enter Patient Info to Search For", font=self.promptFont)
        speLabel.grid(column=0, row=0, columnspan=2, sticky = (N, W))
        fnLabel = ttk.Label(spFrame, text="First Name")
        fnLabel.grid(column=0, row=1, sticky = (N, W))
        fnEntry = ttk.Entry(spFrame)
        fnEntry.grid(column=0, row=2, sticky = (N, W))
        lnLabel = ttk.Label(spFrame, text="Last Name")
        lnLabel.grid(column=0, row=3, sticky = (N, W))
        lnEntry = ttk.Entry(spFrame)
        lnEntry.grid(column=0, row=4, sticky = (N, W))
        dobLabel = ttk.Label(spFrame, text="Date of birth")
        dobLabel.grid(column=0, row=5, sticky = (N, W))
        dobEntry = ttk.Entry(spFrame)
        dobEntry.grid(column=0, row=6, sticky = (N, W))
        pidLabel = ttk.Label(spFrame, text="Patient Identifier")
        pidLabel.grid(column=0, row=7, sticky = (N, W))
        pidEntry = ttk.Entry(spFrame)
        pidEntry.grid(column=0, row=8, sticky = (N, W))
        speSubmitButton = ttk.Button(spFrame, text="SEARCH")
        speSubmitButton.grid(column=0, row=9, sticky = (N, E, W))
        spCancelButton = ttk.Button(spFrame, text="CANCEL", command=spWindow.destroy)
        spCancelButton.grid(column=1, row=9, sticky = (N, E, W))

    #Insert a new patient into the database
    def insertPatient(self, lnStr):
        print(lnStr)
        
    def run_startup(self):
        self.promptNewPatient()
        self.root.mainloop()

if __name__ == '__main__':
    #Make an instance of the application and run it
    su = fvStartup()
    su.run_startup()
