from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

username = "enter your username"
password = "enter your password"

uri = f"mongodb+srv://{username}:{password}@oa.lybaz26.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["OA_PY_OCT2023_12_1"]

students = db["students"]

doc = {
    "firstName": "XYZ",
    "lastName": "ABC",
    "email": "xyz@example.com",
    "age": 12,
    "skills": ["PY", "JAVA"],
    "address": {
        "street": "pondy",
        "city": "chennai",
        "state": "Tamil Nadu",
        "country": "India",
    },
    "phone": "9876543210",
}

students.insert_one(doc)
