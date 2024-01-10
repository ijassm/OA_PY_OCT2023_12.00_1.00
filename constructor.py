class Student:
    def __init__(self, fullName, age, address):
        self.fullName = fullName
        self.age = age
        self.address = address

    def details(self):
        print("fullName - ", self.fullName)
        print("age - ", self.age)
        print("address - ", self.address)


# creating a new object
obj1 = Student("xyz", 20, "pondy")
obj2 = Student("abc", 15, "chennai")

obj1.details()
obj2.details()
