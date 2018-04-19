import pymongo
from pymongo import MongoClient
import pprint
import re

mail_list = [453122, 57747, 255317, 1101758, 688227, 712748, 1052732, 1188275, 1188275, 561070, 164064, 951620, 107191, 63807, 948856]

client = MongoClient()
db = client.enron

for uid in mail_list:
	mail = db.emails.find_one( { 'uid' : uid } )

	try:
		sender = mail['sender']
	except:
		continue


	sdr = db.entities.find_one( { 'uid'  : int(sender) } )
	nm = sdr['email_names']
	try:
		gender = sdr['gender']
	except:
		gender = 'NO GENDER MARKED'

	try:
		aff = sdr['affiliation']
	except:
		aff = 'NO AFFILIATION MARKED'

	print('email with uid {0} has sender {1}, {4} with marked gender = {2} and affiliation {3}'.format(uid, nm, gender, aff, sender))
	print('-'* 80)	
