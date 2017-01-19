from django.db import models

# Create your models here.
class Example(models.Model):
	"""练习表"""
	item = models.CharField(max_length=48)
	solution = models.TextField()
	
	def __str__(self):
		"""返回项目名"""
		return self.item