class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    def __init__(self, firstName, lastName, id, scores):
        super().__init__(firstName, lastName, id)
        self.scores = scores

    def calculate(self):
        av = sum(scores)/len(scores)
        return av

line = "Heraldo Memelli 8135627".split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = 8135627
scores = list( map(int, "100 80".split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())