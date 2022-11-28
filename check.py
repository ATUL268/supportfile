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



watchlist=['NSE:3MINDIA', 'NSE:ABB', 'NSE:POWERINDIA', 'NSE:ACC', 'NSE:AIAENG', 'NSE:APLAPOLLO', 'NSE:AUBANK', 'NSE:AARTIDRUGS', 'NSE:AARTIIND', 'NSE:AAVAS', 'NSE:ABBOTINDIA', 'NSE:ADANIENT', 'NSE:ADANIGREEN', 'NSE:ADANIPORTS', 'NSE:ATGL', 'NSE:ADANITRANS', 'NSE:ABCAPITAL', 'NSE:ABFRL', 'NSE:ADVENZYMES', 'NSE:AEGISCHEM', 'NSE:AFFLE', 'NSE:AJANTPHARM', 'NSE:AKZOINDIA', 'NSE:ALEMBICLTD', 'NSE:APLLTD', 'NSE:ALKEM', 'NSE:ALKYLAMINE', 'NSE:ALOKINDS', 'NSE:AMARAJABAT', 'NSE:AMBER', 'NSE:AMBUJACEM', 'NSE:ANGELBRKG', 'NSE:APOLLOHOSP', 'NSE:APOLLOTYRE', 'NSE:ASAHIINDIA', 'NSE:ASHOKLEY', 'NSE:ASHOKA', 'NSE:ASIANPAINT', 'NSE:ASTERDM', 'NSE:ASTRAZEN', 'NSE:ASTRAL', 'NSE:ATUL', 'NSE:AUROPHARMA', 'NSE:AVANTIFEED', 'NSE:DMART', 'NSE:AXISBANK', 'NSE:BASF', 'NSE:BEML', 'NSE:BSE', 'NSE:BAJAJ-AUTO', 'NSE:BAJAJCON', 'NSE:BAJAJELEC', 'NSE:BAJFINANCE', 'NSE:BAJAJFINSV', 'NSE:BAJAJHLDNG', 'NSE:BALAMINES', 'NSE:BALKRISIND', 'NSE:BALMLAWRIE', 'NSE:BALRAMCHIN', 'NSE:BANDHANBNK', 'NSE:BANKBARODA', 'NSE:BANKINDIA', 'NSE:MAHABANK', 'NSE:BATAINDIA', 'NSE:BAYERCROP', 'NSE:BERGEPAINT', 'NSE:BDL', 'NSE:BEL', 'NSE:BHARATFORG', 'NSE:BHEL', 'NSE:BPCL', 'NSE:BHARATRAS', 'NSE:BHARTIARTL', 'NSE:BIOCON', 'NSE:BIRLACORPN', 'NSE:BSOFT', 'NSE:BLISSGVS', 'NSE:BLUEDART', 'NSE:BLUESTARCO', 'NSE:BBTC', 'NSE:BOSCHLTD', 'NSE:BRIGADE', 'NSE:BRITANNIA', 'NSE:BURGERKING', 'NSE:CCL', 'NSE:CESC', 'NSE:CRISIL', 'NSE:CSBBANK', 'NSE:CADILAHC', 'NSE:CANFINHOME', 'NSE:CANBK', 'NSE:CAPLIPOINT', 'NSE:CGCL', 'NSE:CARBORUNIV', 'NSE:CASTROLIND', 'NSE:CEATLTD', 'NSE:CENTRALBK', 'NSE:CDSL', 'NSE:CENTURYPLY', 'NSE:CENTURYTEX', 'NSE:CERA', 'NSE:CHALET', 'NSE:CHAMBLFERT', 'NSE:CHOLAHLDNG', 'NSE:CHOLAFIN', 'NSE:CIPLA', 'NSE:CUB', 'NSE:COALINDIA', 'NSE:COCHINSHIP', 'NSE:COFORGE', 'NSE:COLPAL', 'NSE:CAMS', 'NSE:CONCOR', 'NSE:COROMANDEL', 'NSE:CREDITACC', 'NSE:CROMPTON', 'NSE:CUMMINSIND', 'NSE:CYIENT', 'NSE:DCBBANK', 'NSE:DCMSHRIRAM', 'NSE:DLF', 'NSE:DABUR', 'NSE:DALBHARAT', 'NSE:DEEPAKNTR', 'NSE:DELTACORP', 'NSE:DHANI', 'NSE:DHANUKA', 'NSE:DBL', 'NSE:DISHTV', 'NSE:DCAL', 'NSE:DIVISLAB', 'NSE:DIXON', 'NSE:LALPATHLAB', 'NSE:DRREDDY', 'NSE:EIDPARRY', 'NSE:EIHOTEL', 'NSE:EPL', 'NSE:EDELWEISS', 'NSE:EICHERMOT', 'NSE:ELGIEQUIP', 'NSE:EMAMILTD', 'NSE:ENDURANCE', 'NSE:ENGINERSIN', 'NSE:EQUITAS', 'NSE:ERIS', 'NSE:ESCORTS', 'NSE:EXIDEIND', 'NSE:FDC', 'NSE:FEDERALBNK', 'NSE:FINEORG', 'NSE:FINCABLES', 'NSE:FINPIPE', 'NSE:FSL', 'NSE:FORTIS', 'NSE:FCONSUMER', 'NSE:FRETAIL', 'NSE:GAIL', 'NSE:GEPIL', 'NSE:GMMPFAUDLR', 'NSE:GMRINFRA', 'NSE:GALAXYSURF', 'NSE:GRSE', 'NSE:GARFIBRES', 'NSE:GICRE', 'NSE:GILLETTE', 'NSE:GLAXO', 'NSE:GLENMARK', 'NSE:GODFRYPHLP', 'NSE:GODREJAGRO', 'NSE:GODREJCP', 'NSE:GODREJIND', 'NSE:GODREJPROP', 'NSE:GRANULES', 'NSE:GRAPHITE', 'NSE:GRASIM', 'NSE:GESHIP', 'NSE:GREAVESCOT', 'NSE:GRINDWELL', 'NSE:GUJALKALI', 'NSE:GAEL', 'NSE:FLUOROCHEM', 'NSE:GUJGASLTD', 'NSE:GNFC', 'NSE:GPPL', 'NSE:GSFC', 'NSE:GSPL', 'NSE:GULFOILLUB', 'NSE:HEG', 'NSE:HCLTECH', 'NSE:HDFCAMC', 'NSE:HDFCBANK', 'NSE:HDFCLIFE', 'NSE:HFCL', 'NSE:HAPPSTMNDS', 'NSE:HATSUN', 'NSE:HAVELLS', 'NSE:HEIDELBERG', 'NSE:HEMIPROP', 'NSE:HEROMOTOCO', 'NSE:HSCL', 'NSE:HINDALCO', 'NSE:HAL', 'NSE:HINDCOPPER', 'NSE:HINDPETRO', 'NSE:HINDUNILVR', 'NSE:HINDZINC', 'NSE:HONAUT', 'NSE:HUDCO', 'NSE:HDFC', 'NSE:HUHTAMAKI', 'NSE:ICICIBANK', 'NSE:ICICIGI', 'NSE:ICICIPRULI', 'NSE:ISEC', 'NSE:IDBI', 'NSE:IDFCFIRSTB', 'NSE:IDFC', 'NSE:IFBIND', 'NSE:IIFL', 'NSE:IIFLWAM', 'NSE:IOLCP', 'NSE:IRB', 'NSE:IRCON', 'NSE:ITC', 'NSE:ITI', 'NSE:INDIACEM', 'NSE:IBULHSGFIN', 'NSE:IBREALEST', 'NSE:INDIAMART', 'NSE:INDIANB', 'NSE:IEX', 'NSE:INDHOTEL', 'NSE:IOC', 'NSE:IOB', 'NSE:IRCTC', 'NSE:ICIL', 'NSE:INDOCO', 'NSE:IGL', 'NSE:INDUSTOWER', 'NSE:INDUSINDBK', 'NSE:INFIBEAM', 'NSE:NAUKRI', 'NSE:INFY', 'NSE:INGERRAND', 'NSE:INOXLEISUR', 'NSE:INTELLECT', 'NSE:INDIGO', 'NSE:IPCALAB', 'NSE:JBCHEPHARM', 'NSE:JKCEMENT', 'NSE:JKLAKSHMI', 'NSE:JKPAPER', 'NSE:JKTYRE', 'NSE:JMFINANCIL', 'NSE:JSWENERGY', 'NSE:JSWSTEEL', 'NSE:JTEKTINDIA', 'NSE:JAMNAAUTO', 'NSE:JINDALSAW', 'NSE:JSLHISAR', 'NSE:JSL', 'NSE:JINDALSTEL', 'NSE:JCHAC', 'NSE:JUBLFOOD', 'NSE:JUSTDIAL', 'NSE:JYOTHYLAB', 'NSE:KPRMILL', 'NSE:KEI', 'NSE:KNRCON', 'NSE:KPITTECH', 'NSE:KRBL', 'NSE:KSB', 'NSE:KAJARIACER', 'NSE:KALPATPOWR', 'NSE:KANSAINER', 'NSE:KARURVYSYA', 'NSE:KSCL', 'NSE:KEC', 'NSE:KOTAKBANK', 'NSE:L&TFH', 'NSE:LTTS', 'NSE:LICHSGFIN', 'NSE:LAOPALA', 'NSE:LAXMIMACH', 'NSE:LTI', 'NSE:LT', 'NSE:LAURUSLABS', 'NSE:LEMONTREE', 'NSE:LINDEINDIA', 'NSE:LUPIN', 'NSE:LUXIND', 'NSE:MASFIN', 'NSE:MMTC', 'NSE:MOIL', 'NSE:MRF', 'NSE:MGL', 'NSE:MAHSCOOTER', 'NSE:MAHSEAMLES', 'NSE:M&MFIN', 'NSE:M&M', 'NSE:MAHINDCIE', 'NSE:MHRIL', 'NSE:MAHLOG', 'NSE:MANAPPURAM', 'NSE:MRPL', 'NSE:MARICO', 'NSE:MARUTI', 'NSE:MFSL', 'NSE:MAXHEALTH', 'NSE:MAZDOCK', 'NSE:METROPOLIS', 'NSE:MINDTREE', 'NSE:MINDACORP', 'NSE:MINDAIND', 'NSE:MIDHANI', 'NSE:MOTHERSUMI', 'NSE:MOTILALOFS', 'NSE:MPHASIS', 'NSE:MCX', 'NSE:MUTHOOTFIN', 'NSE:NATCOPHARM', 'NSE:NBCC', 'NSE:NCC', 'NSE:NESCO', 'NSE:NHPC', 'NSE:NLCINDIA', 'NSE:NMDC', 'NSE:NOCIL', 'NSE:NTPC', 'NSE:NH', 'NSE:NATIONALUM', 'NSE:NFL', 'NSE:NAVINFLUOR', 'NSE:NESTLEIND', 'NSE:NETWORK18', 'NSE:NILKAMAL', 'NSE:NAM-INDIA', 'NSE:OBEROIRLTY', 'NSE:ONGC', 'NSE:OIL', 'NSE:OFSS', 'NSE:ORIENTELEC', 'NSE:ORIENTREF', 'NSE:PIIND', 'NSE:PNBHOUSING', 'NSE:PNCINFRA', 'NSE:PVR', 'NSE:PAGEIND', 'NSE:PERSISTENT', 'NSE:PETRONET', 'NSE:PFIZER', 'NSE:PHILIPCARB', 'NSE:PHOENIXLTD', 'NSE:PIDILITIND', 'NSE:PEL', 'NSE:POLYMED', 'NSE:POLYCAB', 'NSE:POLYPLEX', 'NSE:PFC', 'NSE:POWERGRID', 'NSE:PRESTIGE', 'NSE:PRINCEPIPE', 'NSE:PRSMJOHNSN', 'NSE:PGHL', 'NSE:PGHH', 'NSE:PNB', 'NSE:QUESS', 'NSE:RBLBANK', 'NSE:RECLTD', 'NSE:RITES', 'NSE:RADICO', 'NSE:RVNL', 'NSE:RAIN', 'NSE:RAJESHEXPO', 'NSE:RALLIS', 'NSE:RCF', 'NSE:RATNAMANI', 'NSE:RAYMOND', 'NSE:REDINGTON', 'NSE:RELAXO', 'NSE:RELIANCE', 'NSE:RESPONIND', 'NSE:ROSSARI', 'NSE:ROUTE', 'NSE:SBICARD', 'NSE:SBILIFE', 'NSE:SIS', 'NSE:SJVN', 'NSE:SKFINDIA', 'NSE:SRF', 'NSE:SANOFI', 'NSE:SCHAEFFLER', 'NSE:SCHNEIDER', 'NSE:SEQUENT', 'NSE:SHARDACROP', 'NSE:SFL', 'NSE:SHILPAMED', 'NSE:SCI', 'NSE:SHOPERSTOP', 'NSE:SHREECEM', 'NSE:SHRIRAMCIT', 'NSE:SRTRANSFIN', 'NSE:SIEMENS', 'NSE:SOBHA', 'NSE:SOLARINDS', 'NSE:SOLARA', 'NSE:SONATSOFTW', 'NSE:SPANDANA', 'NSE:SPICEJET', 'NSE:STARCEMENT', 'NSE:SBIN', 'NSE:SAIL', 'NSE:SWSOLAR', 'NSE:STLTECH', 'NSE:STAR', 'NSE:SUDARSCHEM', 'NSE:SUMICHEM', 'NSE:SPARC', 'NSE:SUNPHARMA', 'NSE:SUNTV', 'NSE:SUNCLAYLTD', 'NSE:SUNDARMFIN', 'NSE:SUNDRMFAST', 'NSE:SUNTECK', 'NSE:SUPRAJIT', 'NSE:SUPREMEIND', 'NSE:SUPPETRO', 'NSE:SUVENPHAR', 'NSE:SUZLON', 'NSE:SWANENERGY', 'NSE:SYMPHONY', 'NSE:SYNGENE', 'NSE:TCIEXP', 'NSE:TCNSBRANDS', 'NSE:TTKPRESTIG', 'NSE:TV18BRDCST', 'NSE:TVSMOTOR', 'NSE:TANLA', 'NSE:TASTYBITE', 'NSE:TATACHEM', 'NSE:TATACOFFEE', 'NSE:TATACOMM', 'NSE:TCS', 'NSE:TATACONSUM', 'NSE:TATAELXSI', 'NSE:TATAINVEST', 'NSE:TATAMTRDVR', 'NSE:TATAMOTORS', 'NSE:TATAPOWER', 'NSE:TATASTEEL', 'NSE:TEAMLEASE', 'NSE:TECHM', 'NSE:NIACL', 'NSE:RAMCOCEM', 'NSE:THERMAX', 'NSE:THYROCARE', 'NSE:TIMKEN', 'NSE:TITAN', 'NSE:TORNTPHARM', 'NSE:TORNTPOWER', 'NSE:TRENT', 'NSE:TRIDENT', 'NSE:TRITURBINE', 'NSE:TIINDIA', 'NSE:UCOBANK', 'NSE:UFLEX', 'NSE:UPL', 'NSE:UTIAMC', 'NSE:UJJIVAN', 'NSE:UJJIVANSFB', 'NSE:ULTRACEMCO', 'NSE:UNIONBANK', 'NSE:UBL', 'NSE:MCDOWELL-N', 'NSE:VGUARD', 'NSE:VMART', 'NSE:VIPIND', 'NSE:VSTIND', 'NSE:VAIBHAVGBL', 'NSE:VAKRANGEE', 'NSE:VALIANTORG', 'NSE:VTL', 'NSE:VARROC', 'NSE:VBL', 'NSE:VEDL', 'NSE:VENKEYS', 'NSE:VINATIORGA', 'NSE:IDEA', 'NSE:VOLTAS', 'NSE:WABCOINDIA', 'NSE:WELCORP', 'NSE:WELSPUNIND', 'NSE:WESTLIFE', 'NSE:WHIRLPOOL', 'NSE:WIPRO', 'NSE:WOCKPHARMA', 'NSE:YESBANK', 'NSE:ZEEL', 'NSE:ZENSARTECH', 'NSE:ZYDUSWELL', 'NSE:ECLERX']

data = kite.ltp(watchlist)

df = pd.DataFrame(data)

pdb.set_trace()




# ltp = kite.ltp(['NSE:' + name])['NSE:' + name]['last_price']









