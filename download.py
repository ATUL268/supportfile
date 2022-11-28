from pprint import pprint
import pdb 
import pandas as pd
import time
import zrd_login
kite = zrd_login.kite
import datetime
import support_file as get
import talib






name = 'NIFTY BANK' 
df = get.get_data(name = name, segment = 'NSE:', delta = 2000, interval= 'day', continuous= False, oi=False)
df.to_csv('BN' + '\\' +name + '.csv')
print(name)
