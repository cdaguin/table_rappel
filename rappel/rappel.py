# lit un fichier csv
# met les données dans une liste et un dictionnaire
# propose un mot à l'utilisateur et attend le nombre correspondant
# Tant que la réponse est invalide propose le même mot
# Pour chaque nouveau mot, comptabilise le temps de réponse
# écrit tout les résultats dans une base de données.

#TODO
# exploiter la BDD pour faire des stats par user et par mot
#done  choisir une plage de travail (avec valeurs par défaut)
#done appuyer sur ? pour avoir la réponse
#done  Choisir le nombre de questions (avec valeurs par défaut)
# simplifier le code qui check les reponses
# simplifier l'insertion en BDD, il y a plein d'opérations manuelles
# avoir un fichier de paramètres par défaut par utilisateur
# formatter la sortie des resultats pour que tout soit aligné
# faire des fonctions
# faire des tests
# interface graphique pour afficher les stats
# selection du player dans une liste
# faire sortie propre sur CTRL+C
# probleme d'eception si on entre 8°<del>0 : UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc2 in position 1: invalid continuation byte

default_nb_questions = 20


import csv


import game
import db


class table_rappel:

	def __init__(self, filename):
		self.words = []
		self.read_csv_file(filename)

	def get_word_count(self):
		return len(self.words)

	def read_csv_file(self, filename):
		with open(filename, 'r') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				self.words += row

	# Overload operator []
	def __getitem__(self, index):
		return self.words[index]






def read_input_between_min_max(description, min_value, max_value, default_value):
	try:
		value = int(input("{} [{} - {}] default ({}) : ".format(description, min_value, max_value, default_value)))
		if not min_value <= value <= max_value:
			value = default_value
	except ValueError:
		value = default_value
	return value

def read_input_for_game(word_count):
	name = input("Player name : ")
	min_value = read_input_between_min_max("First value", 0, word_count - 1, 0)
	max_value = read_input_between_min_max("Last value", min_value, word_count - 1, word_count - 1)

	nb_questions = default_nb_questions
	try:
		nb_questions = int(input("Number of questions default ({}) : ".format(default_nb_questions)))
	except ValueError:
		pass

	print("will ask {} questions from value {} to {}".format(nb_questions, min_value, max_value))

	return {'name':name, 'min':min_value, 'max':max_value, 'nb_questions':nb_questions}



if __name__ == "__main__":
	myTable = table_rappel("data/table.csv")

	params = read_input_for_game(myTable.get_word_count())

	partie = game.table_rappel_game(myTable, params)
	partie.play()
	partie.print_results()

	myDb = db.db("output/exemple.db")
	myDb.save(partie.get_name(), partie.get_results())





  # if __name__ == "__main__":
  #      parser = argparse.ArgumentParser(
  #          description='Scrape a webpage.')
  #      parser.add_argument(
  #          '-t',
  #          '--type',
  #          choices=['all', 'png', 'jpg'],
  #          default='all',
  #          help='The image type we want to scrape.')
  #      parser.add_argument(
  #          '-f',
  #          '--format',
  #          choices=['img', 'json'],
  #          default='img',
  #          help='The format images are saved to.')
  #      parser.add_argument(
# 	'url',
  #          help='The URL we want to scrape for images.')
  #      		args = parser.parse_args()
  #      		scrape(args.url, args.format, args.type)

