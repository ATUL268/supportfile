from pprint import pprint
import pandas as pd
import datetime
import pdb
import support_file as get



watchlist = ['ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BPCL', 'BHARTIARTL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GAIL', 'GRASIM', 'HCLTECH', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'HDFC', 'ICICIBANK', 'ITC', 'IOC', 'INDUSINDBK', 'INFY', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NTPC', 'NESTLEIND', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SHREECEM', 'SBIN', 'SUNPHARMA', 'TCS', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN', 'UPL', 'ULTRACEMCO', 'WIPRO']


this_add = '21JUNFUT'
next_add = '21JULFUT'

sl_pct = 1.7
entry_pct = 1
target_pct = 0.3


for name in watchlist:
	print(name)

	this, nextt = get.read_data(name)
	for index, ohlc in this.iterrows():

		try:
			this_ltp = ohlc['close']
			next_ltp = nextt.loc[index]['close']
		except Exception as e:
			continue



		diff = round(((this_ltp - next_ltp)/next_ltp)*100, 2)

		if diff	 > 3:
			print(index, diff, name)
			pdb.set_trace()

