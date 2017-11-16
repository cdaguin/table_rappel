# from random import randint
import random
from time import time
from collections import namedtuple

Result = namedtuple('response', 'word value tries found time')

class table_rappel_game:

	def __init__(self, table, params):
		self.table = table
		self.name = params['name']
		self.min_value = params['min']
		self.max_value = params['max']
		self.nb_questions = params['nb_questions']
		self.results = []

	def ask_question(self, num_question, value_to_find):
		found = False
		ignored = False
		tries = 1
		while not (found or ignored):
			str_read = input('Word n°{} {} (try n°{}) (? for response) : '.format(num_question+1, self.table[value_to_find], tries))
			try:
				if str_read == '?':
					print("Response {} : {}".format(table[value_to_find], i))
					ignored = True;
				else:
					response = int(str_read)
					if (response == value_to_find):
						found = True;
					else:
						tries += 1
			except ValueError:
				tries += 1
		return (tries, found)

	def play(self):
		for num_question in range(self.nb_questions):
			
			num_to_find = random.randint(self.min_value, self.max_value) if self.min_value != self.max_value else self.min_value
			start_time = time()

			resp = self.ask_question(num_question, num_to_find)
			
			r = Result(self.table[num_to_find], num_to_find, resp[0], resp[1], time() - start_time)

			self.results.append(r)

	def print_results(self):
		for r in self.results:
			if r.found:
				print("{:2d} {:s}  : {:d} tries in {:2.2f} seconds".format(r.value, r.word, r.tries, r.time))
			else:
				print("{:2d} {:s}  : {:d} tries and not found".format(r.value, r.word, r.tries))

	def get_results(self):
		return self.results

	def get_name(self):
		return self.name
