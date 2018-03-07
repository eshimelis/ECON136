# Econ 136 - Markets and Modeling
# March 5, 2018

# date_util.py
# 	Utility methods for date handling


import datetime as date

def days2exp(exyear, exmonth, exday):
	"""
		Calculate the days to expiry from today
	"""
	tnow = date.today()
	expiry = date(exyear, exmonth, exday)
	days2expiry = abs(expiry - tnow)
	return int(days2expiry.days)