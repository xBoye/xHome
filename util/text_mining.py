# -*- coding: utf-8 -*-
import os, re

fin = "d:\\xhome\\data\\text_mining\\禅诗.txt"
fout = "d:\\xhome\\data\\out_file\\禅诗_results.csv"
book=os.path.split(fin)[1].split('.')[0]   #书名

repl = '[，：。？∶:;！（）、=《》’‘“\'"\r\n\s )ばhＮB0℃zＧｎｂｄｃ□ｊｔYoｙt／_Ａp@ -Luｌ；bｕ·yie．dｅ３a「２nF,＠Ｖｋ＜＞ｒｐｉ『』ｇｏjａ/2┦ｘ\sZ(＝（）ｖΥw”TW○乙－Ｔ￣１Ｑ８Ｓ０s,r＂Ｆ─]'

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

results = 'id,name,degrees\n' + book + '总字数为：' + str(sum(list((d.values()))))
results = results + '；不重复字数为：'+str(len(d))
print(results)

d=sorted(d.items(),key=lambda a:a[1],reverse=True)
id = 1
try:
	with open(fout, 'w', encoding='utf-8') as out_file:
		print(results, file=out_file)
		for l in d:
			print(str(id)+','+l[0]+','+str(l[1]), file=out_file)
			id += 1
except IOError:
	print('File error..')