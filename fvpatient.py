#!/usr/bin/env python3
"""
ForceView patient class. This class represents a patient that is being studied
"""

__author__ = "Aaron Diab"
__version__ = "0.1.0"
__license__ = "GPL V3"

class fvPatient:

    def __init__(self):
        self.lname = ""
        self.fname = ""
        self.dob = ""
        self.patid = "" 
    
    #Returns the SQL needed to insert a patient
    def genInsertSQL(self):
            return '''INSERT INTO patients({},{},{}) 
                      VALUES(?,?,?) '''.format(self.lname, self.fname, self.dob)

    #Returns the SQL needed to find a patient in the DB
    def genQuerySQL(self):
        return '''SELECT last_name, first_name, date_of_birth, id
                  FROM patients
                  WHERE last_name={}'''.format(self.lname)

    #Returns the SQL needed to delete a patient
    def genDeleteSQL(self):
        return '''DELETE FROM patients 
                  WHERE id={}'''.format(self.id)
    
    #Set patient info
    def setPatInfo(self, lname, fname, dob, patid):
        self.lname = lname
        self.fname = fname
        self.dob = dob
        self.patid = patid

    #Retun all patient info
    def getPatInfo(self):
        return self.lname, self.fname, self.dob, self.patid

    #Set the id for a patient that we queried from the DB
    def setId(self, id):
        self.id = id

if __name__ == '__main__':
    #Make an instance of the application and run it
    pat = fvPatient()
    pat.setPatInfo('Doe', 'Jane', '1-2-1945', '123-45-6789')
    print(type(pat.lname))
