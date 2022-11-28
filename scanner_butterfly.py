from pprint import pprint
import pdb 
import pandas as pd
import time
import zrd_login
import datetime
import support_file01 as sf
import talib
import winsound
import xlwings as xw

def init():
    global name, Status,final_result, kite, breakin_time, breakout_time, wb, sht,Qty,name1,Stoploss,Target,tradeno
    kite = zrd_login.kite
    name = 'NIFTY BANK'
    name1 = 'BANKNIFTY'
    Status = {'Date': None, 'Entry_time': None, 'CE_ATM': None, 'CE_ITM_01': None, 'CE_ITM_02': None,  'CE_ITM_03': None, 'CE_ITM_04': None, 'CE_ITM_05': None, 'CE_OTM': None, 'CE_OTM_01': None, 'CE_OTM_02': None, 'CE_OTM_03': None, 'CE_OTM_04': None, 'CE_OTM_05': None, 'ltp_CE_ATM_00': None, 'ltp_CE_ITM_01': None, 'ltp_CE_ITM_02': None, 'ltp_CE_ITM_03': None, 'ltp_CE_ITM_04': None, 'ltp_CE_ITM_05': None, 'ltp_CE_OTM_01': None, 'ltp_CE_OTM_02': None, 'ltp_CE_OTM_03': None, 'ltp_CE_OTM_04': None, 'ltp_CE_OTM_05': None, 'BID_CE_ATM_00': None, 'BID_CE_ITM_01': None, 'BID_CE_ITM_02': None, 'BID_CE_ITM_03': None, 'BID_CE_ITM_04': None, 'BID_CE_ITM_05': None, 'BID_CE_OTM_01': None, 'BID_CE_OTM_02': None, 'BID_CE_OTM_03': None, 'BID_CE_OTM_04': None, 'BID_CE_OTM_05': None, 'ASK_CE_ATM_00': None, 'ASK_CE_ITM_01': None, 'ASK_CE_ITM_02': None, 'ASK_CE_ITM_03': None, 'ASK_CE_ITM_04': None, 'ASK_CE_ITM_05': None, 'ASK_CE_OTM_01': None, 'ASK_CE_OTM_02': None, 'ASK_CE_OTM_03': None, 'ASK_CE_OTM_04': None, 'ASK_CE_OTM_05': None}
    final_result = {}
    tradeno = 0
    breakin_time = datetime.time(9,25)
    breakout_time = datetime.time(12,10)
    wb = xw.Book('scanner_butterfly.xlsx')
    sht = wb.sheets['Sheet1']
    
init()

# while True:
    # try:
ctime1 = datetime.datetime.now().time()
ctime = datetime.datetime.now()
ltp = sf.LTP(name)
step_value = 100
multiplier = 0
expiry = '21909'
atm_strike = round(ltp/step_value)* step_value + multiplier*step_value
final_result[tradeno] = Status.copy()
sht.range('A1').value = pd.DataFrame(final_result)
Status['Date'] = str(ctime.date())
Status['Entry_time'] = str(ctime.time())
CE_ATM = (name1 + expiry + str(atm_strike) + 'CE')
CE_ITM_01 = (name1 + expiry + str(atm_strike - 100) + 'CE')
CE_ITM_02 = (name1 + expiry + str(atm_strike - 200) + 'CE')
CE_ITM_03 = (name1 + expiry + str(atm_strike - 300) + 'CE')
CE_ITM_04 = (name1 + expiry + str(atm_strike - 400) + 'CE')
CE_ITM_05 = (name1 + expiry + str(atm_strike - 500) + 'CE')
CE_OTM_01 = (name1 + expiry + str(atm_strike + 100) + 'CE')
CE_OTM_02 = (name1 + expiry + str(atm_strike + 200) + 'CE')
CE_OTM_03 = (name1 + expiry + str(atm_strike + 300) + 'CE')
CE_OTM_04 =(name1 + expiry + str(atm_strike + 400) + 'CE')
CE_OTM_05= (name1 + expiry + str(atm_strike + 500) + 'CE')

