#!/usr/bin/env python3
"""
Forceview setup file currently just does initial set up of database
"""

__author__ = "Aaron Diab"
__version__ = "0.1.0"
__license__ = "GPL V3"

import dbhandler as dbh

#Make an instance of the database handler
dh = dbh.dbHandler()
dh.createPatTable()
