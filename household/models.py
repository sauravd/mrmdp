from django.db import models
from django.contrib.gis.db import models

class househead(models.Model):
    fullname=models.CharField(max_length=250)
    photo=models.ImageField()
    tole=models.CharField(max_length=250)
    wardno=models.PositiveSmallIntegerField()
    location=models.PointField()
    address=models.CharField(max_length=250)
    phone=models.PositiveBigIntegerField()
    
