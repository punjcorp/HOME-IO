from django.db import models

# Create your models here.


class IOSwitch(models.Model):
    outlet_id = models.IntegerField()
    icon = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    state = models.BooleanField(
        'tells the switch state true for ON and false for OFF')

    def __str__(self):
        return self.name
