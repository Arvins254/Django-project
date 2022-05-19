from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	published_date = models.DateTimeField("date published")


	def __str__(self):
		return self.title
