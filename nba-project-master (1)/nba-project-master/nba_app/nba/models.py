from django.db import models

# Create your models here.

class Team(models.Model):
	teamId = models.CharField(primary_key=True, max_length=30)
	city = models.CharField(max_length=30)
	full_name = models.CharField(max_length=30)
	nickname = models.CharField(max_length=30)
	tricode = models.CharField(max_length=3)
	conference = models.CharField(max_length=30)
	divison = models.CharField(max_length=30)



#Player belongs to a Team
class Player(models.Model):
	playerId = models.CharField(primary_key=True, max_length=30)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	jersey = models.IntegerField()
	height = models.CharField(max_length=30)
	weight = models.FloatField()
	position = models.CharField(max_length=5)
	





