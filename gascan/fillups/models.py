from django.db import models

class Fillup(models.Model):

  class Meta:
      verbose_name_plural = "fillups"

  car = models.ForeignKey('cars.Car', on_delete=models.CASCADE, default=1)
  fillup_date = models.DateTimeField()
  odometer = models.DecimalField(max_digits=20, decimal_places=1)
  gas_gallons = models.DecimalField(max_digits=5, decimal_places=3)
  latitude = models.DecimalField(
      max_digits=12, decimal_places=8, null=True, blank=True)
  longitude = models.DecimalField(
      max_digits=12, decimal_places=8, null=True, blank=True)
  
  def __str__(self):
    return self.fillup_date.strftime('%b %-d, %Y')
  
  def get_absolute_url(self):
    return u'/fillups/%d' % self.id 
  
  @property
  def miles_driven(self):
    try:
      prev = self.get_previous_by_fillup_date(car=self.car)
      previous_value = prev.odometer
    except:
      previous_value = self.car.starting_odometer
    return self.odometer - previous_value

  @property
  def mpg(self):
    return self.miles_driven / self.gas_gallons 
