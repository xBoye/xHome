from django.db import models

# Create your models here.
class Ksitiscry(models.Model):
	"""地藏占察189条"""
	kci = models.CharField(max_length=16)
	
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.kci