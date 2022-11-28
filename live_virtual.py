from pprint import pprint
import pandas as pd
import zrd_login
import datetime
import pdb
import talib as tb
import support_file01 as sf
import xlwings as xw

def init():

	global watchlist, status, kite, lot_multiplier, temp, breakout_time, breakin_time, capital,watchlist0,rsi,this_watchlist,inst,dfx,dfi,sht
	kite = zrd_login.kite
	watchlist0 = ['3MINDIA','ABB','POWERINDIA','ACC','AIAENG','APLAPOLLO','AUBANK','AARTIDRUGS','AARTIIND','AAVAS','ABBOTINDIA','ADANIENT','ADANIGREEN','ADANIPORTS','ATGL','ADANITRANS','ABCAPITAL','ABFRL','ADVENZYMES','AEGISCHEM','AFFLE','AJANTPHARM','AKZOINDIA','ALEMBICLTD','APLLTD','ALKEM','ALKYLAMINE','ALOKINDS','AMARAJABAT','AMBER','AMBUJACEM','ANGELBRKG','APOLLOHOSP','APOLLOTYRE','ASAHIINDIA','ASHOKLEY','ASHOKA','ASIANPAINT','ASTERDM','ASTRAZEN','ASTRAL','ATUL','AUROPHARMA','AVANTIFEED','DMART','AXISBANK','BASF','BEML','BSE','BAJAJ-AUTO','BAJAJCON','BAJAJELEC','BAJFINANCE','BAJAJFINSV','BAJAJHLDNG','BALAMINES','BALKRISIND','BALMLAWRIE','BALRAMCHIN','BANDHANBNK','BANKBARODA','BANKINDIA','MAHABANK','BATAINDIA','BAYERCROP','BERGEPAINT','BDL','BEL','BHARATFORG','BHEL','BPCL','BHARATRAS','BHARTIARTL','BIOCON','BIRLACORPN','BSOFT','BLISSGVS','BLUEDART','BLUESTARCO','BBTC','BOSCHLTD','BRIGADE','BRITANNIA','BURGERKING','CCL','CESC','CRISIL','CSBBANK','CADILAHC','CANFINHOME','CANBK','CAPLIPOINT','CGCL','CARBORUNIV','CASTROLIND','CEATLTD','CENTRALBK','CDSL','CENTURYPLY','CENTURYTEX','CERA','CHALET','CHAMBLFERT','CHOLAHLDNG','CHOLAFIN','CIPLA','CUB','COALINDIA','COCHINSHIP','COFORGE','COLPAL','CAMS','CONCOR','COROMANDEL','CREDITACC','CROMPTON','CUMMINSIND','CYIENT','DCBBANK','DCMSHRIRAM','DLF','DABUR','DALBHARAT','DEEPAKNTR','DELTACORP','DHANI','DHANUKA','DBL','DISHTV','DCAL','DIVISLAB','DIXON','LALPATHLAB','DRREDDY','EIDPARRY','EIHOTEL','EPL','EDELWEISS','EICHERMOT','ELGIEQUIP','EMAMILTD','ENDURANCE','ENGINERSIN','EQUITAS','ERIS','ESCORTS','EXIDEIND','FDC','FEDERALBNK','FINEORG','FINCABLES','FINPIPE','FSL','FORTIS','FCONSUMER','FRETAIL','GAIL','GEPIL','GMMPFAUDLR','GMRINFRA','GALAXYSURF','GRSE','GARFIBRES','GICRE','GILLETTE','GLAXO','GLENMARK','GODFRYPHLP','GODREJAGRO','GODREJCP','GODREJIND','GODREJPROP','GRANULES','GRAPHITE','GRASIM','GESHIP','GREAVESCOT','GRINDWELL','GUJALKALI','GAEL','FLUOROCHEM','GUJGASLTD','GNFC','GPPL','GSFC','GSPL','GULFOILLUB','HEG','HCLTECH','HDFCAMC','HDFCBANK','HDFCLIFE','HFCL','HAPPSTMNDS','HATSUN','HAVELLS','HEIDELBERG','HEMIPROP','HEROMOTOCO','HSCL','HINDALCO','HAL','HINDCOPPER','HINDPETRO','HINDUNILVR','HINDZINC','HONAUT','HUDCO','HDFC','HUHTAMAKI','ICICIBANK','ICICIGI','ICICIPRULI','ISEC','IDBI','IDFCFIRSTB','IDFC','IFBIND','IIFL','IIFLWAM','IOLCP','IRB','IRCON','ITC','ITI','INDIACEM','IBULHSGFIN','IBREALEST','INDIAMART','INDIANB','IEX','INDHOTEL','IOC','IOB','IRCTC','ICIL','INDOCO','IGL','INDUSTOWER','INDUSINDBK','INFIBEAM','NAUKRI','INFY','INGERRAND','INOXLEISUR','INTELLECT','INDIGO','IPCALAB','JBCHEPHARM','JKCEMENT','JKLAKSHMI','JKPAPER','JKTYRE','JMFINANCIL','JSWENERGY','JSWSTEEL','JTEKTINDIA','JAMNAAUTO','JINDALSAW','JSLHISAR','JSL','JINDALSTEL','JCHAC','JUBLFOOD','JUSTDIAL','JYOTHYLAB','KPRMILL','KEI','KNRCON','KPITTECH','KRBL','KSB','KAJARIACER','KALPATPOWR','KANSAINER','KARURVYSYA','KSCL','KEC','KOTAKBANK','L&TFH','LTTS','LICHSGFIN','LAOPALA','LAXMIMACH','LTI','LT','LAURUSLABS','LEMONTREE','LINDEINDIA','LUPIN','LUXIND','MASFIN','MMTC','MOIL','MRF','MGL','MAHSCOOTER','MAHSEAMLES','M&MFIN','M&M','MAHINDCIE','MHRIL','MAHLOG','MANAPPURAM','MRPL','MARICO','MARUTI','MFSL','MAXHEALTH','MAZDOCK','METROPOLIS','MINDTREE','MINDACORP','MINDAIND','MIDHANI','MOTHERSUMI','MOTILALOFS','MPHASIS','MCX','MUTHOOTFIN','NATCOPHARM','NBCC','NCC','NESCO','NHPC','NLCINDIA','NMDC','NOCIL','NTPC','NH','NATIONALUM','NFL','NAVINFLUOR','NESTLEIND','NETWORK18','NILKAMAL','NAM-INDIA','OBEROIRLTY','ONGC','OIL','OFSS','ORIENTELEC','ORIENTREF','PIIND','PNBHOUSING','PNCINFRA','PVR','PAGEIND','PERSISTENT','PETRONET','PFIZER','PHILIPCARB','PHOENIXLTD','PIDILITIND','PEL','POLYMED','POLYCAB','POLYPLEX','PFC','POWERGRID','PRESTIGE','PRINCEPIPE','PRSMJOHNSN','PGHL','PGHH','PNB','QUESS','RBLBANK','RECLTD','RITES','RADICO','RVNL','RAIN','RAJESHEXPO','RALLIS','RCF','RATNAMANI','RAYMOND','REDINGTON','RELAXO','RELIANCE','RESPONIND','ROSSARI','ROUTE','SBICARD','SBILIFE','SIS','SJVN','SKFINDIA','SRF','SANOFI','SCHAEFFLER','SCHNEIDER','SEQUENT','SHARDACROP','SFL','SHILPAMED','SCI','SHOPERSTOP','SHREECEM','SHRIRAMCIT','SRTRANSFIN','SIEMENS','SOBHA','SOLARINDS','SOLARA','SONATSOFTW','SPANDANA','SPICEJET','STARCEMENT','SBIN','SAIL','SWSOLAR','STLTECH','STAR','SUDARSCHEM','SUMICHEM','SPARC','SUNPHARMA','SUNTV','SUNCLAYLTD','SUNDARMFIN','SUNDRMFAST','SUNTECK','SUPRAJIT','SUPREMEIND','SUPPETRO','SUVENPHAR','SUZLON','SWANENERGY','SYMPHONY','SYNGENE','TCIEXP','TCNSBRANDS','TTKPRESTIG','TV18BRDCST','TVSMOTOR','TANLA','TASTYBITE','TATACHEM','TATACOFFEE','TATACOMM','TCS','TATACONSUM','TATAELXSI','TATAINVEST','TATAMTRDVR','TATAMOTORS','TATAPOWER','TATASTEEL','TEAMLEASE','TECHM','NIACL','RAMCOCEM','THERMAX','THYROCARE','TIMKEN','TITAN','TORNTPHARM','TORNTPOWER','TRENT','TRIDENT','TRITURBINE','TIINDIA','UCOBANK','UFLEX','UPL','UTIAMC','UJJIVAN','UJJIVANSFB','ULTRACEMCO','UNIONBANK','UBL','MCDOWELL-N','VGUARD','VMART','VIPIND','VSTIND','VAIBHAVGBL','VAKRANGEE','VALIANTORG','VTL','VARROC','VBL','VEDL','VENKEYS','VINATIORGA','IDEA','VOLTAS','WABCOINDIA','WELCORP','WELSPUNIND','WESTLIFE','WHIRLPOOL','WIPRO','WOCKPHARMA','YESBANK','ZEEL','ZENSARTECH','ZYDUSWELL','ECLERX']

	watchlist = []
	this_watchlist = []
	# fno_watchlist = ['BPCL', 'MOTHERSUMI', 'RBLBANK', 'SIEMENS', 'GODREJPROP', 'CANBK', 'MARICO', 'BEL', 'NAVINFLUOR', 'CADILAHC', 'SRF', 'DEEPAKNTR', 'UBL', 'NAUKRI', 'LUPIN', 'PVR', 'COLPAL', 'PNB', 'IOC', 'BHEL', 'PETRONET', 'IDFCFIRSTB', 'GRANULES', 'EICHERMOT', 'M&MFIN', 'VOLTAS', 'IGL', 'HINDPETRO', 'TVSMOTOR', 'TATACHEM', 'BANDHANBNK', 'HAVELLS', 'SUNTV', 'AUBANK', 'L&TFH', 'ADANIENT', 'M&M', 'LTI', 'HDFC', 'MINDTREE', 'INFY', 'RAMCOCEM', 'TATAMOTORS', 'SUNPHARMA', 'TITAN', 'SBILIFE', 'POWERGRID', 'VEDL', 'AARTIIND', 'NTPC', 'IBULHSGFIN', 'LICHSGFIN', 'UPL', 'RECLTD', 'BOSCHLTD', 'APLLTD', 'BRITANNIA', 'COFORGE', 'NAM-INDIA', 'JSWSTEEL', 'NMDC', 'GRASIM', 'HDFCAMC', 'HDFCLIFE', 'JINDALSTEL', 'PFC', 'SHREECEM', 'BANKBARODA', 'LTTS', 'AMARAJABAT', 'HCLTECH', 'APOLLOTYRE', 'MCDOWELL-N', 'BALKRISIND', 'ICICIGI', 'ALKEM', 'CUB', 'IRCTC', 'MPHASIS', 'ULTRACEMCO', 'AXISBANK', 'ASIANPAINT', 'TORNTPOWER', 'BHARATFORG', 'HINDALCO', 'ESCORTS', 'TATACONSUM', 'ZEEL', 'ASHOKLEY', 'DLF', 'GUJGASLTD', 'ICICIPRULI', 'LT', 'TORNTPHARM', 'CHOLAFIN', 'JUBLFOOD', 'ITC', 'INDUSTOWER', 'SRTRANSFIN', 'GMRINFRA', 'HEROMOTOCO', 'LALPATHLAB', 'EXIDEIND', 'BAJFINANCE', 'DABUR', 'GODREJCP', 'NATIONALUM', 'PEL', 'BIOCON', 'TCS', 'GAIL', 'GLENMARK', 'ACC', 'APOLLOHOSP', 'CIPLA', 'BAJAJ-AUTO', 'PIIND', 'BHARTIARTL', 'NESTLEIND', 'INDIGO', 'MRF', 'SBIN', 'COALINDIA', 'AUROPHARMA', 'DIVISLAB', 'BAJAJFINSV', 'RELIANCE', 'IDEA', 'TATAPOWER', 'WIPRO', 'ADANIPORTS', 'BERGEPAINT', 'TATASTEEL', 'FEDERALBNK', 'MFSL', 'KOTAKBANK', 'MGL', 'HINDUNILVR', 'TECHM', 'DRREDDY', 'SAIL', 'MARUTI', 'ICICIBANK', 'BATAINDIA', 'MUTHOOTFIN', 'HDFCBANK', 'ONGC', 'INDUSINDBK', 'PIDILITIND', 'AMBUJACEM', 'PAGEIND', 'TRENT', 'CONCOR', 'PFIZER', 'MANAPPURAM', 'CUMMINSIND']


	for name in watchlist0:
		df = sf.histo_data1(name = name,segment = "NSE:",delta = 42,delta1 = 1,interval= 'day',continuous = False,oi = False)
		df['rsi3'] = tb.RSI(df['close'], timeperiod = 3)
		df.to_csv('RSI(DAY)' + '\\' + name + '.csv')
		rsi = df.iloc[-1]['rsi3']
		if rsi > 80 or rsi < 30:
			watchlist.append(name)
	print(watchlist)		

	temp = {'name':None, 'date':None, 'entry_time':None, 'buy_script':None, 'sell_script':None, 'buy_ltp':None, 'sell_ltp':None,  'buy_qty':None, 'sell_qty': None,  'sl':None, 'target':None, 'exit_time':None, 'pnl':None, 'remark':None, 'traded':None, 'remark2':None}
	status = {}

	for name in watchlist:
		status[name] = temp.copy()

	for name in watchlist:							
		this_watchlist.append('NSE:' + name )
	# print(this_watchlist)
	inst = pd.DataFrame(kite.instruments())
	inst = inst.set_index(inst['tradingsymbol'])
	wb = xw.Book('live_status1.xlsx')
	sht = wb.sheets['Sheet1']


	capital = 6000
	lot_multiplier = 1
	
	# pdb.set_trace()

	breakin_time = datetime.time(9,15)
	breakout_time = datetime.time(15,15)

