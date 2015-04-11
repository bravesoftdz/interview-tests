# import this 

import psycopg2

from sql_dml_postgresql import Postgresql


def init_db():
	db = Postgresql()
	db.initialize()

def execute_sql():
	db = Postgresql()

	sql = "select name, email from users limit 100"

	records = db.run_select_sql(sql)
	print(records)


def run():
	#init_db()
	execute_sql()


run() # run project





