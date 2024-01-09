class Student:
    fullName = ""
    age = 0
    address = ""

    def details(self):
        print("fullName - ", self.fullName)
        print("age - ", self.age)
        print("address - ", self.address)


# creating a new object
obj1 = Student()
obj2 = Student()

obj1.fullName = "xyz"
obj1.age = 10
obj1.address = "pondy"

obj2.fullName = "abc"
obj2.age = 15
obj2.address = "chennai"

# print(obj1 is obj2)

# print(obj1.fullName)
# print(obj1.age)
# print(obj1.address)

# print(obj2.fullName)
# print(obj2.age)
# print(obj2.address)

print(obj1)
obj1.details()

print("\n")

print(obj2)
obj2.details()
