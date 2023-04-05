from django.db import models

# Create your models here.
class Topic(models.Model):
    sno = models.IntegerField()
    topic_name=models.CharField(max_length=25, primary_key=True)

class Webpages(models.Model):
    topic_name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    player_ID=models.IntegerField(primary_key=True)
    player_name=models.CharField(max_length=30)

class About(models.Model):
    player_name=models.ForeignKey(Webpages, on_delete=models.CASCADE)
    Jersey_No=models.IntegerField(primary_key=True)
    country=models.CharField(max_length=25)  
