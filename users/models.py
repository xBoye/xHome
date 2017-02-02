from django.db import models

class Names(models.Model):
	"""作品人物名字表"""
	name = models.CharField('名字', max_length=10)
	alias = models.CharField('别名',max_length=20,null=True)
	textbook = models.CharField('出处', max_length=50)
	note = models.TextField('备注', null=True)
	
	def __str__(self):
		return self.name
		
