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
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import fvstartup as su
import fvpatient as fp

class forceView:

    def __init__(self):
        self.currPat = fp.fvPatient()
        self.graphData = np.array([])
        self.selDay = 0
        progEntry = su.fvStartup(self.currPat)
        progEntry.run_startup()
        self.root = Tk()
        self.root.title("Force View")

    #Opens a dialog to allow you to open a new datafile
    def openNewFile(self):
        #Prompt the user for the data file
        dataFile = filedialog.askopenfilename()
        self.graphData = np.fromfile(dataFile, dtype='<u2')

        #Plot the selection graph
        self.plotGraph('sel')

        #Plot the main window graph
        self.plotGraph('main')
    
    #Plot the Selection graph type = type of graph sel or main
    def plotGraph(self, typ):
        #Create the selection plot
        #Maybe create the figure first and then the axes
        fig, ax = plt.subplots()
        if typ == 'sel':
            fig.patch.set_facecolor('xkcd:mint green')
            ax.set_xlim(xmin=0, xmax=self.graphData.size)
            ax.set_ylim(ymin=-5, ymax=np.amax(self.graphData)+50)
            ax.axes.xaxis.set_ticks([])
            ax.axes.yaxis.set_ticks([])
            ax.plot(self.graphData)
            plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
            graphCanvas = FigureCanvasTkAgg(fig, master=self.sgFrame)
            graphCanvas.draw()
            graphCanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        elif typ == 'main':
            startDay = self.selDay * 21600000
            endDay = startDay + 21600000
            ax.set_xlim(xmin=0, xmax=self.graphData.size)
            ax.set_ylim(ymin=-5, ymax=np.amax(self.graphData)+50)
            ax.plot(self.graphData[startDay:endDay])
            fig.tight_layout()
            graphCanvas = FigureCanvasTkAgg(fig, master=self.mgFrame)
            graphCanvas.draw()
            graphCanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            ax.set(xlabel='Seconds', ylabel='Force (N)')
            #ax.legend()
            #Create the toolbar
            grahpToolbar = NavigationToolbar2Tk(graphCanvas, self.mgFrame).update()
            graphCanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    #Opens a dialog to allow you to open an existing datafile
    def openExtantFile(self):
        pass
       
    def run_app(self):
        #Setup the menubar
        self.root.option_add('*tearOff', FALSE)
        menubar = Menu(self.root)
        self.root['menu'] = menubar
        menuFile = Menu(menubar)
        menubar.add_cascade(menu=menuFile, label='File')
        menuFile.add_command(label='Open Data File', command=self.openNewFile)
        #menuFile.add_command(label='Open Existing File', command=self.openExtantFile)

        #Create the main content frame
        mainframe = ttk.Frame(self.root, padding="5 5 5 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        #Setup title fonts
        titleFont = font.Font(family='Helvetica', name='appHighlightFont', size=15, weight='bold')

        #Setup the patient info frame
        piFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=200, height=200)
        piFrame.grid(column=0, row=0, sticky=(N,S))
        piFrame.grid_propagate(False)
        piTitle = ttk.Label(piFrame, text="Patient Info", font=titleFont)
        piTitle.grid(sticky = (N, W))
        #First name entry
        fnLabel = ttk.Label(piFrame, text="First Name")
        fnLabel.grid(sticky = (N, W))
        fnEntryStr = StringVar()
        fnEntryStr.set(self.currPat.fname)
        fnEntry = ttk.Entry(piFrame, textvariable=fnEntryStr)
        fnEntry.grid(sticky = (N, W))
        #Last name entry
        lnLabel = ttk.Label(piFrame, text="Last Name")
        lnLabel.grid(sticky = (N, W))
        lnEntryStr = StringVar()
        lnEntryStr.set(self.currPat.lname)
        lnEntry = ttk.Entry(piFrame, textvariable=lnEntryStr)
        lnEntry.grid(sticky = (N, W))
        #Date of birth entry
        dobLabel = ttk.Label(piFrame, text="Date of birth")
        dobLabel.grid(sticky = (N, W))
        dobEntryStr = StringVar()
        dobEntryStr.set(self.currPat.dob)
        dobEntry = ttk.Entry(piFrame, textvariable=dobEntryStr)
        dobEntry.grid(sticky = (N, W))
        #Patient ID entry
        pidLabel = ttk.Label(piFrame, text="Patient Identifier")
        pidLabel.grid(sticky = (N, W))
        pidEntryStr = StringVar()
        pidEntryStr.set(self.currPat.patid)
        pidEntry = ttk.Entry(piFrame, textvariable=pidEntryStr)
        pidEntry.grid(sticky = (N, W))

        #Setup the data statistics frame
        dsFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=200, height=200)
        dsFrame.grid(column=0, row=1, sticky=(N,S))
        dsFrame.grid_propagate(False)
        dsTitle = ttk.Label(dsFrame, text="Data Statistics", font=titleFont)
        dsTitle.grid(sticky = (N, W))
        dodLabel = ttk.Label(dsFrame, text="Selected Day")
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
        ssLabel = ttk.Label(gsFrame, text="Day selected")
        ssLabel.grid(sticky = (N, W))
        ssEntry = ttk.Entry(gsFrame)
        ssEntry.grid(sticky = (N, W))
        #tssLabel = ttk.Label(gsFrame, text="")
        #tssLabel.grid(sticky = (N, W))
        tsScale = ttk.Scale(gsFrame, orient=HORIZONTAL, length=200, from_=1.0, to=100.0)
        tsScale.grid(sticky = (N, W))

        #Setup the main graph frame
        self.mgFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=600, height=400)
        self.mgFrame.grid(column=1, row=0, columnspan=3,  rowspan=2, sticky=(N, S, E, W))

        #Setup the selection graph frame
        self.sgFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=600, height=200)
        self.sgFrame.grid(column=1, row=2, columnspan=3,  rowspan=1, sticky=(N, S, E, W))
        self.sgFrame.pack_propagate(False)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=3)
        mainframe.columnconfigure(2, weight=3)
        mainframe.columnconfigure(3, weight=3)
        mainframe.rowconfigure(0, weight=4)
        mainframe.rowconfigure(1, weight=4)
        mainframe.rowconfigure(2, weight=1)
        self.root.mainloop()

if __name__ == '__main__':
    #Make an instance of the application and run it
    fv = forceView()
    fv.run_app()
