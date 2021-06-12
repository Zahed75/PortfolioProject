from django.conf.urls import url
from django.urls import path

from Portfolio_App import views

app_name = 'Portfolio_App'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.Contact.as_view(), name='contact'),

]
