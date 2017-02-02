from django.db import models

# Create your models here.
class Words(models.Model):
	"""文本汉字库"""
	name = models.CharField('字',max_length=2)
	degrees = models.IntegerField('字频')
	textbook = models.CharField('文本',max_length=50)
	
	def __str__(self):
		"""返回汉字名"""
		return self.name
		
class Phrases(models.Model):
	"""词组库"""
	name = models.CharField('词组',max_length=10)
	degrees = models.IntegerField('词频')
	textbook = models.CharField('词频',max_length=50)
	
	def __str__(self):
		"""返回汉字名"""
		return self.name
		
class Results(models.Model):
	"""分析结果"""
	textbook = models.CharField('文本',max_length=50)
	summary = models.TextField('结果')
	
	def __str__(self):
		"""返回项目名"""
		return self.textbook

class Names(models.Model):
	"""人物库"""
	name = models.CharField('名字',max_length=10)
	degrees = models.IntegerField('出现频率',null=True)
	textbook = models.CharField('文本',max_length=50)
	alias = models.CharField('别名',max_length=20,null=True)
	note = models.TextField('备注',null=True)