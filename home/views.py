from django.template.context_processors import csrf
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    return render(request, 'home/index.html')

def login_and_auth(request, onsuccess='/userprofile/', onfail='/#logins/'):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None:
        # if user.is_active:
        #     login(request, user)
        #     return redirect(onsuccess)
        # else:
        #     return redirect(onfail)
        login(request, user)
        return redirect(onsuccess)
    else:
        return redirect(onfail)

def signup_user(request, userexists="/#login/"):
    post = request.POST
    user = create_user(username=post['email'], email=post['email'], password=post['password'])
    return login_and_auth(request)
    # if not user_exists(post['email']): 
    #     user = create_user(username=post['email'], email=post['email'], password=post['password'])
    #     return login_and_auth(request)
    # else:
    #     return redirect(userexists)



def user_exists(username):
    if User.objects.filter(username=username).exists():
        return True

    return False

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user
