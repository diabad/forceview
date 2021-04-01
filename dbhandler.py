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
        #Set the dbFile name so the database can be opened
        self.dbFile = self.progDir + '\\fvdatabase.db'
        #Establish db connection
        self.dbConn = self.connectToDB(self.dbFile)

    #Establishes a connection to the database
    def connectToDB(self, dbfile):
        #Initialize the connection variable
        dbConn = None
        try:
            dbConn = sqlite3.connect(dbfile)
            return dbConn
        except Error as err:
            print(err)
        
        return dbConn

    
    def createTable(self, dbconn, tableSQL):
        #Create the database cursor
        try:
            dbCur = dbconn.cursor()
            dbCur.execute(tableSQL)
        except Error as err:
            print(err)

    def createPatTable(self):
        #SQL to create the patient table
        patTableSQL = """ CREATE TABLE IF NOT EXISTS patients (
                            id integer PRIMARY KEY,
                            last_name text NOT NULL,
                            first_name text NOT NULL,
                            date_of_birth text,
                            patient_id
                        ); """
        if self.dbConn is not None:
            self.createTable(self.dbConn, patTableSQL)
        else:
            print("Error opening connection to database!")

    def createPatient(self, patient):
        #SQL to insert a new patient into the database
        sql = ''' INSERT INTO patients(last_name,first_name,date_of_birth,patient_id) VALUES(?,?,?,?) '''

        #Create the db cursor
        dbCur = self.dbConn.cursor()
        dbCur.execute(sql, patient)
        self.dbConn.commit()

        return dbCur.lastrowid

if __name__ == '__main__':
    #Make an instance of the application and run it
    dh = dbHandler()
    dh.createPatTable()
    patient = ('Doe', 'John', '1-1-1945', 987-65-4321)
    dh.createPatient(patient)

