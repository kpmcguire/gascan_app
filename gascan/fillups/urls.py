from django.urls import path

from . import views

app_name = 'fillups'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('new/', views.fillup_new, name='fillup_new'),
]

