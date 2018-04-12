import pymongo
from pymongo import MongoClient
import pprint
import re

client = MongoClient()
db = client.enron

# stores the number of matches
c = 0

peeps = db.entities.find()

aflist = {}

for person in peeps:
    try:
        aflist[person['affiliation']] = 1
    except:
        pass

for i in aflist:
    print(i)
