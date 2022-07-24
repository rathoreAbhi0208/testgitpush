import pymongo

client = pymongo.MongoClient("mongodb+srv://Abhi:abhi02@cluster0.ozaps66.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data ={
  "objectIdFieldName": "OBJECTID",
  "uniqueIdField": {
    "name": "OBJECTID",
    "isSystemMaintained": 'true'
  },
  "globalIdFieldName": "",
  "fields": [
    {
      "name": "OBJECTID",
      "type": "esriFieldTypeOID",
      "alias": "OBJECTID",
      "sqlType": "sqlTypeOther",
      "domain": 'null',
      "defaultValue": 'null'
    },
    {
      "name": "AreaID",
      "type": "esriFieldTypeInteger",
      "alias": "AreaID",
      "sqlType": "sqlTypeOther",
      "domain": 'null',
      "defaultValue": 'null'
    },
    {
      "name": "RegionID",
      "type": "esriFieldTypeInteger",
      "alias": "RegionID",
      "sqlType": "sqlTypeOther",
      "domain": 'null',
      "defaultValue": 'null'
    },
    {
      "name": "Area",
      "type": "esriFieldTypeString",
      "alias": "Area",
      "sqlType": "sqlTypeOther",
      "length": 2048,
      "domain": 'null',
      "defaultValue": 'null'
    },
    {
      "name": "Year",
      "type": "esriFieldTypeInteger",
      "alias": "Year",
      "sqlType": "sqlTypeOther",
      "domain": 'null',
      "defaultValue": 'null'
    },
    {
      "name": "Q1",
      "type": "esriFieldTypeInteger",
      "alias": "Q1",
      "sqlType": "sqlTypeOther",
      "domain": 'null',
      "defaultValue": 'null'
    },
    {
      "name": "Q2",
      "type": "esriFieldTypeInteger",
      "alias": "Q2",
      "sqlType": "sqlTypeOther",
      "domain": 'null',
      "defaultValue": 'null'
    },
    {
      "name": "Q3",
      "type": "esriFieldTypeInteger",
      "alias": "Q3",
      "sqlType": "sqlTypeOther",
      "domain": 'null',
      "defaultValue": 'null'
    },
    {
      "name": "Q4",
      "type": "esriFieldTypeInteger",
      "alias": "Q4",
      "sqlType": "sqlTypeOther",
      "domain": 'null',
      "defaultValue": 'null'
    }
  ],
  "features": [
    {
      "attributes": {
        "OBJECTID": 1,
        "AreaID": 2,
        "RegionID": 19,
        "Area": "Cavan Monaghan",
        "Year": 2022,
        "Q1": 104,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 2,
        "AreaID": 1,
        "RegionID": 20,
        "Area": "Carlow Kilkenny South Tipperary",
        "Year": 2022,
        "Q1": 203,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 3,
        "AreaID": 11,
        "RegionID": 20,
        "Area": "Kerry",
        "Year": 2022,
        "Q1": 97,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 4,
        "AreaID": 13,
        "RegionID": 21,
        "Area": "Mayo",
        "Year": 2022,
        "Q1": 89,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 5,
        "AreaID": 10,
        "RegionID": 21,
        "Area": "Galway Roscommon",
        "Year": 2022,
        "Q1": 253,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 6,
        "AreaID": 17,
        "RegionID": 20,
        "Area": "Waterford Wexford",
        "Year": 2022,
        "Q1": 282,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 7,
        "AreaID": 5,
        "RegionID": 19,
        "Area": "Dublin North",
        "Year": 2022,
        "Q1": 189,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 8,
        "AreaID": 14,
        "RegionID": 21,
        "Area": "The Midwest",
        "Year": 2022,
        "Q1": 294,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 9,
        "AreaID": 15,
        "RegionID": 18,
        "Area": "The Midlands",
        "Year": 2022,
        "Q1": 215,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 10,
        "AreaID": 16,
        "RegionID": 21,
        "Area": "Sligo Leitrim West Cavan",
        "Year": 2022,
        "Q1": 65,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 11,
        "AreaID": 9,
        "RegionID": 18,
        "Area": "Dublin South West Kildare West Wicklow",
        "Year": 2022,
        "Q1": 265,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 12,
        "AreaID": 8,
        "RegionID": 18,
        "Area": "Dublin South East Wicklow",
        "Year": 2022,
        "Q1": 144,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 13,
        "AreaID": 7,
        "RegionID": 18,
        "Area": "Dublin South Central",
        "Year": 2022,
        "Q1": 216,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 14,
        "AreaID": 4,
        "RegionID": 21,
        "Area": "Donegal",
        "Year": 2022,
        "Q1": 137,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 15,
        "AreaID": 3,
        "RegionID": 20,
        "Area": "Cork",
        "Year": 2022,
        "Q1": 495,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 16,
        "AreaID": 12,
        "RegionID": 19,
        "Area": "Louth Meath",
        "Year": 2022,
        "Q1": 242,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    },
    {
      "attributes": {
        "OBJECTID": 17,
        "AreaID": 6,
        "RegionID": 19,
        "Area": "Dublin City North",
        "Year": 2022,
        "Q1": 261,
        "Q2": 'null',
        "Q3": 'null',
        "Q4": 'null'
      }
    }
  ]
}


database = client['MyPractice']
coll = database['DataSet']
coll.insert_one(data)