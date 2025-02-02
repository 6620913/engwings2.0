from django.shortcuts import render,redirect
# from sklearn.metrics import mean_gamma_deviance
from .models import Videos,Courses
# contactform
import os
import smtplib
# import imghdr
from email.message import EmailMessage



# for login register logut features.
from django.contrib.auth.models import User,auth
from django.contrib import messages

# --------------------------------------------








# Create your views here.
def index(request):
    front = Videos.objects.get(course_id=0)

    return render(request,'index.html',{"front":front})

#return about page
def about(request):


    return render(request,'about.html')

#return content page
def content(request,course_id):
    if request.user.is_authenticated:

        content = Videos.objects.filter(course_id=course_id).order_by("cvs")
        front = content[0]
        ctitle = Courses.objects.get(course_id=course_id)


        return render(request,'content.html',{"content":content,"front":front,"ctitle":ctitle})
    else:
        return redirect("login")


#return contact page
def contact(request):


    return render(request,'contact.html')

def front(request,id,course_id):
    if request.user.is_authenticated:

        content = Videos.objects.filter(course_id=course_id).order_by("cvs")
        front = Videos.objects.get(id=id)
        ctitle = Courses.objects.get(course_id=course_id)


        return render(request,'content.html',{"content":content,"front":front,"ctitle":ctitle})
    else:
        return redirect("login")



def contactform(request):



    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    email = request.POST['email']
    phone_number=request.POST['phone_number']
    mg = request.POST['message']


    EMAIL_ADDRESS = 'nerthinksjareen@gmail.com'
    EMAIL_PASSWORD = 'I will eat sahi paneer today'

    msg = EmailMessage()
    msg['Subject'] = 'contacting'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    msg.set_content(f"Contacting: {email}\n Phone: {phone_number}\n : {first_name} {last_name}\n message: {mg} ")



    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


    return render(request,'contact.html')

# return courses page with courses data
def courses(request):
    courses = Courses.objects.all()


    return render(request,'courses.html',{"courses":courses})



'''
login, register, logout features

'''

def login(request):
    if request.user.is_authenticated==False:

        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect("/")
            else:
                messages.info(request,"invalid credentials")
                return redirect("login")

        else:
            return render(request,"login.html")
    else:
        return redirect("/")

def register(request):
    if request.user.is_authenticated==False:



        if request.method=="POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if(password1!=password2):
                print("password not match")
                messages.info(request,"password not match")
                return redirect("register")
            elif(User.objects.filter(username=username).exists()):
                messages.info(request,"Username taken")
                return redirect("register")

            elif (User.objects.filter(email=email).exists()):
                messages.info(request,"email already registerd")
                return redirect("register")
            elif ("@" not in email):
                messages.info(request,"invalid email")
                return redirect("register")

            else:

                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                messages.info(request,"You are registerd now")
                user.save()
                return redirect("login")
        else:
            return render(request,'register.html')
    else:
        return redirect("/")

def logout(request):
    auth.logout(request)
    return redirect('/')