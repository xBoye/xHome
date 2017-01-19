# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from utest.models import Example

def utest(request):
	"""单元测试"""
	import os, re

	fin = "d:\\xhome\\data\\text_mining\\禅诗.txt"
	fout = "d:\\xhome\\data\\out_file\\禅诗_results.csv"
	book=os.path.split(fin)[1].split('.')[0]   #书名

	repl = '[，：。？∶:;！（）、=《》’‘“\'"\r\n\s )ばhＮB0℃zＧｎｂｄｃ□ｊｔYoｙt／_Ａp@ -Luｌ；bｕ·yie．dｅ３a「２nF,＠Ｖｋ＜＞ｒｐｉ【】『』ｇｏjａ/2┦ｘ\sZ(＝（）ｖΥw”TW○乙－Ｔ￣１Ｑ８Ｓ０s,r＂Ｆ─]'

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

	results = book + '总字数为：' + str(sum(list((d.values())))) + '；不重复字数为：'+str(len(d)) + '\r\n序号,字名,出现次数'
	
	d=sorted(d.items(),key=lambda a:a[1],reverse=True)
	id = 1
	for l in d[1:11]:
		results = results + '\r\n' + str(id)+','+l[0]+','+str(l[1])
		id += 1

	e = Example(item=book, solution=results)
	e.save()	
	
	examples = Example.objects.all()
	return render_to_response('utest/utest.html', {'examples':examples})

	
	