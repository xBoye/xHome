# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def centres(request):
	#Python��ϰ��Ŀ��������Center
	return render(request, 'centres/centres.html')