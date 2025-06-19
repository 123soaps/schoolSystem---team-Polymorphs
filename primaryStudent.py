#Create a PrimaryStudent class in this file
#Accept and assign agreed parameters in the constructor and define agreed public methods in the class
#Program the class so that users of the class only need to interact with its methods
class Student(Person):
    def _init_ (self, name, schoolYear):
        super()._init(name)
        self.schoolYear=schoolYear
        print("Created(self.name) in your (self.schoolYear) Student")

class PrimaryStudent (student):
    def _init_(self, name, schoolYear):
        super()._init_(name, schoolYear)
        print("Created (self.name)in a schoolYear). PrimaryStudent")
    def greet(self, person=None):
        if person=None:
            print("no")

class Ryan:
    def __init__(self, age, preferences):
        self.age <= 14
        self.preferences = "they must be under 14, if not, get out of ryans vicinity"
