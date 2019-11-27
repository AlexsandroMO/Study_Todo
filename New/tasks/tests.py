from django.test import TestCase

# Create your tests here.


#pip install django-crispy-forms

#Zerar senha do admin
#python manage.py shell
#from django.contrib.auth.models import User
#User.objects.filter(is_superuser=True)

#usr = User.objects.get(username='nome-do-administrador')
#usr.set_password('nova-senha')
#usr.save()


#=======================
'''
!pip install pandas
!pip install pandasql

import sqlite3
import pandas as pd


def read_sql():
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db
	
	
xx = read_sql()
xx

def read_sql2():
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT * FROM auth_user;
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db

yy = read_sql2()
yy
'''