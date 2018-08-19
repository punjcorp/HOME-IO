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


class IOSwitchGroup(models.Model):
    io_group_id = models.IntegerField()
    icon = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    io_switches = models.ManyToManyField(IOSwitch)

    def __str__(self):
        return self.name


class IOSwitchActivity(models.Model):
    io_activity_id = models.IntegerField()
    action_code = models.CharField(max_length=20)
    action_date = models.DateTimeField('date of action')
    action_by = models.CharField(max_length=50)
    io_switches = models.ManyToManyField(IOSwitch)

    def __str__(self):
        return self.name
