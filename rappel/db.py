import sqlite3
import datetime

class db:
	def __init__(self, filename):	
		self.conn = sqlite3.connect(filename)
		try:
			self.conn.cursor().execute('''create table results
				(name text,
			 	date text,
			 	mot text,
			 	valeur int,
			 	essais int,
			 	found int,
			 	temps int
				)''')
		except sqlite3.OperationalError:
			pass

	def __del__(self):
		self.conn.cursor().close()

	def save(self, name, results):
		date_of_play = datetime.datetime.now()

		for t in results:
			response = [name, str(date_of_play), t.word, t.value, t.tries, t.found, t.time]
			self.conn.cursor().execute('insert into results values (?,?,?,?,?,?,?)', response)

		self.conn.commit()


	def read_all(self):
		return self.conn.execute('select * from results').fetchall()

	def read_field(self, field):
		query ='select ' + field + ' from results'
		return self.conn.execute(query).fetchall()

