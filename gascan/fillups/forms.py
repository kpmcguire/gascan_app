import datetime
from django import forms
from .models import Fillup
from cars.models import Car

class FillupForm(forms.ModelForm):
  class Meta:
    model = Fillup
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user')
    super(FillupForm, self).__init__(*args, **kwargs)
    self.fields['car'].queryset = Car.objects.filter(user=user)
  

