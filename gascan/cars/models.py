from django.db import models
from fillups.models import Fillup
import itertools
from django.contrib.auth.models import User

class Car(models.Model):
  name = models.CharField(max_length=256)
  make = models.CharField(max_length=256)
  model = models.CharField(max_length=256)
  year = models.IntegerField(default=0)
  starting_odometer = models.DecimalField(max_digits=20, decimal_places=1, default=0)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return u'/cars/%d' % self.id 

  @property
  def avg_mileage(self):
    fillups = Fillup.objects.filter(car=self)
    if fillups.count() > 0:
      return sum(fillup.mpg for fillup in fillups) / fillups.count()

