# Econ 136 - Markets and Modeling
# March 5, 2018

# op_util.py
# 	Utility methods for pricing options


import math
import time
import date_util as dateu
import scipy as sp

def csnd(dval):
	"""
		Caclulate the standard normal distribution for dval
	"""
	return (1.0 + math.erf(dval/math.sqrt(2.0)))/2.0


def durvol(dayvol, days):
	"""
		Calculates the duration volatility given days to expiry and daily volatility
	"""
	return dayvol*math.sqrt(days)


def copo(stopr, strike, dayvol, days, rfir):

	d1 = math.log(stopr/strike)+((rfir/365)+(dayvol**2)/2)*days
	durvol = dayvol*math.sqrt(days)
	cumd1 = csnd(d1/durvol)
	cumd2 = csnd((d1/durvol) - durvol)
	discount = math.exp(-rfir*days/365)
	callpr = (stopr*cumd1)-(strike*discount*cumd2)

	delta = cumd1

	return (callpr, delta, durvol)

def popo(stopr, strike, dayvol, days, rfir):

	d1 = math.log(stopr/strike)+((rfir/365)+(dayvol**2)/2)*days
	durvol = dayvol*math.sqrt(days)
	cumd1 = csnd(-d1/durvol)
	cumd2 = csnd(-((d1/durvol) - durvol))
	discount = math.exp(-rfir*days/365)
	callpr = -(stopr*cumd1)+(strike*discount*cumd2)

	delta = cumd1
	
	return (callpr, delta, durvol)

