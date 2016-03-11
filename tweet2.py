# import relevant libraries
import sqlite3
import unicodecsv
import re

# make connection to sqlite database
connection = sqlite3.connect('20110311.db')
cursor = connection.cursor()

# query to extract tweets for a given time span
query = """SELECT nickname, body, date,url FROM tweets WHERE date > '2011-03-11 14:47:00' AND date < '2011-03-11 15:47:00' AND body LIKE '%@%'"""

# define parameters for output file
out_csv = unicodecsv.DictWriter(open('311_first60mins_nodes_only.csv', 'w'), ['Source', 'Target'])
out_csv.writerow({'Source' : 'Source', 'Target' : 'Target'})

# loop through each record in the database
for row in cursor.execute(query):
	# identify relevant fields to extract
	this_user = row[0]
	body = row[1]
	body = body.replace("'","\"")
	body = body
	date = row[2]
	url = row[3]

	# username needs to be extracted from url field
	username = url.split('/')[3]

	# find every instance of "@" mentions and create a source -> target row
	for word in body.split(' '):
		if len(word) > 0:
			if word[0] == '@':
				# clean the data
				cleanword = word.replace("@","")
				cleanword = cleanword.replace(":","")
				cleanuser = this_user.replace("\n","")
				cleanuser = this_user.replace("\\n","")
				error = False
				if cleanword == '': error = True
				if cleanuser == '': error = True
				if len(cleanword) > 30: error = True
				if username == cleanword: error = True # don't allow self direction
				if error == False:
					print date+": "+username+"-->"+cleanword+"-->"+'"'+body+'"' : '\''+cleanword+'\'', 'date':'\''+date+'\'','body': '\''+body+'\''})
					out_csv.writerow({'Source' : username, 'Target' : cleanword})