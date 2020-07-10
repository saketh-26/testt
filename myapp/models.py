from django.db import models

# Create your models here.

class TitanicPrediction(models.Model):
	GENDER = [('M','Male'),('F','Female')]
	PLACES = [('queenstown','queenstown'),('southampton','southampton'),('cherbourg','cherbourg')]

	class CLASS(models.IntegerChoices):
		Class1 = 1
		Class2 = 2
		Class3 = 3
	age = models.FloatField()
	sibsp = models.IntegerField()
	parch = models.IntegerField()
	fare = models.FloatField()
	gender = models.CharField(max_length = 10,choices=GENDER)
	pclass = models.IntegerField(choices = CLASS.choices)
	place = models.CharField(max_length = 50,choices=PLACES)
