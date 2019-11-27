import sqlite3
import pandas as pd


def read_sql2():
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT * FROM auth_user;
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db


def read_sql3():
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT * FROM django_admin_log;
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db