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

watchlist = ['3MINDIA','ABB','POWERINDIA','ACC','AIAENG','APLAPOLLO','AUBANK','AARTIDRUGS','AARTIIND','AAVAS','ABBOTINDIA','ADANIENT','ADANIGREEN','ADANIPORTS','ATGL','ADANITRANS','ABCAPITAL','ABFRL','ADVENZYMES','AEGISCHEM','AFFLE','AJANTPHARM','AKZOINDIA','ALEMBICLTD','APLLTD','ALKEM','ALKYLAMINE','ALOKINDS','AMARAJABAT','AMBER','AMBUJACEM','ANGELBRKG','APOLLOHOSP','APOLLOTYRE','ASAHIINDIA','ASHOKLEY','ASHOKA','ASIANPAINT','ASTERDM','ASTRAZEN','ASTRAL','ATUL','AUROPHARMA','AVANTIFEED','DMART','AXISBANK','BASF','BEML','BSE','BAJAJ-AUTO','BAJAJCON','BAJAJELEC','BAJFINANCE','BAJAJFINSV','BAJAJHLDNG','BALAMINES','BALKRISIND','BALMLAWRIE','BALRAMCHIN','BANDHANBNK','BANKBARODA','BANKINDIA','MAHABANK','BATAINDIA','BAYERCROP','BERGEPAINT','BDL','BEL','BHARATFORG','BHEL','BPCL','BHARATRAS','BHARTIARTL','BIOCON','BIRLACORPN','BSOFT','BLISSGVS','BLUEDART','BLUESTARCO','BBTC','BOSCHLTD','BRIGADE','BRITANNIA','BURGERKING','CCL','CESC','CRISIL','CSBBANK','CADILAHC','CANFINHOME','CANBK','CAPLIPOINT','CGCL','CARBORUNIV','CASTROLIND','CEATLTD','CENTRALBK','CDSL','CENTURYPLY','CENTURYTEX','CERA','CHALET','CHAMBLFERT','CHOLAHLDNG','CHOLAFIN','CIPLA','CUB','COALINDIA','COCHINSHIP','COFORGE','COLPAL','CAMS','CONCOR','COROMANDEL','CREDITACC','CROMPTON','CUMMINSIND','CYIENT','DCBBANK','DCMSHRIRAM','DLF','DABUR','DALBHARAT','DEEPAKNTR','DELTACORP','DHANI','DHANUKA','DBL','DISHTV','DCAL','DIVISLAB','DIXON','LALPATHLAB','DRREDDY','EIDPARRY','EIHOTEL','EPL','EDELWEISS','EICHERMOT','ELGIEQUIP','EMAMILTD','ENDURANCE','ENGINERSIN','EQUITAS','ERIS','ESCORTS','EXIDEIND','FDC','FEDERALBNK','FINEORG','FINCABLES','FINPIPE','FSL','FORTIS','FCONSUMER','FRETAIL','GAIL','GEPIL','GMMPFAUDLR','GMRINFRA','GALAXYSURF','GRSE','GARFIBRES','GICRE','GILLETTE','GLAXO','GLENMARK','GODFRYPHLP','GODREJAGRO','GODREJCP','GODREJIND','GODREJPROP','GRANULES','GRAPHITE','GRASIM','GESHIP','GREAVESCOT','GRINDWELL','GUJALKALI','GAEL','FLUOROCHEM','GUJGASLTD','GNFC','GPPL','GSFC','GSPL','GULFOILLUB','HEG','HCLTECH','HDFCAMC','HDFCBANK','HDFCLIFE','HFCL','HAPPSTMNDS','HATSUN','HAVELLS','HEIDELBERG','HEMIPROP','HEROMOTOCO','HSCL','HINDALCO','HAL','HINDCOPPER','HINDPETRO','HINDUNILVR','HINDZINC','HONAUT','HUDCO','HDFC','HUHTAMAKI','ICICIBANK','ICICIGI','ICICIPRULI','ISEC','IDBI','IDFCFIRSTB','IDFC','IFBIND','IIFL','IIFLWAM','IOLCP','IRB','IRCON','ITC','ITI','INDIACEM','IBULHSGFIN','IBREALEST','INDIAMART','INDIANB','IEX','INDHOTEL','IOC','IOB','IRCTC','ICIL','INDOCO','IGL','INDUSTOWER','INDUSINDBK','INFIBEAM','NAUKRI','INFY','INGERRAND','INOXLEISUR','INTELLECT','INDIGO','IPCALAB','JBCHEPHARM','JKCEMENT','JKLAKSHMI','JKPAPER','JKTYRE','JMFINANCIL','JSWENERGY','JSWSTEEL','JTEKTINDIA','JAMNAAUTO','JINDALSAW','JSLHISAR','JSL','JINDALSTEL','JCHAC','JUBLFOOD','JUSTDIAL','JYOTHYLAB','KPRMILL','KEI','KNRCON','KPITTECH','KRBL','KSB','KAJARIACER','KALPATPOWR','KANSAINER','KARURVYSYA','KSCL','KEC','KOTAKBANK','L&TFH','LTTS','LICHSGFIN','LAOPALA','LAXMIMACH','LTI','LT','LAURUSLABS','LEMONTREE','LINDEINDIA','LUPIN','LUXIND','MASFIN','MMTC','MOIL','MRF','MGL','MAHSCOOTER','MAHSEAMLES','M&MFIN','M&M','MAHINDCIE','MHRIL','MAHLOG','MANAPPURAM','MRPL','MARICO','MARUTI','MFSL','MAXHEALTH','MAZDOCK','METROPOLIS','MINDTREE','MINDACORP','MINDAIND','MIDHANI','MOTHERSUMI','MOTILALOFS','MPHASIS','MCX','MUTHOOTFIN','NATCOPHARM','NBCC','NCC','NESCO','NHPC','NLCINDIA','NMDC','NOCIL','NTPC','NH','NATIONALUM','NFL','NAVINFLUOR','NESTLEIND','NETWORK18','NILKAMAL','NAM-INDIA','OBEROIRLTY','ONGC','OIL','OFSS','ORIENTELEC','ORIENTREF','PIIND','PNBHOUSING','PNCINFRA','PVR','PAGEIND','PERSISTENT','PETRONET','PFIZER','PHILIPCARB','PHOENIXLTD','PIDILITIND','PEL','POLYMED','POLYCAB','POLYPLEX','PFC','POWERGRID','PRESTIGE','PRINCEPIPE','PRSMJOHNSN','PGHL','PGHH','PNB','QUESS','RBLBANK','RECLTD','RITES','RADICO','RVNL','RAIN','RAJESHEXPO','RALLIS','RCF','RATNAMANI','RAYMOND','REDINGTON','RELAXO','RELIANCE','RESPONIND','ROSSARI','ROUTE','SBICARD','SBILIFE','SIS','SJVN','SKFINDIA','SRF','SANOFI','SCHAEFFLER','SCHNEIDER','SEQUENT','SHARDACROP','SFL','SHILPAMED','SCI','SHOPERSTOP','SHREECEM','SHRIRAMCIT','SRTRANSFIN','SIEMENS','SOBHA','SOLARINDS','SOLARA','SONATSOFTW','SPANDANA','SPICEJET','STARCEMENT','SBIN','SAIL','SWSOLAR','STLTECH','STAR','SUDARSCHEM','SUMICHEM','SPARC','SUNPHARMA','SUNTV','SUNCLAYLTD','SUNDARMFIN','SUNDRMFAST','SUNTECK','SUPRAJIT','SUPREMEIND','SUPPETRO','SUVENPHAR','SUZLON','SWANENERGY','SYMPHONY','SYNGENE','TCIEXP','TCNSBRANDS','TTKPRESTIG','TV18BRDCST','TVSMOTOR','TANLA','TASTYBITE','TATACHEM','TATACOFFEE','TATACOMM','TCS','TATACONSUM','TATAELXSI','TATAINVEST','TATAMTRDVR','TATAMOTORS','TATAPOWER','TATASTEEL','TEAMLEASE','TECHM','NIACL','RAMCOCEM','THERMAX','THYROCARE','TIMKEN','TITAN','TORNTPHARM','TORNTPOWER','TRENT','TRIDENT','TRITURBINE','TIINDIA','UCOBANK','UFLEX','UPL','UTIAMC','UJJIVAN','UJJIVANSFB','ULTRACEMCO','UNIONBANK','UBL','MCDOWELL-N','VGUARD','VMART','VIPIND','VSTIND','VAIBHAVGBL','VAKRANGEE','VALIANTORG','VTL','VARROC','VBL','VEDL','VENKEYS','VINATIORGA','IDEA','VOLTAS','WABCOINDIA','WELCORP','WELSPUNIND','WESTLIFE','WHIRLPOOL','WIPRO','WOCKPHARMA','YESBANK','ZEEL','ZENSARTECH','ZYDUSWELL','ECLERX']
traded = []
for name in watchlist:
	data = get.get_data(name=name, segment='NSE:', delta=20, interval='day', continuous=False, oi=False)
	df = pd.DataFrame(data)

	df['rsi_3'] = talib.RSI(df['close'], timeperiod=3)
	rsi = round(df.iloc[-1]['rsi_3'],2)

	openn,high,low,close = get.ohlc(name)
	ltp = get.LTP(name)

	if (rsi < 30) and (openn == low) and (name not in traded):
		traded.append(name)
		print(f"Buy___{name} rsi is less than 30 & open = low ltp is {ltp}")
		winsound.Beep(frequency=750, duration=100)

	if (rsi > 75) and (openn == high) and (name not in traded):
		traded.append(name)
		print(f"Sell___{name} rsi is more than 75 & open = high ltp is {ltp}")
		winsound.Beep(frequency=750, duration=1000)
		# pdb.set_trace()




# df['10_day_MA'] = talib.MA(df['close'], timeperiod=10, matype=0)
# MA_10 = df.iloc[-1]['10_day_MA']




# real = talib.MA(df['close'], timeperiod=10, matype=0)
# df['50_day_MA'] = talib.MA(df['close'], timeperiod=50, matype=0)

# mov_avg_value = df[-1:]['50_day_MA']

# print(mov_avg_value)





	















