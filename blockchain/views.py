# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def blockchain(request):
	"""区块链blockchain"""
	return render(request, 'blockchain/blockchain.html')	
	
