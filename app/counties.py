#from pickle import load
from numpy import str
import pandas as pd

def ListCounties():
	counties= []
	try:
		counties_df = pd.read_csv('app/static/county_info.csv', dtype={'FIPS':str})
		counties= counties_df.to_dict(orient='records')  # get file in format [{'County': 'Alameda', 'FIPS': '06001'}]
	except:
		print 'Ooops. Counties not found.'
		return None
	return counties

if __name__ == '__main__':
	counties= ListCounties()
	for c in counties:
		print '%s - %s' % (c['FIPS'], c['County'])
