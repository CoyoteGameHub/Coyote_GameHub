from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

from . import views
urlpatterns = [

    url(r'^$', views.index, name ='index'),
    url(r'^auth/', views.login_and_auth, name ='login_and_auth'),
    url(r'^signup/', views.signup_user, name ='signup_user'),
    

]
