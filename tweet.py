import sqlite3
import unicodecsv
import re

connection = sqlite3.connect('20110311.db')

cursor = connection.cursor()
# query = """SELECT nickname, body, date FROM tweets WHERE date > '2011-03-11 12:00:00' AND date < '2011-03-11 13:00:00' AND body LIKE '%@%'"""
query = """SELECT nickname, body, date FROM tweets WHERE url LIKE 'http://twitter.com/ooe_san/%' AND body LIKE '%@%'"""

out_csv = unicodecsv.DictWriter(open('ooe_san.csv', 'w'), ['Source', 'Target','date','body'])
out_csv.writerow({'Source' : 'Source', 'Target' : 'Target', 'date' : 'date', 'body' : 'body'})

for row in cursor.execute(query):
	this_user = row[0]
	text_field = row[1]
	date = row[2]

	for word in text_field.split(' '):
		if len(word) > 0:
			if word[0] == '@':
				# print word[0]
				cleanword = word.replace("@","")
				cleanword = cleanword.replace(":","")
				cleanuser = this_user.replace("\n","")
				cleanuser = this_user.replace("\\n","")
				error = False
				if cleanword == '': error = True
				if cleanuser == '': error = True
				if len(cleanword) > 30: error = True
				if error == False:
					print date+": "+cleanuser+"-->"+cleanword
					out_csv.writerow({'Source' : cleanuser, 'Target' : cleanword, 'date':date,'body': text_field})