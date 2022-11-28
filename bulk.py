from pprint import pprint
import pdb 
import pandas as pd
import time
import zrd_login
kite = zrd_login.kite
import datetime
import support_file as get
import talib
import winsound
import xlwings as xw


watchlist3 = ['ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BPCL', 'BHARTIARTL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'HDFC', 'ICICIBANK', 'ITC', 'IOC', 'INDUSINDBK', 'INFY', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NTPC', 'NESTLEIND', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SHREECEM', 'SBIN', 'SUNPHARMA', 'TCS', 'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN', 'UPL', 'ULTRACEMCO', 'WIPRO']

for name in watchlist3:
	ltp = kite.ltp(['NSE:' + name])['NSE:' + name]['last_price']
	price1 = ltp-1
	qty = int(10000//ltp)
	if qty > 0:
		# kite.place_order(tradingsymbol = name ,exchange=kite.EXCHANGE_NSE,transaction_type=kite.TRANSACTION_TYPE_BUY,quantity= qty,order_type=kite.ORDER_TYPE_LIMIT,price=price1, product=kite.PRODUCT_CNC,variety=kite.VARIETY_AMO, validity = 'DAY')
		
		print(f"Stock {name} order placed at {price1} with Qty {qty}") 
