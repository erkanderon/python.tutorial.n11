from inheritance.Human import Human
from inheritance.Horse import Horse

class TutorialMainClass:

	def __init__(self):
		print("Tutorial Başlıyor...")


if __name__=="__main__":

	TutorialMainClass()

	print("------------------------------------")
		
	# Inheritance call
	person = Human("Erkan", "happy", 2, "Devops")
	person.describe()
	person.call()

	print("------------------------------------")

	horse = Horse("İnci", "sad", 4)
	horse.describe()
	horse.call()

	# Decorators call


