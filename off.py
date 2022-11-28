import pandas as pd
import pdb

main = []
blank = []

status = {'Feeder_code': None , 'Sold_Unit': None , 'Lenght': None, 'no_of_consumer': None,'LOAD_KW': None }
series_no = 0
record = {}

df = pd.read_csv('cd.csv')

df = df.set_index(df['Feeder Code'])


for index , values in df.iterrows():
	main.append(index)

for feeder_code in main:

	try:		
		op = df.loc[feeder_code]
		total_sold_unit = df.loc[feeder_code]['Unit Sold'].sum()
		no_of_consumer = df.loc[feeder_code]['No of Consumr'].sum()
		LOAD_KW = round(df.loc[feeder_code]['LOAD KW'].sum(),2)
				
	
		if (feeder_code in blank):
			continue
		
		series_no = series_no + 1
		status['Feeder_code'] = feeder_code
		status['Sold_Unit'] = total_sold_unit
			# status['Lenght'] = len(op)
		status['no_of_consumer'] = no_of_consumer
		status['LOAD_KW'] = LOAD_KW
		
		record[series_no] = status
	
		status = {'Feeder_code': None , 'Sold_Unit': None , 'Lenght': None, 'no_of_consumer': None,'LOAD_KW': None }
		blank.append(feeder_code)

	except Exception as e:
		print(e)
		# pdb.set_trace()




	# if status['Feeder_code'] in record:
	# 	continue

pd.DataFrame(record).T.to_csv('test.csv')
		










		# pdb.set_trace()
		





	# print(index, values)



