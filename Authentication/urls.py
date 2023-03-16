from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login),
    path('home', views.login_view,name='home'),
    path('abc/',views.precess,name='precess'),
    path('check_username/', views.check_username, name='check_username'),
    path('check_email/', views.check_email, name='check_email'),
    path('login/', views.signin, name='Login'),
    path('', views.Login, name='SignUp'),
]