# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def algorithm(request):
	"""区块链blockchain"""
	return render(request, 'algorithm/algorithm.html')
	
def blackholenumbers(request):
	"""黑洞数blackholenumbers"""
	context = {'blackholenumber':'黑洞数'}
	return render(request, 'algorithm/blackholenumbers.html', context)
	
def findblackholenumbers(request):
	"""寻找黑洞数"""
	if request.method == 'POST':
		n = int(request.POST['figures'])
	start = 10**(n-1)
	end = 10**n
	#依次测试每个数
	black_hole_numbers = []
	for i in range(start, end):
		#由这几个数字组成的最大数和最小数
		big = ''.join(sorted(str(i),reverse=True))
		little = ''.join(reversed(big))
		big, little = map(int,(big, little))
		if big-little == i:
			black_hole_numbers.append(i)
	print(n,'位黑洞数：',black_hole_numbers)
	
	title = '%d位黑洞数' %(n)
	context = {'title':title, 'black_hole_numbers':black_hole_numbers}
	return render(request, 'algorithm/blackholenumbers.html', context)