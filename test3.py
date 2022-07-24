import pymongo


client = pymongo.MongoClient("mongodb+srv://Abhi:abhi02@cluster0.ozaps66.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = {
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": 'true',
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}


database = client['SuperHeroes']
collection = database['Table']
#collection.insert_many(one)

#collection.update_one({'squadName':'Super hero squad','name':'Molecule Man'},{'$set':{'age':30}})
record  = collection.find({'members':{'name':'Molecule Man'}})
for i in record:
  print(i)

