import zrd_login
kite = zrd_login.kite
import talib
from pprint import pprint
import pdb
import pandas as pd
import support_file as get
import datetime
import time
import winsound

status = {'Signal_Sell': None,'Signal_Buy': None,}
trade_no = 0
Trade_log ={}



while True :
	name = 'SBIN'
	data = get.get_data(name=name, segment='NSE:', delta=5, interval='minute', continuous=False, oi=False)
	
	data['RSI'] = talib.RSI(data['close'], timeperiod=14)
	
	df  =  data.set_index(data['date'])
	
	completed_candle = pd.Series(datetime.datetime.now()).dt.floor('1min')[0]- datetime.timedelta(minutes=1)
	completed_candle = completed_candle.strftime("%Y-%m-%d %H:%M:%S+05:30")

	completed_candle_rsi_val = df.loc[completed_candle]['RSI']
	current_candle_rsi_val = round(data.iloc[-1]['RSI'],2)
	
	if (completed_candle_rsi_val) < 40 and (status['Signal_Sell'] is None):
		print(name)
		winsound.Beep(frequency=750, duration=100)

		status['Signal_Sell'] = 'Yes'
		trade_no  = trade_no + 1
		Trade_log[trade_no] = status
		status = {'Signal_Sell': None,'Signal_Buy': None,}

	if completed_candle_rsi_val > 60:
		print(name)
		winsound.Beep(frequency=750, duration=1000)
		trade_no  = trade_no + 1

		status['Signal_Buy'] = 'Yes'


		#  In complete !



	

	









