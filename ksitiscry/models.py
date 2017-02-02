from django.db import models

# Create your models here.
class Ksitiscry(models.Model):
	"""地藏占察189条"""
	kci = models.CharField(max_length=16)
	
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.kci
		
class Avalokiscry(models.Model):
	"""观音签100条"""
	signtype = models.CharField('上中下签',max_length=4)
	signmetaphor = models.CharField('签喻',max_length=12)
	signpoem = models.CharField('签诗',max_length=64)
	signotes = models.TextField('签释')
	
	
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.signmetaphor
