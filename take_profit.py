from pprint import pprint
import pdb 
import pandas as pd
import time
import zrd_login
kite = zrd_login.kite
import datetime
import support_file as get



# specific for any Scrip only
traded = []
name = input("Enter Stock Name ")
profit = int(input(f"Enter Profit You want to do in {name} = "))
lp = float(input(f"Enter Sell value for  {name} = "))
qty = int(input(f"Enter Quantity for  {name} = "))
sv = lp*qty
bvp = sv-profit  # svp = sell value at profit
tpl = round(bvp/qty,1)

order_id_1 = kite.place_order(variety = kite.VARIETY_REGULAR , exchange = kite.EXCHANGE_NSE , tradingsymbol = name , transaction_type = kite.TRANSACTION_TYPE_SELL , quantity = qty , product = kite.PRODUCT_MIS , order_type = kite.ORDER_TYPE_LIMIT , price=lp, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
print(f"order id is {order_id_1} placed at {lp} now wait for buy order")
print(f"First Order placement time is {datetime.datetime.now().time()}")

while True:


	oh = kite.order_history(order_id=order_id_1)
	lenn = len(oh) 

	for x in range(lenn):


		if (oh[x]['status'] =='COMPLETE') and (oh[x]['filled_quantity']==qty) and (name not in traded):
			


			order_id_tp = kite.place_order(variety = kite.VARIETY_REGULAR , exchange = kite.EXCHANGE_NSE , tradingsymbol = name , transaction_type = kite.TRANSACTION_TYPE_BUY , quantity = qty , product = kite.PRODUCT_MIS , order_type = kite.ORDER_TYPE_LIMIT , price = tpl, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
			traded.append(name)
			print(order_id_tp)
			print(f"TP Order placement time is {datetime.datetime.now().time()}")
			if oh[x]['status'] =='COMPLETE' :
				break


	if name in traded:
		break
		print('Done ! ')

# Code is final not ameendement required !!!!!
				

			
	
