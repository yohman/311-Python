import sqlite3
import unicodecsv
import re

connection = sqlite3.connect('20110311.db')

cursor = connection.cursor()
query = """SELECT date,url,body from tweets where body like '%#hinan%' order by date LIMIT 0,100"""
# query = """SELECT nickname, body, date,url FROM tweets LIMIT 0,100"""

# out_csv = unicodecsv.DictWriter(open('311_first60mins_nodes_only.csv', 'w'), ['Source', 'Target','date','body'])
out_csv = unicodecsv.DictWriter(open('anpi.csv', 'w'), ['date', 'username','body'])
# out_csv.writerow({'Source' : 'Source', 'Target' : 'Target','date':'date','body':'body'})
out_csv.writerow({'date' : 'date', 'username' : 'username', 'body' : 'body'})

for row in cursor.execute(query):
	date = row[0]
	url = row[1]
	body = row[2]
	body = body.replace("'","\"")
	body = body
	username = url.split('/')[3]

	print date+": "+username+"-->"+body
	# out_csv.writerow({'Source' : '\''+username+'\'', 'Target' : '\''+cleanword+'\'', 'date':'\''+date+'\'','body': '\''+body+'\''})
	# out_csv.writerow({'Source' : username, 'Target' : cleanword})