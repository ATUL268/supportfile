from pprint import pprint
import pdb 
import pandas as pd
import time
import zrd_login
kite = zrd_login.kite
import datetime
import support_file as get
import winsound





# _________________________________________________________________________________________________________________

#  Code is Final !! Not yet tried live......27/05/21  12 :51 Complete !!!! if required any amendment please do....
# _________________________________________________________________________________________________________________




traded = []
name ='NIFTY 50'


profit = 1100
lp = float(input(f"Enter Limit Price for Call Option   {name} = "))
qty = 1800
bv = lp*qty
svp = bv+profit  # svp = sell value at profit
tpl = round(svp/qty,1) # limit price at which profit book
ltp= kite.ltp(['NSE:' + name])['NSE:' + name]['last_price']
sv = 50
otm_strike = round(ltp/sv)*sv
name = 'NIFTY' + '21MAY'+ str(otm_strike)+'CE'
ltp = get.LTP_NFO(name)





order_id_1 = kite.place_order(variety = kite.VARIETY_REGULAR , exchange = kite.EXCHANGE_NFO , tradingsymbol = name , transaction_type = kite.TRANSACTION_TYPE_BUY , quantity = qty , product = kite.PRODUCT_NRML , order_type = kite.ORDER_TYPE_LIMIT , price=lp, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
print(f"order id is {order_id_1} placed at {lp} now wait for buy order")
print(f"First Order placement time is {datetime.datetime.now().time()}")

while True:


	oh = kite.order_history(order_id=order_id_1)
	lenn = len(oh) 

	for x in range(lenn):


		if (oh[x]['status'] =='COMPLETE') and (oh[x]['filled_quantity']==qty) and (name not in traded):
			


			order_id_tp = kite.place_order(variety = kite.VARIETY_REGULAR , exchange = kite.EXCHANGE_NFO , tradingsymbol = name , transaction_type = kite.TRANSACTION_TYPE_SELL , quantity = qty , product = kite.PRODUCT_NRML , order_type = kite.ORDER_TYPE_LIMIT , price = tpl, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
			traded.append(name)
			print(order_id_tp)
			print(f"TP Order placement time is {datetime.datetime.now().time()}")
			if oh[x]['status'] =='COMPLETE' :
				break


	if name in traded:
		break
		print('Done ! ')
# _________________________________________________________________________________________________________________

# Code is Final !! Not yet tried live......27/05/21  12 :51 Complete !!!! if required any amendment please do....

# _________________________________________________________________________________________________________________			
	





