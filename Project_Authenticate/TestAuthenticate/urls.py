from django.urls import path
from . import views

app_name = 'TestAuthenticate' # if you are writing this in anchor tag <a> you have to write " name='' " of urls in html files

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='registerpage'),
    path('login/', views.login, name='loginpage'),
    path('logout/', views.logout_user, name='logout'),
]
