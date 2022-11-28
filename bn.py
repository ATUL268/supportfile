from pprint import pprint
import pdb 
import pandas as pd
import time
# import zrd_login
# kite = zrd_login.kite
import datetime
import support_file as get
import talib

# BackTesting Code for RSI   !!!

status = {'Name':None, 'Entry_Date':None, 'Buy_script':None, 'Sell_script':None, 'Buy_Price':None, 'Sell_Price':None, 'Entry_time':None, 'Qty':None, 'StopLoss':None, 'Target': None, 'Exit_time':None, 'PNL':None, 'Remark':None, 'Traded':None, 'Remark_2':None,'Remark_3':None, 'RSI_value_Buy': None,'RSI_value_Sell': None, 'Exit_Date' : None , 'Exit_time': None}
final_result = {}
trade_no = 0 

	
# Reading historical Data !!!
data = pd.read_csv('BN' + '\\'+ 'NIFTY BANK.csv')
nifty =  data.set_index(data['date'])
nifty['rsi_3'] = round(talib.RSI(nifty['close'], timeperiod=3),2)

# iterration day by day to read ltp and rsi values
for index,values in nifty.iterrows():

	try:
		nifty_ltp = values['close']
		nifty_rsi_3 = values['rsi_3']

	
	except Exception as e:
		continue


# if condition to check rsi values !!! 
	if nifty_rsi_3 < 15 :

		if (nifty_rsi_3 < 15) and (status['Traded'] is None):
			
			trade_no = trade_no + 1
	
			status['Name'] = 'NIFTYBANK_INDEX'
			status['Entry_Date'] = index[:10]
			status['Buy_script'] = 'NIFTYBANK_INDEX'
			status['Sell_script'] = 'NIFTYBANK_INDEX'
			status['Buy_Price'] = values['close']
			
			status['Entry_time'] = index[:10]
			status['Qty'] = 1
			status['StopLoss'] = values['close']-values['close']*0.99
			status['Target'] = values['close']+values['close']*0.03
			status['Traded'] = 'Yes' 
			status['Remark'] = 'RSI_3_Buy' 
			status['RSI_value_Buy'] = values['rsi_3']
		
	if (status['Traded'] == 'Yes'):
	
		if (nifty_ltp < status['StopLoss']) or (nifty_ltp > status['Target']):

			PNL = round((nifty_ltp- status['Buy_Price']) * status['Qty'],2)

			status['PNL'] = PNL
			status['Sell_Price'] = nifty_ltp
			status['RSI_value_Sell'] = values['rsi_3']
			status['Exit_Date'] = index[:10]
			status['Exit_time'] = index[:10]

			if (nifty_ltp < status['StopLoss']):
				status['Remark_2'] = 'StopLoss_Hit'

			if (nifty_ltp > status['Target']):
				status['Remark_2'] = 'Target_Hit'



			final_result[trade_no] = status

			status = {'Name':None, 'Entry_Date':None, 'Buy_script':None, 'Sell_script':None, 'Buy_Price':None, 'Sell_Price':None, 'Entry_time':None, 'Qty':None, 'StopLoss':None, 'Target': None, 'Exit_time':None, 'PNL':None, 'Remark':None, 'Traded':None, 'Remark_2':None,'Remark_3':None, 'RSI_value_Buy': None,'RSI_value_Sell': None, 'Exit_Date' : None , 'Exit_time': None}

			
pd.DataFrame(final_result).T.to_csv('RSI_3_Day_no_sl_15.csv')


	



		
	





