
def getEthName(ethnicity='hispanic'):
	#print ethnicity
		
	if ethnicity=='white':
		eth_name='White/Caucasian'
	elif ethnicity=='african':
		eth_name='African-American'
	elif ethnicity=='asian':
		eth_name='Asian-American/Pacific Islander'
	elif ethnicity=='hispanic':
		eth_name='Hispanic'
	elif ethnicity=='other':
		eth_name='Other'
	else:
		eth_name=None

	return eth_name

