from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
# Changing the name of newsibject  to headline 

    def __str__(self):
        return self.headline
