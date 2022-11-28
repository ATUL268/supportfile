# import zrd_login
# kite = zrd_login.kite
import talib
from pprint import pprint
import pdb
import pandas as pd
import support_file as get
import datetime
import time
import winsound


Watchlist = ['ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BPCL', 'BHARTIARTL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'HDFC', 'ICICIBANK', 'ITC', 'IOC', 'INDUSINDBK', 'INFY', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NTPC', 'NESTLEIND', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SHREECEM', 'SBIN', 'SUNPHARMA', 'TCS', 'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN', 'UPL', 'ULTRACEMCO', 'WIPRO']
status = {'name':None, 'date':None, 'buy_script':None, 'sell_script':None, 'buy_ltp':None, 'sell_ltp':None, 'entry_time':None, 'qty':None, 'sl':None, 'target':None, 'exit_time':None, 'pnl':None, 'remark':None, 'tarded':None, 'remark2':None}
final_result = {}
tradeno = 0

this_add = '21JUNFUT'
next_add = '21JULFUT'	

sl_pct = 1
entry_pct = 2
target_pct = 1.5




for name in Watchlist:
	print(name)
	winsound.Beep(frequency=750, duration=100)

	this,nextt =  get.read_data(name) 

	for index , ohlc in this.iterrows():
		try:
			this_name = name + this_add 
			next_name =  name + next_add 
			this_ltp = ohlc['close']  
			next_ltp = nextt.loc[index]['close']
			this_volume = ohlc['volume']  
			next_volume = nextt.loc[index]['volume']
		except Exception as e:
			continue

		diff = round(((this_ltp - next_ltp)/next_ltp) * 100,2)
		
		if diff > entry_pct :

			if (this_ltp > next_ltp) and (this_volume !=0) and (status['tarded'] is None):
				
				tradeno = tradeno + 1
				status['name'] = name
				status['date'] = index[:10]
				status['sell_script '] = this_name
				status['buy_script'] = next_name
				status['sell_ltp'] = this_ltp
				status['buy_ltp'] = next_ltp 
				status['entry_time'] = index
				status['qty'] = 1
				status['sl'] = diff + sl_pct
				status['target'] = diff - target_pct
				status['remark'] = 'this_next'
				status['tarded'] = 'Yes'
				# pdb.set_trace()

			if (next_ltp > this_ltp) and (this_volume !=0) and (status['tarded'] is None):

				tradeno = tradeno + 1
				status['name'] = name
				status['date'] = index[:10]
				status['sell_script '] = next_name
				status['buy_script'] = this_name
				status['sell_ltp'] = next_ltp
				status['buy_ltp'] = this_ltp
				status['entry_time'] = index
				status['qty'] = 1
				status['sl'] = diff + sl_pct
				status['target'] = diff - target_pct
				status['remark'] = 'next_this'
				status['tarded'] = 'Yes'
		
		if (status['tarded'] =='Yes'):


# 				Find PNL !!!!

			if (diff > status['sl'] ) or (diff < status['target']) or (index[11:16] == '15:15'):

				if (status['remark'] =='this_next') or (index[11:16] == '15:15'):

					pnl1 = (status['sell_ltp'] - this_ltp)*status['qty']
					pnl2 = (next_ltp - status['buy_ltp'] )*status['qty']

				if (status['remark'] == 'next_this') or (index[11:16] == '15:15'):

					pnl1 = (status['sell_ltp'] - next_ltp)*status['qty']
					pnl2 = (this_ltp - status['buy_ltp'] )*status['qty']


				status['exit'] = index
				status['pnl'] = pnl1 + pnl2

#				Give Remark !!!			


				if (diff > status['sl'] ):
					status['remark2'] = 'Stoploss_Hit'

				if (diff < status['target']):
					status['remark2'] = 'Target_Hit'

				if (index[11:16] == '15:15'):
					status['remark2'] = 'Market_over'

				# pdb.set_trace()

				final_result[tradeno] = status

				status = {'name':None, 'date':None, 'buy_script':None, 'sell_script':None, 'buy_ltp':None, 'sell_ltp':None, 'entry_time':None, 'qty':None, 'sl':None, 'target':None, 'exit_time':None, 'pnl':None, 'remark':None, 'tarded':None, 'remark2':None}

pd.DataFrame(final_result).T.to_csv('results3.csv')



				
  
   




		






# ______________________________________________________________________________________________________________________________
# 03.
# We are checking each one miniute candle to both futures contract so that we can find the difference and find arbitrage opportunities !!!





