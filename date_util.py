
import datetime as date

def days2exp(exyear, exmonth, exday):
	"""
		Calculate the days to expiry
	"""
	tnow = date.today()
	expiry = date(exyear, exmonth, exday)
	days2expiry = abs(expiry - tnow)
	return int(days2expiry.days)