from django.template.context_processors import csrf
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def loginview(request, onsuccess='/', onfail='home/index.html'):
    if request.user.is_authenticated():
        return redirect(onsuccess)
    else:
        c = {}
        c.update(csrf(request))
        return render_to_response(onfail, c)

@login_required(login_url='/login/', redirect_field_name=None)
def index(request):
    return render(request, 'home/userprofile.html')

def login_and_auth(request, onsuccess='/', onfail='/login/', onwtf='/#dailydeals'):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(onsuccess)
        else:
            return redirect(onwtf)
        
    else:
        return redirect(onfail)

def signup_user(request, userexists="/login/"):
    post = request.POST
    if not user_exists(post['email']): 
        user = create_user(username=post['email'], email=post['email'], password=post['password'])
        return login_and_auth(request)
    else:
        return redirect(userexists)



def user_exists(username):
    if User.objects.filter(username=username).exists():
        return True

    return False

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

@login_required(login_url='/login/', redirect_field_name=None)
def game_one(request):
    return render(request, 'home/game1.html')

@login_required(login_url='/login/', redirect_field_name=None)
def game_two(request):
    return render(request, 'home/game1.html')

@login_required(login_url='/login/', redirect_field_name=None)
def game_three(request):
    return render(request, 'home/game1.html')

def log_out(request, onlogout='/'):
    logout(request)
    return redirect(onlogout)
