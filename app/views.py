from flask import render_template, request
from app import app

from counties import ListCounties

# Libraries for SQL
#from sqlalchemy import create_engine
#from sqlalchemy_utils import database_exists, create_database
import pandas as pd
#import psycopg2

#user = 'joao'
#psswrd = 'insight17a'
#host = 'localhost'
#dbname = 'birth_db'
#db = create_engine('postgresql://%s:%s@%s/%s'%(user,psswrd,host,dbname))
#con = None
#con = psycopg2.connect(database=dbname, user=user, password=psswrd, host=host)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
#  return render_template('index.html')
  county_names= ListCounties()
  return render_template("input.html", county_names=county_names)


@app.route('/about')
@app.route('/about.html')
def about():
  return render_template('about.html')

@app.route('/contact')
@app.route('/contact.html')
def contact():
  return render_template('contact.html')


@app.route('/realtime')
@app.route('/realtime.html')
def realtime():
  return render_template("realtime.html")


@app.route('/input')
def breath_input():
  county_names= ListCounties()
  return render_template("input.html", county_names=county_names)


@app.route('/output')
def breath_output():
  county_names= ListCounties()
  county= request.args.get('county')
  age= request.args.get('age')
  gender= request.args.get('gender')
  return render_template("output.html", county_names=county_names, county=county, age=age, gender=gender)



