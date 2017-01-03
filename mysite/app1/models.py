from django.db import models
from django.utils import timezone

class Post(models.Model):
	author=models.ForeignKey('auth.User')
	title=models.CharField(max_length=200)
	akt_prawny=models.TextField()
	publikator=models.CharField(max_length=100)
	zakres_zmian=models.TextField()
	obowiazuje_od=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(default=timezone.now)
	
	
	def publish(self):
		self.published_date=timezone.now()
		self.save()
	
	def __str__(self):
		return self.title