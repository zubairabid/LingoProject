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

# OLD ALGO:: found all substrings, even instances like 'his' in 'this'
#	if any(key in body for key in plist):
#		c = c + 1
#
#		print("\n" + key + ":\n")
#		pprint.pprint(body)
#		print(str(c) + "\n\n")
	
# ALGO: prints the docs, highlighting the found pronoun. Bugs exist
	for key in plist:
		if(re.search(r'\b' + key + r'\b', body) is not None):
			c = c + 1
			print("\n:-::--:" + key + ": ")
			body = body[:body.index(key):] + '*'*50 + key.upper() + "*"*50 + body[body.index(key)::]
			pprint.pprint(body)
			print(str(c) + "\n\n")

print(c)
