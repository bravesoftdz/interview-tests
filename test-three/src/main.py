import psycopg2, getopt, sys

from sql_dml_postgresql import Postgresql

def init_db():
	db = Postgresql()
	db.initialize()

def execute_sql():
	db = Postgresql()
	sql = "SELECT name, email FROM users WHERE email LIKE '@gmail.com%' GROUP BY name, email"

	records = db.run_select_sql(sql)
	print(records)

def create_index(index):
	db = Postgresql()
	db.create_index(index)	

def run():
	args, _ = getopt.getopt(sys.argv[1:], "irc", ["initdb", "runquery", "createindex="])
	
	for opt, arg in args:       
		if opt in ("-i", "--initdb"):
			print("Starting objects in DB")
			init_db()
			break
		elif opt in ("-r", "--runquery"):
			print("Running query SQL")
			execute_sql()
			break

		elif opt in ("-c", "--createindex"):
			print("Creating index %s" % arg)
			create_index(arg)
			break

	else:	
		print("Hey! You need to say that I have to do.")

run() 





