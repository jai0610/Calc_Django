from calculator.views import calci, history, index, login, signout, signup
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('calculate/history/', history, name='history'),
    path('history/', history, name='history'),
    path('calculate/', calci, name='calci'),
    path('logout/',signout),
]