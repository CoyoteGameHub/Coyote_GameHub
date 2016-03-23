from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

from . import views
urlpatterns = [

    url(r'^$', views.index, name ='index'),
    url(r'^auth/', views.login_and_auth, name ='login_and_auth'),
    url(r'^signup/', views.signup_user, name ='signup_user'),
    url(r'^login/', views.loginview, name ='loginview'),
    url(r'^game1/', views.game_one, name = 'game_one'),
    url(r'^logout/', views.log_out, name = 'log_out'),
    url(r'^game2/', views.game_one, name = 'game_two'),
    url(r'^game3/', views.game_one, name = 'game_three'),


]
