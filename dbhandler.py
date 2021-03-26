#!/usr/bin/env python3
"""
ForceView dbhandler class. This class handles initial creation of the database, table setup and 
reading data from and writing to the database.
"""

__author__ = "Aaron Diab"
__version__ = "0.1.0"
__license__ = "GPL V3"

import sqlite3
from sqlite3 import Error
import os

class dbHandler:

    def __init__(self):
        #Get the applications base directory
        self.progDir = os.path.dirname(os.path.abspath(__file__))

    #def dbConn(dbfile):

    #def run_startup(self):
        #self.root.mainloop()

if __name__ == '__main__':
    #Make an instance of the application and run it
    dh = dbHandler()
    print(dh.progDir)
