from django.urls import path
from . import views

app_name = 'Password_Generator_App'

urlpatterns = [
    path('', views.home, name='home'),
]
