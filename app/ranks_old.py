from numpy import array, str
import pandas as pd

def getRanks(fips='06037', age='0-4', gender='female', ethnicity='hispanic'):
	#print fips, age, gender, ethnicity
	try:
		rates_df = pd.read_csv('app/static/rates_2014.csv', dtype={'FIPS':str} )
		ranks_df = pd.read_csv('app/static/ranks_2014.csv')

		inds= (rates_df['FIPS']==fips) & \
					(rates_df['Age']==age) & \
					(rates_df['Gender']==gender) & \
					(rates_df['Ethnicity']==ethnicity)

		temp_df= ranks_df[inds]

		row= temp_df.to_dict(orient='records')
		row= row[0] # select only the dict

	except:
		print 'Ooops. Ranks not found.'
		row= None

	return row


if __name__ == '__main__':
	ranks_row= getRanks()
	print 'The percentage ranks of the different factors compared to the rest of the California counties are:'
	print '                median AQI : %f' % ranks_row['AQI Median']
	print '                 ozone AQI : %f' % ranks_row['O3 AQI']
	print '                 PM2.5 AQI : %f' % ranks_row['PM2.5 AQI']
	print '          Traffic pollution: %f' % ranks_row['Traffic pollution']
	print 'Area burned from wild fires: %f' % ranks_row['Area burned']
