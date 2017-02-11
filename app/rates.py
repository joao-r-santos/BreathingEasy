from numpy import array, str
import pandas as pd
#from utils import getEthName

def getRates(fips='06037', age='0-4', gender='female', ethnicity='hispanic'):
	#print fips, age, gender, ethnicity
	try:
		rates_df = pd.read_csv('app/static/rates_2014.csv', dtype={'FIPS':str} )

		row= rates_df[(rates_df['FIPS']==fips) & \
									(rates_df['Age']==age) & \
									(rates_df['Gender']==gender) & \
									(rates_df['Ethnicity']==ethnicity)]

		row= row.to_dict(orient='records')
		row= row[0] # select only the dict

		#row['Ethnicity']= getEthName(row['Ethnicity'])


	except:
		print 'Ooops. Rate not found.'
		row= None

	return row


if __name__ == '__main__':
	rates_row= getRates()
	print 'The predicted rate of ED visits in %s county is %.2f, while the real rate is %.2f' % (rates_row['County'], rates_row['Rate real'], rates_row['Rate predict'])
