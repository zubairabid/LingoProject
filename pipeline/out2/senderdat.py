import pymongo
from pymongo import MongoClient
import pprint
import re

mail_list = [46030, 44264, 401171, 1260916, 273429, 1114355, 275760, 922548, 745614, 291116, 810451, 2976, 84079, 859183, 44264, 682902, 705237, 1105030, 560878, 1262942, 285428, 1188651, 62974, 824867, 682950, 284998, 44236, 921340, 6705, 780944, 31184, 208817]

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
