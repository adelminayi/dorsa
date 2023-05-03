from django.db import models

# Create your models here.
class AddValues(models.Model):
    avalue = models.IntegerField()
    bvalue = models.IntegerField()
    sumvalue = models.IntegerField()

    def __str__(self):
        return str(self.avalue) + ' + ' + str(self.bvalue)