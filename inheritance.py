class Father:
    def __init__(self, name, age):
        self.fatherName = name
        self.fatherAge = age

    def getFamilyDetails(self):
        print("Father Name: ", self.fatherName)
        print("Father Age: ", self.fatherAge)
        print("Son Name: ", self.sonName)
        print("Son Age: ", self.sonAge)
        print()


class Son(Father):
    def __init__(self, sonName, sonAge, fatherName, fatherAge):
        Father.__init__(self, fatherName, fatherAge)
        self.sonName = sonName
        self.sonAge = sonAge


son = Son("Son", 20, "father", 46)

son.getFamilyDetails()

print(son.fatherName, son.sonName)
