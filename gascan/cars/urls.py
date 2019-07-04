from django.urls import path

from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('new/', views.CarNew.as_view(), name='car_new'),
    # path('register/', views.register, name='register'),
]
