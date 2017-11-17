import glob
import unittest
import os
from collections import namedtuple

from rappel import db

Result = namedtuple('response', 'word value tries found time')

class DBTestCreation(unittest.TestCase):
	
	def setUp(self):
		self.db_file_name = "temp/tu.db"
		# do some house cleaning
		if glob.glob(self.db_file_name):
			os.remove(self.db_file_name)

	def tearDown(self):
		os.remove(self.db_file_name)

	def test_create_db_file(self):
		self.assertEqual(glob.glob(self.db_file_name), [])
		myDb = db.db(self.db_file_name)
		self.assertEqual(glob.glob(self.db_file_name), [self.db_file_name])



class DBTestUsage(unittest.TestCase):

	def setUp(self):
		self.db_file_name = "temp/tu.db"
		# do some house cleaning
		if glob.glob(self.db_file_name):
			os.remove(self.db_file_name)

		r1 = Result("toit", 1, 1, 1, 1)
		r2 = Result("nez", 2, 2, 2, 2)
		r3 = Result("mât", 3, 3, 3, 3)
		
		self.myDb = db.db(self.db_file_name)
		self.myDb.save("player1", [r1,r2])
		self.myDb.save("player2", [r3])
	

	# def tearDown(self):
	# 	os.remove(self.db_file_name)


	def test_save_sth(self):
		results = self.myDb.read_all()

		self.assertEqual(len(results), 3)
		self.assertEqual(len(results[0]), 7)
		self.assertEqual(results[0][0], "player1")
		self.assertEqual(results[0][2], "toit")

	def test_name(self):
		players = self.myDb.read_field("name")
		self.assertEqual(players[0][0], "player1")
		self.assertEqual(players[2][0], "player2")

if __name__ == '__main__':
	unittest.main()