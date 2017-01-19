from django.db import models

# Create your models here.
class Words(models.Model):
	"""文本汉字库"""
	name = models.CharField(max_length=2)
	degrees = models.IntegerField()
	fromtext = models.CharField(max_length=20)
	
	def __str__(self):
		"""返回汉字名"""
		return self.name
		
class Results(models.Model):
	"""分析结果"""
	item = models.CharField(max_length=20)
	summary = models.TextField()
	
	def __str__(self):
		"""返回项目名"""
		return self.item