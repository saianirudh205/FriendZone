from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.
def Login(request):


    return render(request,'login.html',{'first':'True','button':'SignUp','Click':'Login','const':'Email','pass':'precess'})

@csrf_protect
def precess(request):
    if request.method=='POST' :

        username,l_name,email,password=request.POST['f_name'],request.POST['l_name'],request.POST['email'],request.POST['password']

        user=User(username=username,last_name=l_name,email=email,password=password)
        user.save()

    return render(request,'login.html',{'first':'','button':'Login','Click':'SignUp','const':'Email'})



def check_username(request):
    #print(request.GET)
    if request.method == 'GET':
        username = request.GET['username']

        if User.objects.filter(username=username).exists():
            data = {'is_taken': True}
        else:
            data = {'is_taken': False}
        return JsonResponse(data)

def check_email(request):
    print(request.GET)
    if request.method == 'GET':
        email = request.GET['email']
        #username=username.replace(' ','_')
        if '@' not in email:
            data={'result':'Not Valid'}
        elif User.objects.filter(email=email).exists():
            data={'result':'Email already taken'}
        else:
            data={'result':'Cool'}
        return JsonResponse(data)


def signin(request):

    return render(request,'login.html',{'first':False,'button':'Login','Click':'SignUp','const':'Email','pass':'home'})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=username, password=password)
        print(user)
        if user is not None:
            return HttpResponse('YEAY')
        else:
            return Login(request,error="User name or Password didnt match")
    return render(request, 'login.html')
