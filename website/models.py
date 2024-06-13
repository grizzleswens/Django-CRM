from django.db import models

# Create your models here.
# Code will be the same regardless of db
# Need to make a migration and push it in to database when you add or change


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zipcode = models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")

