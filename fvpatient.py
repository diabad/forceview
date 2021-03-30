class fvpatient(lname, fname, dob):
	def __init__(self, lname, fname, dob):
		self.lname = lname
		self.fname = fname
		self.dob = dob
		self.id = None
	
	#Returns the SQL needed to insert a patient
	def insertSQL(self):
		return ''' INSERT INTO patients({},{},{}) 
                           VALUES(?,?,?) '''.format(self.lname, self.fname, self.dob)

	#Returns the SQL needed to find a patient in the DB
	def querySQL(self):
		return '''SELECT last_name, first_name, date_of_birth, id
			  FROM patients
			  WHERE last_name={}'''.format(self.lname)

	#Returns the SQL needed to delete a patient
	def deleteSQL(self):
		return '''DELETE FROM patients 
			  WHERE id={}'''.format(self.id)

	#Set the id for a patient that we queried from the DB
	def setId(self, id):
		self.id = id

