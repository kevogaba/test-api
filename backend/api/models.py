from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Table for Annual Summarised Data
class Accomplishment(models.Model):
    title = models.CharField(max_length=50)
    accomplishment = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, default=User)
    
    def __str__(self) -> str:
        return self.accomplishment


# Table for Indicator
class Indicator(models.Model):
    accomplishment = models.ForeignKey('Accomplishment', related_name='indicators', on_delete=models.CASCADE)
    name = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, default=User)
    
    def __str__(self) -> str:
        return self.name


# Quantitative data for all units of measurement perfomance quarterly for a year
class Measurement(models.Model):
    indicator = models.ForeignKey('Indicator', related_name='measurements', on_delete=models.CASCADE)
    name = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, default=User)

    class Meta:
        db_table = "Units of Measurements"
    def __str__(self) -> str:
        return self.name


class Baseline(models.Model):
    measurement = models.ForeignKey('Measurement', related_name='baselines', on_delete=models.CASCADE)
    items = models.TextField()
    count = models.IntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, default=User)

    def __str__(self) -> str:
        return self.count


# Detailed quarterly data per unit of measurement
class Quarter(models.Model):
    class Status(models.TextChoices):
        Validated = 'Validated'
        Not_validated = 'Not validated'
        Work_in_progress = 'Work in Progress'
        Pending = 'Pending'
    title = models.CharField(max_length=50)
    unit = models.ForeignKey('Measurement', related_name='quarters', on_delete=models.CASCADE)
    items = models.TextField()
    progress = models.CharField(max_length=256)
    sub_programme_status = models.TextField(choices=Status.choices)
    ppd_validation_status = models.TextField(choices=Status.choices)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, default=User)
    
    class Meta:
        db_table = "Quarterly Raw Data"

    def __str__(self) -> str:
        return self.title
    '''
    def cumulative_items(self):
        baseline = Baseline.objects.filter(Measurement_Unit=self.unit)
        previous = self.Previous_Count
        current = self.Number_of_Items
        if previous==0:
            return baseline + current
        else:
            return previous + current

    def target(self, instance):
        previous_target = Quarter.objects.filter(target=instance.target).exclude(id=instance.id).last()
        target = Target.objects.filter(Quarter=self.Quarter)
        baseline = Baseline.objects.filter(Measurement_Unit=self.Measurement_Unit)
        if previous_target:
            return previous_target + target
        else:
            return baseline + target

    def percentage(self):
        target = self.target()
        actual = self.cumulative_items()
        percent = (target/actual)*100
        return f"{percent}"
    '''


class Target(models.Model):
    quarter = models.ForeignKey('Quarter', related_name='targets', on_delete=models.CASCADE)
    target = models.IntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, default=User)

    def __str__(self) -> str:
        return self.target