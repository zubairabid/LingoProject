import pymongo
from pymongo import MongoClient
import pprint
import re

client = MongoClient()
db = client.enron

# stores the number of matches
c = 0

# stores a list of dicts, where the dicts are the json objects (documents)
allmails = db.emails.find({'recipients.5':{ '$exists' : 'true' }})

# pronoun list to be used for limiting scope
plist = ['he', 'she', 'they', 'her', 'hers', 'his', 'him', 'theirs', 'them', 'their']

for mail in allmails:
	body = mail['body']
	
	try:
		mtype = mail['message_type']
	except:
		mtype = ""

	try:
		sub = mail['subject']
	except:
		sub = ""
	
	
	print("*"*80 + "\nMESSAGE TYPE :::: " + mtype + "\nSUBJECT :::: " + sub + "\n\n\n" + body + "\n\n\n");
