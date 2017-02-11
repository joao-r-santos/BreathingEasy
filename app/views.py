from flask import render_template, request
from app import app

#import pandas as pd

from counties import ListCounties
from rates import getRates
from impact import getImpact
from ranks import getRanks
from utils import getEthName

# Libraries for SQL
#from sqlalchemy import create_engine
#from sqlalchemy_utils import database_exists, create_database
#import psycopg2

#user = 'joao'
#psswrd = 'insight17a'
#host = 'localhost'
#dbname = 'birth_db'
#db = create_engine('postgresql://%s:%s@%s/%s'%(user,psswrd,host,dbname))
#con = None
#con = psycopg2.connect(database=dbname, user=user, password=psswrd, host=host)


#@app.route('/')
#@app.route('/index')
#@app.route('/index.html')
#def index():
#	return render_template('index.html')


@app.route('/about')
@app.route('/about.html')
def about():
	return render_template('about.html')

@app.route('/contact')
@app.route('/contact.html')
def contact():
	return render_template('contact.html')


#@app.route('/realtime')
#@app.route('/realtime.html')
#def realtime():
#	return render_template("realtime.html")


@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/input')
@app.route('/input.html')
def breath_input():
	counties= ListCounties()
	return render_template("input.html", counties=counties)



@app.route('/output')
@app.route('/output.html')
def breath_output():
	counties= ListCounties()

	county_fips= request.args.get('county')
	for c in counties:
		if c['FIPS']==county_fips:
			county_name= c['County']
	age= request.args.get('age')
	gender= request.args.get('gender')
	ethnicity= request.args.get('ethnicity')
	#print county_fips, age, gender, ethnicity

	eth_name= getEthName(ethnicity)

	if (county_fips==None) or (age==None) or (gender==None) or (ethnicity==None):
		return render_template("wrong.html", counties=counties)
	else:
		try:
			rates= getRates(fips=county_fips, age=age, gender=gender, ethnicity=ethnicity)
			ranks= getRanks(fips=county_fips, age=age, gender=gender, ethnicity=ethnicity)
			impact= getImpact(fips=county_fips, age=age, gender=gender, ethnicity=ethnicity)

			if rates != None:
				return render_template("output.html", counties=counties, rates=rates, ranks=ranks, impact=impact, eth_name=eth_name)
			else:
				return render_template("missing.html", counties=counties, county_name=county_name, age=age, gender=gender, eth_name=eth_name)
		except:
				return render_template("missing.html", counties=counties, county_name=county_name, age=age, gender=gender, eth_name=eth_name)

