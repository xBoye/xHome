# -*- coding: utf-8 -*-
import re

fin = "论语.txt"
fout = "论语_results.csv"
repl = '[，：。？！‘’""；\r\n]'
d={}

try:
	with open(fin, 'r', encoding='utf-8') as in_file:
		for l in in_file:
			l = list(re.sub(repl,'',l))
			for k in l:
				if k in d:
					d[k] +=1
				else:
					d.update({k:1})
except IOError:
	print('File error..')

results = 'id,name,degrees\n论语总字数为：' + str(sum(list((d.values()))))
d=sorted(d.items(),key=lambda a:a[1],reverse=True)
results = results + '；不重复字数为：'+str(len(d))
print(results)
id = 1
try:
	with open(fout, 'w', encoding='utf-8') as out_file:
		#print(results, file=out_file)
		for l in d:
			results = results + '\n' + str(id) + ',' + l[0]+',' + str(l[1])
			id += 1
		print(results, file=out_file)
except IOError:
	print('File error..')