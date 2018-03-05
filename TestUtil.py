import op_util as opu
import date_util as dateu


stosym = "TEST"
days = 4
stopr  = float(100)
strike = float(102)
dayvol = float(0.03205)
rfir = float(0.0225)

call_val = opu.copo(stopr, strike, dayvol, days, rfir)

print(call_val)