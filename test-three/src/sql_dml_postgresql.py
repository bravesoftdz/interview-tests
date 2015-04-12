import psycopg2
from contextlib import closing

class Postgresql:

	def run_select_sql(self, sql):
		with closing(self.__factory_conn()) as conn:
			with closing(conn.cursor()) as cur:	
				cur.execute(sql)
				return cur.fetchall() 			


	def initialize(self):
		with closing(self.__factory_conn()) as conn:
			with closing(conn.cursor()) as cur:	
				
				try:
					self.__create_sequence(cur)
					self.__create_table(cur)
					self.__delete_data(cur)
					self.__feet_data_table(cur)
					self.__create_index_email(cur)

					conn.commit()
				except DatabaseError as e:
					if conn:
						conn.rollback()
						print("Yeap! I could not init DB - {0}".format(e.strerror))


	def __create_sequence(self, cur):
		cur.execute("CREATE SEQUENCE users_id_sequence;")	


	def __create_table(self, cur):
		cur.execute('''
			CREATE TABLE IF NOT EXISTS users (
				id integer PRIMARY KEY DEFAULT nextval('users_id_sequence'),
				name varchar(40) NOT NULL, 
				email varchar(40) NOT NULL
			);
			''')


	def __delete_data(self, cur):
		cur.execute('DELETE FROM users;')


	def __feet_data_table(self, cur):
		users = [ ("Fulano"  , "fulano@gmail.com"  ),
				  ("Ciclano" , "ciclano@gmail.com" ),
				  ("Beltrano", "beltrano@gmail.com"),
				  ("Trajano" , "trajano@hotmail.com" ) ]

		cur.executemany('INSERT INTO users(name, email) values(%s, %s);', users)

		# Geometric progression - http://en.wikipedia.org/wiki/Geometric_progression
		# INsere cerca 4194304 de registros
		for _ in range(20): 
			cur.execute('''
				INSERT INTO users(name, email)
				SELECT name,
					   email
				FROM users
				''')	


	def __create_index_email(self, cur):
		cur.execute('''
				CREATE INDEX idx_email ON users USING btree (email varchar_pattern_ops);
				''')
				

	def __factory_conn(self):
		try:
			return psycopg2.connect(database="kangaroo")
		except DatabaseError as e:
			print ("Opss! I could not connect DB - {0}".format(e.strerror))
			
		




