from django.db import models

# Create your models here.
class Userdata(models.Model):
    userId = models.IntegerField(default=0)
    id = models.IntegerField(default=0,primary_key=True)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.title