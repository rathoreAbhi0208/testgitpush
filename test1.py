import pymongo

client = pymongo.MongoClient("mongodb+srv://Abhi:abhi02@cluster0.ozaps66.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['MyInfo']
collection = database['Abhi']

# record = collection.find()
# for i in record:
#     print(i)
#

# data = collection.find({'companyName':'iNeuron'})
# for i in data:
#     print(i)

data = collection.find({'courseOffered':{'$gt':'E'}})
for i in data:
    print(i)