BID_CE_ATM_00 = sf.BID_NFO(CE_ATM)
BID_CE_ITM_01 = sf.BID_NFO(CE_ITM_01)
BID_CE_ITM_02 = sf.BID_NFO(CE_ITM_02)
BID_CE_ITM_03 = sf.BID_NFO(CE_ITM_03)
BID_CE_ITM_04 = sf.BID_NFO(CE_ITM_04)
BID_CE_ITM_05 = sf.BID_NFO(CE_ITM_05)
BID_CE_OTM_01 = sf.BID_NFO(CE_OTM_01)
BID_CE_OTM_02 = sf.BID_NFO(CE_OTM_02)
BID_CE_OTM_03 = sf.BID_NFO(CE_OTM_03)
BID_CE_OTM_04 = sf.BID_NFO(CE_OTM_04)
BID_CE_OTM_05 = sf.BID_NFO(CE_OTM_05)
ASK_CE_ATM_00 = sf.ASK_NFO(CE_ATM)
ASK_CE_ITM_01 = sf.ASK_NFO(CE_ITM_01)
ASK_CE_ITM_02 = sf.ASK_NFO(CE_ITM_02)
ASK_CE_ITM_03 = sf.ASK_NFO(CE_ITM_03)
ASK_CE_ITM_04 = sf.ASK_NFO(CE_ITM_04)
ASK_CE_ITM_05 = sf.ASK_NFO(CE_ITM_05)
ASK_CE_OTM_01 = sf.ASK_NFO(CE_OTM_01)
ASK_CE_OTM_02 = sf.ASK_NFO(CE_OTM_02)
ASK_CE_OTM_03 = sf.ASK_NFO(CE_OTM_03)
ASK_CE_OTM_04 = sf.ASK_NFO(CE_OTM_04)
ASK_CE_OTM_05 = sf.ASK_NFO(CE_OTM_05)
ltp_CE_ATM_00 = sf.LTP_NFO(CE_ATM)
ltp_CE_ITM_01 = sf.LTP_NFO(CE_ITM_01)
ltp_CE_ITM_02 = sf.LTP_NFO(CE_ITM_02)
ltp_CE_ITM_03 = sf.LTP_NFO(CE_ITM_03)
ltp_CE_ITM_04 = sf.LTP_NFO(CE_ITM_04)
ltp_CE_ITM_05 = sf.LTP_NFO(CE_ITM_05)
ltp_CE_OTM_01 = sf.LTP_NFO(CE_OTM_01)
ltp_CE_OTM_02 = sf.LTP_NFO(CE_OTM_02)
ltp_CE_OTM_03 = sf.LTP_NFO(CE_OTM_03)
ltp_CE_OTM_04 = sf.LTP_NFO(CE_OTM_04)
ltp_CE_OTM_05 = sf.LTP_NFO(CE_OTM_05)
Status['ltp_CE_ATM_00'] = ltp_CE_ATM_00 
Status['ltp_CE_ITM_01'] = ltp_CE_ITM_01
Status['ltp_CE_ITM_02'] = ltp_CE_ITM_02
Status['ltp_CE_ITM_03'] = ltp_CE_ITM_03
Status['ltp_CE_ITM_04'] = ltp_CE_ITM_04
Status['ltp_CE_ITM_05'] = ltp_CE_ITM_05
Status['ltp_CE_OTM_01'] = ltp_CE_OTM_01
Status['ltp_CE_OTM_02'] = ltp_CE_OTM_02
Status['ltp_CE_OTM_03'] = ltp_CE_OTM_03
Status['ltp_CE_OTM_04'] = ltp_CE_OTM_04
Status['ltp_CE_OTM_05'] = ltp_CE_OTM_05
Status['BID_CE_ATM_00'] = BID_CE_ATM_00
Status['BID_CE_ITM_01'] = BID_CE_ITM_01
Status['BID_CE_ITM_02'] = BID_CE_ITM_02
Status['BID_CE_ITM_03'] = BID_CE_ITM_03
Status['BID_CE_ITM_04'] = BID_CE_ITM_04
Status['BID_CE_ITM_05'] = BID_CE_ITM_05
Status['BID_CE_OTM_01'] = BID_CE_OTM_01 
Status['BID_CE_OTM_02'] = BID_CE_OTM_02
Status['BID_CE_OTM_03'] = BID_CE_OTM_03
Status['BID_CE_OTM_04'] = BID_CE_OTM_04
Status['BID_CE_OTM_05'] = BID_CE_OTM_05
Status['ASK_CE_ATM_00'] = ASK_CE_ATM_00
Status['ASK_CE_ITM_01'] = ASK_CE_ITM_01
Status['ASK_CE_ITM_02'] = ASK_CE_ITM_02
Status['ASK_CE_ITM_03'] = ASK_CE_ITM_03
Status['ASK_CE_ITM_04'] = ASK_CE_ITM_04
Status['ASK_CE_ITM_05'] = ASK_CE_ITM_05
Status['ASK_CE_OTM_01'] = ASK_CE_OTM_01
Status['ASK_CE_OTM_02'] = ASK_CE_OTM_02
Status['ASK_CE_OTM_03'] = ASK_CE_OTM_03
Status['ASK_CE_OTM_04'] = ASK_CE_OTM_04
Status['ASK_CE_OTM_05'] = ASK_CE_OTM_05
jodi_01 = (2*(BID_CE_ATM_00) - (ASK_CE_ITM_01) - (ASK_CE_OTM_01))
jodi_02 = (2*(BID_CE_ITM_01) - (ASK_CE_ATM_00) - (ASK_CE_ITM_02))
jodi_03 = (2*(BID_CE_ITM_02) - (ASK_CE_ITM_01) - (ASK_CE_ITM_03))
jodi_04 = (2*(BID_CE_ITM_03) - (ASK_CE_ITM_02) - (ASK_CE_ITM_04))
jodi_05 = (2*(BID_CE_ITM_04) - (ASK_CE_ITM_03) - (ASK_CE_ITM_05))
jodi_06 = (2*(BID_CE_OTM_01) - (ASK_CE_ATM_00) - (ASK_CE_OTM_02))
jodi_07 = (2*(BID_CE_OTM_02) - (ASK_CE_OTM_01) - (ASK_CE_OTM_03))
jodi_08 = (2*(BID_CE_OTM_03) - (ASK_CE_OTM_02) - (ASK_CE_OTM_04))
jodi_09 = (2*(BID_CE_OTM_04) - (ASK_CE_OTM_03) - (ASK_CE_OTM_05))
Status['jodi_01'] = jodi_01
Status['jodi_02'] = jodi_02
Status['jodi_03'] = jodi_03
Status['jodi_04'] = jodi_04
Status['jodi_05'] = jodi_05
Status['jodi_06'] = jodi_06
Status['jodi_07'] = jodi_07
Status['jodi_08'] = jodi_08
Status['jodi_09'] = jodi_09


# except Exception as e:
# print(e)
# cont       