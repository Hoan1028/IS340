#Create an appointment class that cointains date and desc
class Appointment:
	#initialize constructor
	def __init__(self,day,month,year,desc):
		self._desc= desc
		self._year= year
		self._month= month
		self._day= day

	#compare dates of object and print if all match
	def occursOn(self,year,month,day):
		if year == self._year:
			if month == self._month:
				if day == self._day:
					print(self)

#inherits appointment
class Onetime(Appointment):
	def __init__(self,day,month,year,desc):
		Appointment.__init__(self,day,month,year,desc)
#inherits appointment		
class Daily(Appointment):
	def __init__(self,day,month,year,desc):
		Appointment.__init__(self,day,month,year,desc)
#inherits appointment		
class Monthly(Appointment):
	def __init__(self,day,month,year,desc):
		Appointment.__init__(self,day,month,year,desc)
		
