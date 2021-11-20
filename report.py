def rep():
	import csv
	import sqlite3
	list = []
	#templist = []
	def displayDatabase():
		conn= sqlite3.connect('FaceBase.db')
		cmd="SELECT * FROM Student "
		cursor=conn.execute(cmd)
		for row in cursor:
			templist = []
			if row[1] == True:
				status = "Not-Student"
			else:
				status = "Student"
			templist.append(row[0])
			templist.append(row[1])
			templist.append(row[3])
			templist.append(row[2])
			templist.append(row[4])
			templist.append(row[5])
			templist.append(row[6])
			templist.append(row[7])
			#templist.append(status)
			list.append(templist)
		conn.commit()
		conn.close()

	reportfile = open('report.csv', 'w')
	reportwriter = csv.writer(reportfile)
	reportwriter.writerow(['Student Number', 'Student Name','Mail','Gender','Faculty','Department','Nationality','Identity Number'])
	for i in range(0, 10):
		displayDatabase()
		reportwriter.writerow(list[i])
		list = []
	reportfile.close()
