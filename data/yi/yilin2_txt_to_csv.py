"""易林后半部分文本转为csv文件。"""
# -*- coding: utf-8 -*-

fin = "test.txt"
fout = "test_out.csv"
#fin = "yilin2Doc.txt"
#fout = "yilin2Doc.csv"

g64=['乾之','坤之','屯之','蒙之','需之','讼之','师之','比之','小畜之','履之','泰之','否之','同人之','大有之','谦之','豫之','随之','蛊之','临之','观之','噬嗑之','贲之','剥之','复之','无妄之','大畜之','颐之','大过之','坎之','离之','咸之','恒之','遯之','大壮之','晋之','明夷之','家人之','睽之','蹇之','解之','损之','益之','夬之','姤之','萃之','升之','困之','井之','革之','鼎之','震之','艮之','渐之','归妹之','丰之','旅之','巽之','兑之','涣之','节之','中孚之','小过之','既济之','未济之']

id = 1153   #易林后半部分从1153条临之临开始
try:
	with open(fin, 'r',encoding='utf-8') as in_file, open(fout, 'w',encoding='utf-8') as out_file: 
		print('id,jname,jci,yi_id', file=out_file)
		for line in in_file:
			line = (','.join(line.split('。',1))).strip('\n')
			line = str(id)+','+g64[(id-1)//64]+line+','+str((id-1)//64+1)
			print(line, file=out_file)
			id += 1
except IOError:
	print('File error..')
