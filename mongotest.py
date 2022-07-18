import pymongo
client = pymongo.MongoClient("mongodb+srv://Abhi:abhi02@cluster0.xvex2zh.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name' : 'Abhishek',
    'email' : 'abhi@gmail.com',
    'surname' : 'singh'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)