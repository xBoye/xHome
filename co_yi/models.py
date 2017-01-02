from django.db import models

class Yi(models.Model):
	"""周易64卦模式"""
	gname = models.CharField('卦名', max_length=8)
	gci = models.TextField('卦辞')
	xci = models.TextField('象辞')
	tci = models.TextField('彖辞')
	y1 = models.CharField('初爻', max_length=50)
	x1 = models.CharField('初爻小象', max_length=50)
	y2 = models.CharField('二爻', max_length=50)
	x2 = models.CharField('二爻小象', max_length=50)
	y3 = models.CharField('三爻', max_length=50)
	x3 = models.CharField('三爻小象', max_length=50)
	y4 = models.CharField('四爻', max_length=50)
	x4 = models.CharField('四爻小象', max_length=50)
	y5 = models.CharField('五爻', max_length=50)
	x5 = models.CharField('五爻小象', max_length=50)
	y6 = models.CharField('上爻', max_length=50)
	x6 = models.CharField('上爻小象', max_length=50)
	yy = models.CharField('用爻', max_length=50, null=True)
	xx = models.CharField('用爻小象', max_length=50, null=True)
	wenyan = models.TextField('文言', blank=True, null=True)
	gbin = models.CharField('二进制卦序', max_length=6)

	def __str__(self):
		return self.gname
		
class Yilin(models.Model):
	"""焦氏易林4096卦模式"""
	yi = models.ForeignKey(Yi)	
	jname = models.CharField('易林卦名', max_length=10)
	jci = models.TextField('易林卦辞', blank=True, null=True)
	
	class Meta:
		verbose_name_plural = 'yilins'
	
	def __str__(self):
		return self.jname