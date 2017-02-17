from numpy import array, str
import pandas as pd

def getImpact(fips='06037', age='0-4', gender='female', ethnicity='hispanic'):
	#print fips, age, gender, ethnicity
	try:
		rates_df = pd.read_csv('app/static/rates_2014.csv', dtype={'FIPS':str} )
		impact_df = pd.read_csv('app/static/impactscore_2014.csv')

		inds= (rates_df['FIPS']==fips) & \
					(rates_df['Age']==age) & \
					(rates_df['Gender']==gender) & \
					(rates_df['Ethnicity']==ethnicity)

		temp_df= impact_df[inds]

		row= temp_df.to_dict(orient='records')
		row= row[0] # select only the dict

	except:
		print 'Ooops. Impact not found.'
		row= None

	return row


if __name__ == '__main__':
	impact_row= getImpact()
	print 'The impact score for the different factors are:'
	print 'median AQI: %f' % impact_row['AQI Median']
	print 'ozone AQI : %f' % impact_row['O3 AQI']
	print 'PM2.5 AQI : %f' % impact_row['PM2.5 AQI']
	print 'Traffic pollution: %f' % impact_row['Traffic pollution']
	print 'Area burned from wildfires: %f' % impact_row['Area burned']
