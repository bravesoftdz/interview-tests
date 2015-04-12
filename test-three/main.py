# import this 


import psycopg2, getopt, sys

from sql_dml_postgresql import Postgresql

def init_db():
	db = Postgresql()
	db.initialize()

def execute_sql():

	db = Postgresql()

	sql = "SELECT email FROM users WHERE email LIKE '@gmail.com%' GROUP BY email"

	records = db.run_select_sql(sql)
	print(records)


def run():
	args, _ = getopt.getopt(sys.argv[1:], "ir", ["initdb", "runquery"])
		
	for o, _ in args:       
		if o in ("-i", "--initdb"):
			print("Starting objects in DB")
			init_db()
			break
		elif o in ("-r", "--runquery"):
			print("Running query SQL")
			execute_sql()
			break
	else:	
		print("Hey! You need to say that I have to do.")

run() 





