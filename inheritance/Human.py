from .Animal import AnimalClass

class Human(AnimalClass):
	def __init__(self, name, feel, arm_count, work_title):
		self.title = "İnsan"
		self.work_title = work_title

		AnimalClass.__init__(self, name, feel, arm_count)

	def describe(self):
		print(self.name + " has a title " + self.title)
		print(self.name + " called as " + self.name)
		print(self.name + " call " + self.call() + " because he feels like " + self.feel)
		print(self.name + " have " + str(self.arm_count) + " arm")
		print(self.name + " has a title called " + self.work_title)

	def call(self):
		if self.feel == "happy":
			return "Haha"
		elif self.feel == "sad":
			return "Tüh"
		else:
			return "Lolololo"