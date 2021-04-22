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
import fvpatient as fp

class fvStartup:

    def __init__(self, patient):
        self.root = Tk()
        self.root.title("Force View Start Up")
        self.root.resizable(False, False)
        #Setup prompt fonts
        self.promptFont = font.Font(family='Helvetica', name='appHighlightFont', size=15, weight='bold')
        #Create a frame to hold everything
        self.mainFrame = ttk.Frame(self.root, padding="5 5 5 5", borderwidth=5, relief="ridge")
        self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.patient = patient

    #Create the new patient prompt window
    def promptNewPatient(self):
        npLabel = ttk.Label(self.mainFrame, text="Are you creating a new patient?", font=self.promptFont)
        npLabel.grid(column=0, row=0, columnspan=2, sticky = (N, E, W))
        npYButton = ttk.Button(self.mainFrame, text="YES", command=self.newPatient)
        npYButton.grid(column=0, row=1, sticky = (N, E, W))
        npNButton = ttk.Button(self.mainFrame, text="NO", command=self.patientSearch)
        npNButton.grid(column=1, row=1, sticky = (N, E, W))

    def newPatient(self):
        self.npWindow = Toplevel(self.root)
        self.npWindow.title("New Patient Entry")
        self.npWindow.resizable(False, False)
        npFrame = ttk.Frame(self.npWindow, padding="5 5 5 5", borderwidth=5, relief="ridge")
        npFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        npeLabel = ttk.Label(npFrame, text="Enter Patient Info", font=self.promptFont)
        npeLabel.grid(column=0, row=0, columnspan=2, sticky = (N, W))
        #Get first name of patient
        fnLabel = ttk.Label(npFrame, text="First Name")
        fnLabel.grid(column=0, row=1, sticky = (N, W))
        self.fname = StringVar()
        fnEntry = ttk.Entry(npFrame, textvariable=self.fname)
        fnEntry.grid(column=0, row=2, sticky = (N, W))
        #Get last name of patient
        lnLabel = ttk.Label(npFrame, text="Last Name")
        lnLabel.grid(column=0, row=3, sticky = (N, W))
        self.lname = StringVar()
        lnEntry = ttk.Entry(npFrame, textvariable=self.lname)
        lnEntry.grid(column=0, row=4, sticky = (N, W))
        #Get patient date of birth
        dobLabel = ttk.Label(npFrame, text="Date of birth")
        dobLabel.grid(column=0, row=5, sticky = (N, W))
        self.dobirth = StringVar()
        dobEntry = ttk.Entry(npFrame, textvariable=self.dobirth)
        dobEntry.grid(column=0, row=6, sticky = (N, W))
        #Get the patient id (SSN or such)
        pidLabel = ttk.Label(npFrame, text="Patient Identifier")
        pidLabel.grid(column=0, row=7, sticky = (N, W))
        self.patid = StringVar()
        pidEntry = ttk.Entry(npFrame, textvariable=self.patid)
        pidEntry.grid(column=0, row=8, sticky = (N, W))
        #Create submit button
        npeSubmitButton = ttk.Button(npFrame, text="SUBMIT", command=self.insertPatToDB)
        npeSubmitButton.grid(column=0, row=9, sticky = (N, E, W))
        #Create cancel button
        npCancelButton = ttk.Button(npFrame, text="CANCEL", command=self.npWindow.destroy)
        npCancelButton.grid(column=1, row=9, sticky = (N, E, W))

    def patientSearch(self):
        self.spWindow = Toplevel(self.root)
        self.spWindow.title("Patient Search")
        self.spWindow.resizable(False, False)
        spFrame = ttk.Frame(self.spWindow, padding="5 5 5 5", borderwidth=5, relief="ridge")
        spFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        speLabel = ttk.Label(spFrame, text="Enter Patient Info to Search For", font=self.promptFont)
        speLabel.grid(column=0, row=0, columnspan=2, sticky = (N, W))
        fnLabel = ttk.Label(spFrame, text="First Name")
        fnLabel.grid(column=0, row=1, sticky = (N, W))
        self.fname = StringVar()
        fnEntry = ttk.Entry(spFrame, textvariable=self.fname)
        fnEntry.grid(column=0, row=2, sticky = (N, W))
        lnLabel = ttk.Label(spFrame, text="Last Name")
        lnLabel.grid(column=0, row=3, sticky = (N, W))
        self.lname = StringVar()
        lnEntry = ttk.Entry(spFrame, textvariable=self.lname)
        lnEntry.grid(column=0, row=4, sticky = (N, W))
        #These are commented out to make searching simpler
        #dobLabel = ttk.Label(spFrame, text="Date of birth")
        #dobLabel.grid(column=0, row=5, sticky = (N, W))
        #dobEntry = ttk.Entry(spFrame)
        #dobEntry.grid(column=0, row=6, sticky = (N, W))
        #pidLabel = ttk.Label(spFrame, text="Patient Identifier")
        #pidLabel.grid(column=0, row=7, sticky = (N, W))
        #pidEntry = ttk.Entry(spFrame)
        #pidEntry.grid(column=0, row=8, sticky = (N, W))
        speSubmitButton = ttk.Button(spFrame, text="SEARCH", command=self.searchForPat)
        speSubmitButton.grid(column=0, row=9, sticky = (N, E, W))
        spCancelButton = ttk.Button(spFrame, text="CANCEL", command=self.spWindow.destroy)
        spCancelButton.grid(column=1, row=9, sticky = (N, E, W))

    #Insert a new patient into the database
    def insertPatToDB(self):
        self.patient.setPatInfo(self.lname.get(), self.fname.get(), self.dobirth.get(), self.patid.get())
        dbHand = dh.dbHandler()
        dbHand.createPatient(self.patient.getPatInfo())
        self.npWindow.destroy()
        self.root.destroy()

    def searchForPat(self):
        #print(self.fname.get(), self.lname.get())
        dbHand = dh.dbHandler()
        searchPat = dbHand.getSpecificPat(self.fname.get(), self.lname.get())[0] 
        self.patient.setPatInfo(searchPat[1], searchPat[2], searchPat[3], searchPat[4])
        self.spWindow.destroy()
        self.root.destroy()
       
    def run_startup(self):
        self.promptNewPatient()
        self.root.mainloop()

if __name__ == '__main__':
    #Make an instance of the application and run it
    su = fvStartup()
    su.run_startup()
