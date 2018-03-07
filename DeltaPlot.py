# Econ 136 - Markets and Modeling
# March 7, 2018

# DeltaPlot.py
# 	Plot delta curves

import op_util as opu
import date_util as dateu
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

stosym = "AA"
stopr = 45.60
strikeRange = [42, 52]
dayvol = float(0.023434)
rfir = float(0.025)

strikePrices = np.linspace(strikeRange[0], strikeRange[1], 11)

days = 11.0
marchDeltas = []

for strike in strikePrices:
	# if strike < stopr:
	(_, delta, _) = opu.popo(stopr, strike, dayvol, days, rfir)
	# else: 
	# 	(_, delta, _) = opu.copo(stopr, strike, dayvol, days, rfir)

	marchDeltas.append(delta)


aprilDeltas = []
days = 46.0

for strike in strikePrices:
	# if strike < stopr:
	(_, delta, _) = opu.popo(stopr, strike, dayvol, days, rfir)
	# else: 
	# 	(_, delta, _) = opu.copo(stopr, strike, dayvol, days, rfir)

	aprilDeltas.append(delta)

print("March: ", marchDeltas)
print("April: ", aprilDeltas)


# plotting
sns.set_style("darkgrid")
plt.rcParams["axes.labelsize"] = 15

plt.plot(strikePrices, marchDeltas, label="March Expiration (11 Days)")
plt.plot(strikePrices, aprilDeltas, label="April Expiration (46 Days)")

plt.legend()

plt.title(stosym + ' Delta Option Calculations')
plt.xlabel('Strike Price')
plt.ylabel('Delta')

plt.show()