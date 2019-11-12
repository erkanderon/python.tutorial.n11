from .Animal import AnimalClass

class Horse(AnimalClass):
	def __init__(self, name, feel, arm_count):
		self.title = "At"

		AnimalClass.__init__(self, name, feel, arm_count)

	def describe(self):
		print(self.name + " has a title " + self.title)
		print(self.name + " called as " + self.name)
		if isinstance(self.call, Horse):
			print(self.name + " call " + self.call() + " because he feels like " + self.feel)
		print(self.name + " have " + str(self.arm_count) + " arm")