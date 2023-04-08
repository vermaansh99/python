class Person:
    # class attribute
    species = "Homosepains"

    def _init_(self, name, age):
        self.name = name
        self.age = age

    def speak(self, word="Hello"):
        print(word+" "+self.name)

    def walk(self):
        print("Walking")


def speak(self):
    print("Hello "+self.name)


# Inheritance
class Student(Person):
    def _init_(self, name, age, roll_number):
        super()._init_(name, age)
        self.roll_number = roll_number

    def learn(self):
        print("Learning..")

    # method overiding
    def speak(self, word="Hi"):
        print(word+" "+self.name)


class Teacher(Person):
    def _init_(self, name, age, department_id):
        super()._init_(name, age)
        self.department_id = department_id

    def teach(self):
        print("Teaching..")

    def speak(self, word="Welcome"):
        print(word+" "+self.name)


# instantiate a object from a class
student1 = Student("Sumit", 25, "1MV19IS404")
print(student1.roll_number)
print(student1.species)
print(Person.species)

student1.learn()
student1.speak()

teacher = Teacher("Ansh", 21, "123")
print(teacher.department_id)
teacher.speak()



def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender


   