#!/bin/python
import psycopg2

def test(name, *haha, title , age , **ll):
	print(name)
	print(haha)
	print(title)
	print(age)
	print(ll['nn'])

if __name__ == '__main__':
	# conn = psycopg2.connect(database="rms_haohao", user="postgres", password="postgres", host="192.168.1.15", port="5432")
	# cur = conn.cursor()
	# # cur.execute('''CREATE TABLE COMPANY
	# #           (ID          INT NOT NULL,
	# #            NAME      TEXT              NOT NULL,
	# #            AGE        INT              NOT NULL,
	# #            ADDRESS   TEXT) ''')
	#
	# cur.execute('drop table company')
	#
	# print("Table created successfully")
	#
	# conn.commit()
	# conn.close()
	ll = {'nn':'haohao','nnn':18}
	test('haohao','1','2',title='haohao',age=18,**ll)

	haha = (1,2,3,4,5,6,7,8,9)
	print(len(haha))
	print(len(haha[-1:-10:-2]))
