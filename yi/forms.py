# -*- coding: utf-8 -*-
from django.forms import ModelForm, ValidationError

from .models import Yi, Yilin

class YiForm(ModelForm):
	class Meta:
		model = Yi
		fields = '__all__'

class YilinForm(ModelForm):  
    class Meta:  
        model = Yilin
        fields = '__all__'  
