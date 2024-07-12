from django.db import models

# Create your models here.

class Item(models.Model):
    dietType = models.CharField(max_length=200)
    dishName = models.CharField(max_length=200)
    dishDifficulty = models.CharField(max_length=200)
    dishBy = models.CharField(max_length=200)
    dishImage = models.CharField(max_length=200)
    step1 = models.CharField(max_length=200)
    step2 = models.CharField(max_length=200)
    step3 = models.CharField(max_length=200)
    step4 = models.CharField(max_length=200)
    step5 = models.CharField(max_length=200)
    step6 = models.CharField(max_length=200)
    step7 = models.CharField(max_length=200)
    step8 = models.CharField(max_length=200)
    step9 = models.CharField(max_length=200)
    step10 = models.CharField(max_length=200)
    userAdded = models.CharField(max_length=200)
    created= models.DateTimeField(auto_now_add=True)

