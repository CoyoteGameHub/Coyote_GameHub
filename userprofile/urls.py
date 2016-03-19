from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'userprofile'

from . import views
urlpatterns = [
    url(r'^userprofile', views.index, name ='index'),  
]
