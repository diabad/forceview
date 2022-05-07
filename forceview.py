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
        self.selPoint = 0
        progEntry = su.fvStartup(self.currPat)
        progEntry.run_startup()
        self.root = Tk()
        self.root.title("Force View")
        #Create the figure and axes for plots
        self.selFig, self.selAx = plt.subplots()
        plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

    #Opens a dialog to allow you to open a new datafile
    def openNewFile(self):
        #Get the # of samples in a day with 250 samples in a second
        self.sampsPerDay = 250*60*60*24

        #Prompt the user for the data file
        dataFile = filedialog.askopenfilename()
        self.graphData = np.fromfile(dataFile, dtype='<u2')
        totNumSamps = self.graphData.size
        daysInFile = int(totNumSamps/self.sampsPerDay)+1
        self.ndEntryStr.set(daysInFile)

        #Plot the selection graph
        self.plotSelGraph()

    #Opens a dialog to allow you to open an existing datafile
    def openExtantFile(self):
        pass
       
    #Plot the Selection graph type = type of graph sel or main
    def plotSelGraph(self):
        #Create the selection plot
        self.selAx.set_xlim(xmin=0, xmax=self.graphData.size)
        self.selAx.set_ylim(ymin=-5, ymax=np.amax(self.graphData)+50)
        self.selAx.axes.xaxis.set_ticks([])
        self.selAx.axes.yaxis.set_ticks([])
        self.selAx.plot(self.graphData)
        selGraphCanvas = FigureCanvasTkAgg(self.selFig, master=self.sgFrame)
        selGraphCanvas.draw()
        selGraphCanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        selGraphCanvas.mpl_connect('button_press_event', self.selMousePos)

    def selMousePos(self,event):
        #Set the select point with a mouse click and load main graph
        selPosX, selPosY = int(event.xdata), int(event.ydata)
        self.selPoint = selPosX
        #Set the selected day entry box
        self.dsEntryStr.set(int(selPosX/self.sampsPerDay))
        print('x = %d, y = %d' % (selPosX, selPosY))

        #Plot the main window graph
        line = self.mainGraphLine.pop(0)
        line.remove()
        if self.selPoint + 21600000 < self.graphData.size:
            endPoint = self.selPoint + 21600000
        else:
            endPoint = self.graphData.size 
        self.mainAx.set_xlim(xmin=0, xmax=(endPoint-self.selPoint))
        self.mainAx.set_ylim(ymin=-5, ymax=np.amax(self.graphData)+50)
        self.mainGraphLine = self.mainAx.plot(self.graphData[self.selPoint:endPoint])
        self.mainFig.tight_layout()
        self.graphCanvas.draw()

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
        dsLabel = ttk.Label(dsFrame, text="Day selected")
        dsLabel.grid(sticky = (N, W))
        self.dsEntryStr = StringVar()
        dsEntry = ttk.Entry(dsFrame, textvariable=self.dsEntryStr)
        dsEntry.grid(sticky = (N, W))

        #Setup the graph selection data frame 
        gsFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=200, height=200)
        gsFrame.grid(column=0, row=2, sticky=(N,S))
        gsFrame.grid_propagate(False)
        gsTitle = ttk.Label(gsFrame, text="Selection Graph", font=titleFont)
        gsTitle.grid(sticky = (N, W))
        ndLabel = ttk.Label(gsFrame, text="Number of days in file")
        ndLabel.grid(sticky = (N, W))
        self.ndEntryStr = StringVar()
        ndEntry = ttk.Entry(gsFrame, textvariable=self.ndEntryStr)
        ndEntry.grid(sticky = (N, W))

        #Setup the main graph frame
        self.mgFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=600, height=400)
        self.mgFrame.grid(column=1, row=0, columnspan=3,  rowspan=2, sticky=(N, S, E, W))
        #Create the main graph figure and axis
        self.mainFig, self.mainAx = plt.subplots()
        #Setup the main graph canvas
        self.graphCanvas = FigureCanvasTkAgg(self.mainFig, master=self.mgFrame)
        self.graphCanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        #Set up the main graph axes
        self.mainAx.set(xlabel='Samples', ylabel='Force (N)')
        self.mainGraphLine = self.mainAx.plot(0,0)
        #Create the main graph toolbar
        grahpToolbar = NavigationToolbar2Tk(self.graphCanvas, self.mgFrame).update()
        self.graphCanvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

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
