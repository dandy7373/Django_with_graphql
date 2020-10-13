from django.contrib import admin
from django.urls import path, include
from . import views
from userprofile import views
from django.conf.urls import url
# SET THE NAMESPACE!
app_name = 'userprofile'
urlpatterns = [
    #path('',views.userprofile,name='userprofile'),
    
# Be careful setting the name to just /login use userlogin instead!

    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    


]