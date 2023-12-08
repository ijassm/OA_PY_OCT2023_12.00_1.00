# person1 = {"name": "xyz", "age": 10, "skills": ["PY", "JAVA"]}
# person2 = {"name": "abc", "age": 20, "skills": ["PY", "JS"]}


# skills = person1["skills"]
# print(type(person1))
# print(person1["name"])
# print(person1["age"])
# print()
# print(skills[0])
# print(skills[1])

# person1["skills"].append("JS")
# person1["age"] = 20


# person1.update({"address": "chennai"})
# person2["address"] = "pondy"

# print(person1)
# print(person2)

# persons = [
#     {"name": "abc", "age": 25, "skills": ["JS", "CSS"]},
#     {"name": "xyz", "age": 30, "skills": ["PY", "JAVA", "HTML"]},
#     {"name": "def", "age": 22, "skills": ["C++", "JS", "CSS"]},
#     {"name": "ghi", "age": 35, "skills": ["JAVA", "HTML"]},
#     {"name": "jkl", "age": 28, "skills": ["PY", "C++", "CSS"]},
#     {"name": "mno", "age": 18, "skills": ["JS", "HTML"]},
#     {"name": "pqr", "age": 40, "skills": ["PY", "JAVA"]},
#     {"name": "stu", "age": 32, "skills": ["JS", "C++", "HTML"]},
#     {"name": "vwx", "age": 27, "skills": ["PY", "CSS"]},
#     {"name": "yz", "age": 23, "skills": ["JAVA", "JS"]},
# ]

# names = []
# ages = []

# print(names)
# print(ages)

# for i in persons:
#     names.append(i["name"])
#     ages.append(i["age"])

# print(names)
# print(ages)


persons = [
    {"id": 1, "name": "John Doe", "age": 28, "skills": ["PY", "CSS"]},
    {"id": 2, "name": "Jane Smith", "age": 30, "skills": ["JAVA", "HTML"]},
    {"id": 3, "name": "Michael Johnson", "age": 22, "skills": ["C++", "JS", "CSS"]},
    {"id": 4, "name": "Emily Davis", "age": 35, "skills": ["JAVA", "HTML"]},
    {"id": 5, "name": "Christopher Brown", "age": 28, "skills": ["PY", "C++", "CSS"]},
    {"id": 6, "name": "Olivia White", "age": 18, "skills": ["JS", "HTML"]},
    {"id": 7, "name": "David Hall", "age": 40, "skills": ["PY", "JAVA"]},
    {"id": 8, "name": "Sophia Miller", "age": 32, "skills": ["JS", "C++", "HTML"]},
    {"id": 9, "name": "Daniel Wilson", "age": 27, "skills": ["PY", "CSS"]},
    {"id": 10, "name": "Emma Taylor", "age": 23, "skills": ["JAVA", "JS"]},
    {"id": 11, "name": "Liam Brown", "age": 31, "skills": ["JS", "C++", "HTML"]},
    {"id": 12, "name": "Ava Smith", "age": 25, "skills": ["PY", "CSS"]},
    {"id": 13, "name": "Noah Johnson", "age": 29, "skills": ["JAVA", "HTML"]},
    {"id": 14, "name": "Olivia Davis", "age": 33, "skills": ["C++", "JS", "CSS"]},
    {"id": 15, "name": "Liam White", "age": 26, "skills": ["PY", "C++", "CSS"]},
    {"id": 16, "name": "Emma Hall", "age": 20, "skills": ["JS", "HTML"]},
    {"id": 17, "name": "Aiden Taylor", "age": 37, "skills": ["PY", "JAVA"]},
    {"id": 18, "name": "Sophia Wilson", "age": 34, "skills": ["JS", "C++", "HTML"]},
    {"id": 19, "name": "Mia Miller", "age": 24, "skills": ["PY", "CSS"]},
    {"id": 20, "name": "Ethan Brown", "age": 21, "skills": ["JAVA", "JS"]},
]


id = 10

for i in persons:
    if id == i["id"]:
        print(i)


# -------------------------------------------------------------------

# person = ["bala", 12, ["PY", "JAVA"], "pondy"]

# person = {"name": "bala", "age": 10, "address": "pondy", "name": "xyz"}

# print(person)
