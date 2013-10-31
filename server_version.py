import MySQLdb
conn=MySQLdb.connect(host="localhost",user="root",passwd="hello",db="mysql")
cursor=conn.cursor()
cursor.execute("Select version();")
row=cursor.fetchone()
print "server version ",row[0]
cursor.close()
conn.close()
