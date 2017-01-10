# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

@login_required
def just_a_try(request):
	"""试一试"""
	return render(request, 'try/try.html')	