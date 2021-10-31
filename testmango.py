import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://nikos:123@cluster0.u2pew.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["test"]

collection = db["test"]

#collection.insert_one({"_id": 0, "name":'nikos', "score": 5})

#collection.insert_many([{"_id": 5, "name":'nikos', "score": 5},{"_id": 6, "name":'nikos', "score": 5}])

results = collection.find({'name':'nikos'})

one = collection.find_one({'_id': 5})

#collection.delete_one({})
#collection.update_one({'_id: 5'},{"$set":{"name":"kostas"}})
#count = collection.count_documents({})

print(one)

for result in results:
	print(result)