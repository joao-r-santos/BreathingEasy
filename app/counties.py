from pickle import load
from numpy import array

def ListCounties():
  fin = open('app/static/counties.pkl','rb')
  try:
    county_names = load(fin)
  except:
    print 'Ooops. County Names not found.'
    county_names= array([],dtype=np.str)
  return county_names

if __name__ == '__main__':
  county_names= ListCounties()
  for i in xrange(len(county_names)):
    print '%2d) %s' % (i+1, county_names[i])
