#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Aaron Diab"
__version__ = "0.1.0"
__license__ = "GPL V3"

from tkinter import *
from tkinter import ttk
from tkinter import font

class forceView:

    def __init__(self, root):
        root.title("Force View")

        mainframe = ttk.Frame(root, padding="5 5 5 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        #Setup title fonts
        titleFont = font.Font(family='Helvetica', name='appHighlightFont', size=15, weight='bold')

        #Setup the patient info frame
        piFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=200, height=200)
        piFrame.grid(column=0, row=0, sticky=(N,S))
        piFrame.grid_propagate(False)
        piTitle = ttk.Label(piFrame, text="Patient Info", font=titleFont)
        piTitle.grid(sticky = (N, W))
        fnLabel = ttk.Label(piFrame, text="First Name")
        fnLabel.grid(sticky = (N, W))
        fnEntry = ttk.Entry(piFrame)
        fnEntry.grid(sticky = (N, W))
        lnLabel = ttk.Label(piFrame, text="Last Name")
        lnLabel.grid(sticky = (N, W))
        lnEntry = ttk.Entry(piFrame)
        lnEntry.grid(sticky = (N, W))
        dobLabel = ttk.Label(piFrame, text="Date of birth")
        dobLabel.grid(sticky = (N, W))
        dobEntry = ttk.Entry(piFrame)
        dobEntry.grid(sticky = (N, W))
        pidLabel = ttk.Label(piFrame, text="Patient Identifier")
        pidLabel.grid(sticky = (N, W))
        pidEntry = ttk.Entry(piFrame)
        pidEntry.grid(sticky = (N, W))

        #Setup the data statistics frame
        dsFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=200, height=200)
        dsFrame.grid(column=0, row=1, sticky=(N,S))
        dsFrame.grid_propagate(False)
        dsTitle = ttk.Label(dsFrame, text="Data Statistics", font=titleFont)
        dsTitle.grid(sticky = (N, W))
        dodLabel = ttk.Label(dsFrame, text="Days of Data")
        dodLabel.grid(sticky = (N, W))
        dodEntry = ttk.Entry(dsFrame)
        dodEntry.grid(sticky = (N, W))
        lsLabel = ttk.Label(dsFrame, text="Largest Spikes")
        lsLabel.grid(sticky = (N, W))
        lsEntry = ttk.Entry(dsFrame)
        lsEntry.grid(sticky = (N, W))
        satLabel = ttk.Label(dsFrame, text="Spikes above threshold")
        satLabel.grid(sticky = (N, W))
        satEntry = ttk.Entry(dsFrame)
        satEntry.grid(sticky = (N, W))
        thsLabel = ttk.Label(dsFrame, text="Threshold")
        thsLabel.grid(sticky = (N, W))
        thScale = ttk.Scale(dsFrame, orient=HORIZONTAL, length=200, from_=1.0, to=100.0)
        thScale.grid(sticky = (N, W))
        mvdLabel = ttk.Label(dsFrame, text="Mean value of data")
        mvdLabel.grid(sticky = (N, W))
        mvdEntry = ttk.Entry(dsFrame)
        mvdEntry.grid(sticky = (N, W))

        #Setup the graph selection data frame
        gsFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=200, height=200)
        gsFrame.grid(column=0, row=2, sticky=(N,S))
        gsFrame.grid_propagate(False)
        gsTitle = ttk.Label(gsFrame, text="Selection Graph", font=titleFont)
        gsTitle.grid(sticky = (N, W))
        tsLabel = ttk.Label(gsFrame, text="Time span")
        tsLabel.grid(sticky = (N, W))
        tsEntry = ttk.Entry(gsFrame)
        tsEntry.grid(sticky = (N, W))
        tssLabel = ttk.Label(gsFrame, text="Threshold")
        tssLabel.grid(sticky = (N, W))
        tsScale = ttk.Scale(gsFrame, orient=HORIZONTAL, length=200, from_=1.0, to=100.0)
        tsScale.grid(sticky = (N, W))
        ssLabel = ttk.Label(gsFrame, text="Span selected")
        ssLabel.grid(sticky = (N, W))
        ssEntry = ttk.Entry(gsFrame)
        ssEntry.grid(sticky = (N, W))

        #Setup the main graph frame
        mgFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=600, height=400)
        mgFrame.grid(column=1, row=0, columnspan=3,  rowspan=2, sticky=(N, S, E, W))

        #Setup the selection graph frame
        sgFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=600, height=200)
        sgFrame.grid(column=1, row=2, columnspan=3,  rowspan=1, sticky=(N, S, E, W))

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=3)
        mainframe.columnconfigure(2, weight=3)
        mainframe.columnconfigure(3, weight=3)
        mainframe.rowconfigure(0, weight=4)
        mainframe.rowconfigure(1, weight=4)
        mainframe.rowconfigure(2, weight=1)

root = Tk()
forceView(root)
root.mainloop()

