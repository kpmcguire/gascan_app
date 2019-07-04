from django import forms
import datetime

from django.http import HttpResponseRedirect
from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Fillup
from cars.models import Car
from .forms import FillupForm
from django.shortcuts import redirect

class IndexView(generic.ListView):
  template_name = 'fillups/index.html'
  context_object_name = 'fillup_list'

  def get_queryset(self):
    user_cars = Car.objects.filter(user=self.request.user)
    return Fillup.objects.filter(car__in=user_cars).order_by('fillup_date')

class DetailView(generic.DetailView):
  model = Fillup
  template_name = 'fillups/detail.html'

def fillup_new(request, *args, **kwargs):
  if request.method == 'POST':
    form = FillupForm(request.POST, user=request.user)
    if form.is_valid():
      form.save()
      return redirect('/fillups/')
  else:
    form = FillupForm(user=request.user, initial={'fillup_date': datetime.datetime.today})
  return render(request, 'fillups/fillup_form.html', {'form': form})



