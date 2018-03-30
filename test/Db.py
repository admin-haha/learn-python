#!/bin/python
import psycopg2



if __name__ == '__main__':
	conn = psycopg2.connect(database="rms_haohao", user="postgres", password="postgres", host="192.168.1.15", port="5432")
	cur = conn.cursor()
	# cur.execute('''CREATE TABLE COMPANY
	#           (ID          INT NOT NULL,
	#            NAME      TEXT              NOT NULL,
	#            AGE        INT              NOT NULL,
	#            ADDRESS   TEXT) ''')

	cur.execute('drop table company')

	print("Table created successfully")

	conn.commit()
	conn.close()
