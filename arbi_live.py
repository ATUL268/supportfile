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

def init():

	global watchlist, status, kite, this_add, next_add	, sl_pct, entry_pct	, target_pct, lot_multiplier, this_watchlist, next_watchlist,inst,sht, temp


	watchlist = ['BPCL', 'MOTHERSUMI', 'RBLBANK', 'SIEMENS', 'GODREJPROP', 'CANBK', 'MARICO', 'BEL', 'NAVINFLUOR', 'CADILAHC', 'SRF', 'DEEPAKNTR', 'UBL', 'NAUKRI', 'LUPIN', 'PVR', 'COLPAL', 'PNB', 'IOC', 'BHEL', 'PETRONET', 'IDFCFIRSTB', 'GRANULES', 'EICHERMOT', 'M&MFIN', 'VOLTAS', 'IGL', 'HINDPETRO', 'TVSMOTOR', 'TATACHEM', 'BANDHANBNK', 'HAVELLS', 'SUNTV', 'AUBANK', 'L&TFH', 'ADANIENT', 'M&M', 'LTI', 'HDFC', 'MINDTREE', 'INFY', 'RAMCOCEM', 'TATAMOTORS', 'SUNPHARMA', 'TITAN', 'SBILIFE', 'POWERGRID', 'VEDL', 'AARTIIND', 'NTPC', 'IBULHSGFIN', 'LICHSGFIN', 'UPL', 'RECLTD', 'BOSCHLTD', 'APLLTD', 'BRITANNIA', 'COFORGE', 'NAM-INDIA', 'JSWSTEEL', 'NMDC', 'GRASIM', 'HDFCAMC', 'HDFCLIFE', 'JINDALSTEL', 'PFC', 'SHREECEM', 'BANKBARODA', 'LTTS', 'AMARAJABAT', 'HCLTECH', 'APOLLOTYRE', 'MCDOWELL-N', 'BALKRISIND', 'ICICIGI', 'ALKEM', 'CUB', 'IRCTC', 'MPHASIS', 'ULTRACEMCO', 'AXISBANK', 'ASIANPAINT', 'TORNTPOWER', 'BHARATFORG', 'HINDALCO', 'ESCORTS', 'TATACONSUM', 'ZEEL', 'ASHOKLEY', 'DLF', 'GUJGASLTD', 'ICICIPRULI', 'LT', 'TORNTPHARM', 'CHOLAFIN', 'JUBLFOOD', 'ITC', 'INDUSTOWER', 'SRTRANSFIN', 'GMRINFRA', 'HEROMOTOCO', 'LALPATHLAB', 'EXIDEIND', 'BAJFINANCE', 'DABUR', 'GODREJCP', 'NATIONALUM', 'PEL', 'BIOCON', 'TCS', 'GAIL', 'GLENMARK', 'ACC', 'APOLLOHOSP', 'CIPLA', 'BAJAJ-AUTO', 'PIIND', 'BHARTIARTL', 'NESTLEIND', 'INDIGO', 'MRF', 'SBIN', 'COALINDIA', 'AUROPHARMA', 'DIVISLAB', 'BAJAJFINSV', 'RELIANCE', 'IDEA', 'TATAPOWER', 'WIPRO', 'ADANIPORTS', 'BERGEPAINT', 'TATASTEEL', 'FEDERALBNK', 'MFSL', 'KOTAKBANK', 'MGL', 'HINDUNILVR', 'TECHM', 'DRREDDY', 'SAIL', 'MARUTI', 'ICICIBANK', 'BATAINDIA', 'MUTHOOTFIN', 'HDFCBANK', 'ONGC', 'INDUSINDBK', 'PIDILITIND', 'AMBUJACEM', 'PAGEIND', 'TRENT', 'CONCOR', 'PFIZER', 'MANAPPURAM', 'CUMMINSIND']

	temp =  {'Name':None, 'Entry_Date':None, 'Buy_script':None, 'Sell_script':None, 'Buy_Price':None, 'Sell_Price':None, 'Entry_time':None, 'Qty':None, 'StopLoss':None, 'Target': None, 'Exit_time':None, 'PNL':None, 'Remark':None, 'Traded':None, 'Remark_2':None,'Exit_Date' : None , 'Exit_time': None, 'Diff': None}

	status = {}

	for name in watchlist:
		status[name] = temp.copy()

	kite = zrd_login.kite

	this_add = '21JUNFUT'
	next_add = '21JULFUT'

	this_watchlist = []
	next_watchlist = []

	for name in watchlist:
		this_watchlist.append('NFO:' + name + this_add)

	for name in watchlist:
		next_watchlist.append('NFO:' + name + next_add)

	sl_pct = 2
	entry_pct = 2.5
	target_pct = 0.5
	lot_multiplier = 1

	inst = pd.DataFrame(kite.instruments())
	inst = inst.set_index(inst['tradingsymbol']) 

	wb = xw.Book('live_status.xlsx')
	sht = wb.sheets['Sheet1']

	


