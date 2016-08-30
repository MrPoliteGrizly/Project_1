from django.db import models

# Create your models here.
class Subject(models.Model):
	sub = models.CharField(max_length=200)
	sub_text = models.TextField(default='')
	sub_pub = models.DateTimeField("date published")
	# list_display = ('sub', 'sub_text', 'sub_pub')
	def __str__(self):
		return self.sub