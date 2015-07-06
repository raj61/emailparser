#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","password","db_name" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

s=str(file("emails.txt").read())
w=s.split(';');

#for every emailid in file
for i in w:
    # Prepare SQL query to INSERT a record into the database.
    # Replace Table name
    sql = "INSERT INTO TABLE(email) \
       VALUES ('%s')" % \
       (i)
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
       print "Data entered Successfully"
    except:
       # Rollback in case there is any error
       db.rollback()
       print "Error"

# disconnect from server
db.close()


    
