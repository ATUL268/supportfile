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
loss = int(input(f"Enter loss You want to do in {name} = "))
lp = float(input(f"Enter Sell value for  {name} = "))
qty = int(input(f"Enter Quantity for  {name} = "))
sv = lp*qty # Sell value = lp(limit price * quantity)
bvl = sv+loss    # bvl = buy value at loss
bvp = sv-profit  # svp = sell value at profit
tpl = round(bvp/qty,1)
sll = round(bvl/qty,1) # limit price at which profit book

order_id_1 = kite.place_order(variety = kite.VARIETY_REGULAR , exchange = kite.EXCHANGE_NSE , tradingsymbol = name , transaction_type = kite.TRANSACTION_TYPE_SELL , quantity = qty , product = kite.PRODUCT_MIS , order_type = kite.ORDER_TYPE_LIMIT , price=lp, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
print(f"order id is {order_id_1} placed at {lp} now wait for buy order")
print(f"First Order placement time is {datetime.datetime.now().time()}")

while True:


	oh = kite.order_history(order_id=order_id_1)
	lenn = len(oh) 

	for x in range(lenn):


		if (oh[x]['status'] =='COMPLETE') and (oh[x]['filled_quantity']==qty) and (name not in traded):
			


			order_id_tp = kite.place_order(variety = kite.VARIETY_REGULAR , exchange = kite.EXCHANGE_NSE , tradingsymbol = name , transaction_type = kite.TRANSACTION_TYPE_BUY , quantity = qty , product = kite.PRODUCT_MIS , order_type = kite.ORDER_TYPE_LIMIT , price = tpl, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
			order_id_sl = kite.place_order(variety = kite.VARIETY_REGULAR , exchange = kite.EXCHANGE_NSE , tradingsymbol = name , transaction_type = kite.TRANSACTION_TYPE_BUY , quantity = qty , product = kite.PRODUCT_MIS , order_type = kite.ORDER_TYPE_SLM , price = None, validity=None, disclosed_quantity=None, trigger_price= sll, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
			traded.append(name)
			tp = kite.order_history(order_id=order_id_tp)
			sl = kite.order_history(order_id=order_id_sl)
			print(order_id_tp)
			print(order_id_sl)
			print(f"SL and TP Order placement time is {datetime.datetime.now().time()}")

			while True:
				tp = kite.order_history(order_id=order_id_tp)
				sl = kite.order_history(order_id=order_id_sl

					# Start from here




			if (tp[x]['status'] =='COMPLETE') and (sl[x]['status'] =='OPEN'):
				kite.cancel_order(variety=kite.VARIETY_REGULAR, order_id=order_id_sl,parent_order_id=None)


			elif (tp[x]['status'] =='OPEN') and (sl[x]['status'] =='COMPLETE'):
				kite.cancel_order(variety=kite.VARIETY_REGULAR, order_id=order_id_tp,parent_order_id=None)


			if (tp[x]['status'] =='COMPLETE') or (sl[x]['status'] =='COMPLETE'):
				break
	break
print(f"Order is complete you can check Now {tpl} and {sll}" )
print(f"Order Exit time is {datetime.datetime.now().time()}")