init()
while True:
	ctime = datetime.datetime.now()
	ctime1 = datetime.datetime.now().time()
	print(ctime)
	sht.range('A1').value = pd.DataFrame(status).T
	name_data = kite.quote(this_watchlist)
	
	for name in watchlist:
		# print (name)
		openn = name_data['NSE:' + name]['ohlc']['open']
		close = name_data['NSE:' + name]['ohlc']['close']
		high = name_data['NSE:' + name]['ohlc']['high']
		low = name_data['NSE:' + name]['ohlc']['low']
		ltp = name_data['NSE:' + name]['last_price']
		# inst_tick = inst.loc[name]['tick_size'][-1]
		# sl_pcts = (high + (inst_tick*2) 
		# sl_pctb = (low - inst_tick*2)
		dfx = pd.DataFrame(status).T
		no_of_trades = dfx[dfx['traded'] == 'yes'].shape[0]
		if (ctime1 > breakin_time) and (ctime1 < breakout_time) and (no_of_trades < 10): 
			if (rsi > 80) and (openn == high) and (status[name]['traded'] is None) and (80 < ltp < 5000):
				print('sell',name)					
				status[name]['name'] = name
				status[name]['date'] = str(ctime.date())
				status[name]['entry_time'] = str(ctime.time())
				status[name]['buy_script'] = None
				status[name]['sell_script'] = name
				status[name]['buy_ltp'] = None
				status[name]['sell_ltp'] = ltp
				status[name]['open'] = openn
				status[name]['high'] = high
				status[name]['low'] =  low
				status[name]['buy_qty'] = None
				status[name]['sell_qty'] = capital//ltp
				status[name]['sl'] = ((status[name]['sell_ltp']) + 0.01*(status[name]['sell_ltp']))
				status[name]['target'] = ((status[name]['sell_ltp']) - 0.01*(status[name]['sell_ltp']))
				status[name]['remark'] = 'sell'
				status[name]['traded'] = 'yes'
				# pdb.set_trace() 
				# sell_orderid = kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol= name, transaction_type=kite.TRANSACTION_TYPE_SELL, quantity=status[name]['qty'], product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET, price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
				# status[name]['sell_orderid'] = sell_orderid	
			if (rsi < 30) and (openn == low) and (status[name]['traded'] is None) and (80 < ltp < 5000):
				print('buy',name)					
				status[name]['name'] = name
				status[name]['date'] = str(ctime.date())
				status[name]['entry_time'] = str(ctime.time())
				status[name]['buy_script'] = name
				status[name]['sell_script'] = None
				status[name]['buy_ltp'] =  ltp
				status[name]['sell_ltp'] =  None
				status[name]['open'] = openn
				status[name]['high'] = high
				status[name]['low'] =  low
				status[name]['buy_qty'] = capital//ltp
				status[name]['sell_qty'] = None
				status[name]['sl'] = ((status[name]['buy_ltp']) - 0.01*(status[name]['buy_ltp']))
				status[name]['target'] = ((status[name]['buy_ltp']) + 0.01*(status[name]['buy_ltp']))
				status[name]['remark'] = 'buy'
				status[name]['traded'] = 'yes'					
				# buy_orderid = kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol= name, transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=status[name]['qty'], product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET, price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)			
				# status[name]['buy_orderid'] = buy_orderid
		if (status[name]['traded'] == 'yes') and ((ctime.time() < datetime.time(15,15))):
			if ((ltp > status[name]['sl']) or (ltp < status[name]['target'])) and (status[name]['remark2'] is None) and (status[name]['remark'] == 'sell'):
				print('buy1',name)
				status[name]['buy_ltp1'] =  ltp
				pnl1 = (status[name]['sell_ltp'] - status[name]['buy_ltp1'])*status[name]['sell_qty']
				# buy_orderid1 = kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol= name, transaction_type=kite.TRANSACTION_TYPE_BUY, quantity=status[name]['qty'], product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET, price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
				# status[name]['buy_orderid'] = buy_orderid1
				if (ltp > status[name]['sl']):
					status[name]['remark2'] = 'sl_hit'
				if (ltp < status[name]['target']):
					status[name]['remark2'] = 'target_hit'
				if (ctime.time() > datetime.time(15,15)):
					status[name]['remark2'] = 'market_over'
			if ((ltp < status[name]['sl']) or (ltp > status[name]['target'])) and (status[name]['remark2'] is None) and status[name]['remark'] == 'buy':
				print('sell1',name)
				status[name]['sell_ltp1'] =  ltp
				pnl1 = (status[name]['sell_ltp1'] - status[name]['buy_ltp'])*status[name]['buy_qty']
				# sell_orderid1 = kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE, tradingsymbol= name, transaction_type=kite.TRANSACTION_TYPE_SELL, quantity=status[name]['qty'], product=kite.PRODUCT_MIS, order_type=kite.ORDER_TYPE_MARKET, price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
				# status[name]['sell_orderid'] = sell_orderid1
				if (ltp < status[name]['sl']):
					status[name]['remark2'] = 'sl_hit'
				if (ltp > status[name]['target']):
					status[name]['remark2'] = 'target_hit'
				if (ctime.time() > datetime.time(15,15)):
					status[name]['remark2'] = 'market_over'
				status[name]['pnl'] = pnl1 + pnl2
				status[name]['exit_time'] = str(ctime.time())
				# status[name] = temp.copy()
