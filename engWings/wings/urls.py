

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('about',views.about, name='about'),
    path('content/<int:course_id>',views.content, name='content'),
    path('contact',views.contact, name='contact'),
    path('contactform',views.contactform, name='contactform'),
    path('front/<int:id>/<int:course_id>',views.front,name='front'),
    path('courses',views.courses, name='courses'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name='logout'),

]
