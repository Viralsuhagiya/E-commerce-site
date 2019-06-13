from django.shortcuts import render, redirect
from .models import News
from . forms import RegistrationForm,RegistrationModelForm
from .models import Registration
from django.contrib import messages
import cv2
import sys

# Create your views here.
def index(request):
    return  render(request,'my/home.html',{'posts':['post1','post2']})

def contact(request):
    context = {'contact': 'Viral suhagiya',
               'mylist': ['email-viralsuhagiya02@gmail.com','contact- 8490057085'],
               }
    return  render(request,'my/contact.html',context)

def about(request):
    context={}
    return render(request, 'my/about.html', context)

def news_details(request):
    obj = News.objects.get(id=1)
    context={
        'object':obj,
    }
    return render(request, 'my/news.html', context)

def news_years(request,year):
    a_list = News.objects.filter(pub_date__year = year)
    context={
        'year':year,
        'article_list':a_list,
    }
    return render(request, 'my/news_year.html', context)

def registration(request):
    context={
        "form":RegistrationForm,

    }
    return render(request, 'my/registration.html', context)

def addUser(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        register = Registration(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],
                                email=form.cleaned_data['email'],
                                phone=form.cleaned_data['phone'],
                                )
        register.save()
        messages.add_message(request, messages.SUCCESS,"You have registered successfully")
    return redirect('add')

def modelformview(request):
    context = {
        'modelform':RegistrationModelForm
    }
    return render(request, "my/modelform.html", context)

def addModeldata(request):
    mymodelform = RegistrationModelForm(request.POST)
    if mymodelform.is_valid():
        mymodelform.save()
        messages.add_message(request, messages.SUCCESS, "You have registered successfully")
    return redirect('addModelform')

def detect(request):
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # set Width
    cap.set(4, 480)  # set Height
    while (True):
        ret, frame = cap.read()
        frame = cv2.flip(frame, -1)  # Flip camera vertically
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)

        k = cv2.waitKey(30) & 0xff
        if k == 27:  # press 'ESC' to quit
            break
    cap.release()
    cv2.destroyAllWindows()
    return render(request, "my/modelform.html")