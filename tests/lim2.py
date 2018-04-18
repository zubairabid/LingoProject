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
#plist = ['he', 'she', 'they', 'her', 'hers', 'his', 'him', 'theirs', 'them', 'their']
plist = ['(s)he', 'he/she', 'she/he', 'he\she', 'she\he', 'he or she', 'she or he', 'his/her', 'his/hers', 'his or hers', 'his or her', 'her/his', 'hers/his', 'hers or his', 'her or his']

for mail in allmails:
	ll = []

	uid = mail['uid']

	body = mail['body']
	# getting sender uid string
	try:
		sender = mail['sender']
	except:
		continue

	# ORIGINAL MESSAGE
	annotations = mail['annotations']
	orhelper = annotations[len(annotations) - 1]
	origin = body[orhelper['start_index'] : orhelper['end_index']]

	#sdr = db.entities.find_one( { 'uid'  : int(sender) } )
	#eid = sdr['email_address']
	#nm = sdr['email_names']
	#try:
	#	gndr = sdr['gender']
	#except:
	#	gndr = "NO GENDER MARKED"
	#
	#try:
	#	aff = sdr['affiliation']
	#except:
	#	aff = "AFFLILIATION UNMARKED"

	# # MIGHT NEED TO REMOVE
	# if (gndr != 'M' and gndr != 'F'):
	# 	continue

	# getting recipients uid string list
	rec = mail['recipients']

	# getting message type
	try:
		mtype = mail['message_type']
	except:
		mtype = "MESSAGE TYPE UNMARKED"

	# subject
	try:
		sub = mail['subject']
	except:
		sub = "SUBJECT UNMARKED"

	for key in plist:

		# eliminating non matches
		if (re.search(r'\b' + key + r'\b', origin) is None):
			continue

		ll.append(key)

		if (key == plist[len(plist) - 1]):
			c += 1
			print("*"*120)
			print("MESSAGE TYPE :::: " + str(mtype))
			print("UID :::: " + str(uid))
			print("SUBJECT :::: " + str(sub))
			print("KEY(s) :::: " + str(ll))
			print("SENDER :::: " + str(sender))
	#		print("SENDER EMAIL :::: " + str(eid))
	#		print("SENDER NAME(S) :::: " + str(nm))
	#		print("SENDER GENDER :::: " + str(gndr))
	#		print("SENDER AFFLILIATION :::: " + str(aff))
			print("RECEIVERS :::: " + str(rec))
			print("COUNT :::: " + str(c));
			print("\nORIGINAL MESSAGE: \n\n\n" + str(origin) + "\n\n\n")
			# print("*"*120 + "\nMESSAGE TYPE :::: " + str(mtype) + "\nSUBJECT :::: " + str(sub) + "\nKEY(s) :::: " + str(ll) + "\nSENDER :::: " + str(sender) + "\nSENDER EMAIL :::: " + str(eid) + "\nSENDER NAME(S) :::: " + str(nm) + "SENDER GENDER :::: " + str(gndr) + "\nRECEIVERS :::: " + str(rec) + "\nCOUNT :::: " + str(c) + "\n\n\n" + str(body) + "\n\n\n")