init()


while True:


	this_data = kite.ltp(this_watchlist)
	next_data = kite.ltp(next_watchlist)
	ctime = datetime.datetime.now()
	# pdb.set_trace()
	# print(ctime)

	sht.range('A1').value = pd.DataFrame(status).T
	# pdb.set_trace()

	for name in watchlist:

		this_name = name + this_add
		next_name = name + next_add

		this_ltp = this_data['NFO:' + this_name]['last_price']
		next_ltp = next_data['NFO:' + next_name]['last_price']
		diff = abs(round(((this_ltp - next_ltp)/next_ltp)*100, 2))

		if diff > entry_pct:

			if (this_ltp > next_ltp) and (status[name]['Traded'] is None):

				status[name]['Name'] = name
				status[name]['Entry_Date'] = str(ctime.date())
				status[name]['Sell_script'] =  this_name
				status[name]['Buy_script'] = next_name
				status[name]['Sell_Price'] = this_ltp
				status[name]['Buy_Price'] = next_ltp
				status[name]['Entry_time'] = str(ctime.time())
				status[name]['Qty'] = lot_multiplier*inst.loc[this_name]['lot_size']
				status[name]['StopLoss'] = diff + sl_pct
				status[name]['Target'] = diff - sl_pct
				status[name]['Diff'] = diff
				status[name]['Remark'] = 'This_Next'
				status[name]['Traded']  = 'Yes'


			if (next_ltp > this_ltp) and (status[name]['Traded'] is None):


				status[name]['Name'] = name
				status[name]['Entry_Date'] = str(ctime.date())
				status[name]['Sell_script'] =  next_name
				status[name]['Buy_script'] = this_name
				status[name]['Sell_Price'] = next_ltp
				status[name]['Buy_Price'] = this_ltp
				status[name]['Entry_time'] = str(ctime.time())
				status[name]['Qty'] = lot_multiplier*inst.loc[this_name]['lot_size']
				status[name]['StopLoss'] = diff + sl_pct
				status[name]['Target'] = diff - sl_pct
				status[name]['Diff'] = diff
				status[name]['Remark'] = 'Next_This'
				status[name]['Traded']  = 'Yes'

		if (status[name]['Traded']  == 'Yes'):

			if (diff > status[name]['StopLoss']) or (diff < status[name]['Target']) or (ctime.time() > datetime.time(15, 15)):


				# if (status[name]['Remark'] = 'This_Next'):
				# 	status[name]['PNL'] = 

					# Complete PNL And reddy it !!! Everything id alright!



				# give remark
				if (diff > status[name]['StopLoss']):

					status[name]['Remark_2'] = 'StopLoss_Hit'



				if (diff < status[name]['Target']):

					status[name]['Remark_2'] = 'Target_Hit'



				if ((str(ctime.time()))[0:5]) == '15:15':

					status[name]['Remark_2'] = 'Market_Over'

				status[name]['Exit_time'] = str(ctime.time())
				# pdb.set_trace()



				

# Complete for Virtual Trading --- Made for Google Cloud Platform----!!! soni90_pc Date !   08/06/2021





