from django.http import HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import RegistrationForm

from .models import Car

class IndexView(generic.ListView):
  template_name = 'cars/index.html'
  context_object_name = 'latest_car_list'
  
  def get_queryset(self):
    return Car.objects.filter(user=self.request.user).order_by('year')

class DetailView(LoginRequiredMixin, generic.DetailView):
  model = Car
  template_name = 'cars/detail.html'

class DeleteView(generic.DeleteView):
  model = Car
  success_url = "/cars/"

class CarNew(CreateView):
  model = Car
  fields = '__all__'

def register(request):
  if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
          form.save()
          username = form.cleaned_data.get('username')
          raw_password = form.cleaned_data.get('password1')
          user = authenticate(username=username, password=raw_password)
          login(request, user)
          return redirect('/cars/')
  else:
      form = RegistrationForm()
  return render(request, 'accounts/register.html', {'form': form})

def home_index(request):
  user_cars = Car.objects.filter(user=request.user).order_by('year')
  return render(request, 'cars/home_index.html', context={'user_cars': user_cars})
  
