from django.urls import path
from .views import home

app_name = 'catalog'

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', home, name='contacts'),

]