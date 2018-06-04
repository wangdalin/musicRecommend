#-*- coding: utf-8 -*-
import xlrd

filename = "D:/code/OOP/mucis/data/labeled/baseline_%d.xlsx"


count = 0;
for i in range(1,8):
	data = xlrd.open_workbook(filename%i)
	table = data.sheets()[0]
	count = count + 1
	with open("txtdata/data%d.txt"%count,'w', encoding = 'utf-8') as f:

		for x in range(1,table.nrows):

			qid = str(int(table.cell(x,0).value)).replace('$',' ')
			qid = qid.replace('#',' ')

			query = str(table.cell(x,1).value).replace('$',' ')
			query = query.replace('#',' ')
			
			sim_id = str(int(table.cell(x,2).value)).replace('$',' ')
			sim_id = sim_id.replace('#',' ')
			
			sim_comment = str(table.cell(x,3).value).replace('$',' ')
			sim_comment = sim_comment.replace('#',' ')
			
			song_id = str(int(table.cell(x,4).value)).replace('$',' ')
			song_id = song_id.replace('#',' ')
			
			song_name = str(table.cell(x,5).value).replace('$',' ')
			song_name = song_name.replace('#',' ')
			
			lyric = str(table.cell(x,6).value).replace('$',' ')
			lyric = lyric.replace('#',' ')
			
			author = str(table.cell(x,7).value).replace('$',' ')
			author = author.replace('#',' ')

			label = str(int(table.cell(x,8).value)).replace('$',' ')
			label = label.replace('#',' ')
			
			values = [qid,query,sim_id,sim_comment,song_id,song_name,lyric,author,label]
			value = "#".join(values)
			value = value+"$"

			# print(value)
			# print(type(value))
			f.write(value)
		f.close()	


for i in range(11,23):
	count = count + 1
	data = xlrd.open_workbook(filename%i)
	table = data.sheets()[0]
	with open("txtdata/data%d.txt"%count,'w', encoding = 'utf-8') as f:

		for x in range(1,table.nrows):
			
			qid = str(int(table.cell(x,0).value)).replace('$',' ')
			qid = qid.replace('#',' ')

			query = str(table.cell(x,1).value).replace('$',' ')
			query = query.replace('#',' ')
			
			sim_id = str(int(table.cell(x,2).value)).replace('$',' ')
			sim_id = sim_id.replace('#',' ')
			
			sim_comment = str(table.cell(x,3).value).replace('$',' ')
			sim_comment = sim_comment.replace('#',' ')
			
			song_id = str(int(table.cell(x,4).value)).replace('$',' ')
			song_id = song_id.replace('#',' ')
			
			song_name = str(table.cell(x,5).value).replace('$',' ')
			song_name = song_name.replace('#',' ')
			
			lyric = str(table.cell(x,6).value).replace('$',' ')
			lyric = lyric.replace('#',' ')
		
			author = str(table.cell(x,7).value).replace('$',' ')
			author = author.replace('#',' ')

			label = str(int(table.cell(x,8).value)).replace('$',' ')
			label = label.replace('#',' ')

			values = [qid,query,sim_id,sim_comment,song_id,song_name,lyric,author,label]
			value = "#".join(values)
			value = (value+"$")
			# print(value)
			# print(type(value))
			f.write(value)			


	f.close()





