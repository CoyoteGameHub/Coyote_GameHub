from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'home/index.html')

def login_and_auth(request, onsuccess='/userprofile/', onfail='/#login/'):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            redirect(onsuccess)
        else:
            redirect(onfail)
    else:
        redirect(onfail)

def signup_user(request):
    post = request.POST
    if user_exists(post['email']): 
        return redirect("/#login/")
    else:
        user = create_user(username=post['email'], email=post['email'], password=post['password'], name=post['name'])
        return login_and_auth(request)


def user_exists(username):
    user_count = User.objects.filter(username=username).count()
    if user_count == 0:
        return False
    return True

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user
