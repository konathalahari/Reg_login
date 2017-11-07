from django.shortcuts import render
from django.http import HttpResponse
from .forms import regform,login
from .models import *

def reg(request):
    if request.method=='POST':
        form=regform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registration Successful')
        else:
            print(form.errors)
            return HttpResponse('Error occured')
    else:
        form=regform()
        return render(request,'reg.html',{'form':form})

def log(request):
    if request.method=="POST":
        myform=login(request.POST)
        if myform.is_valid():
           my=myform.cleaned_data['myuser']
           pd=myform.cleaned_data['pwd']
           p=Reg.objects.filter(myuser=my,pwd=pd)
           if p:
            return HttpResponse('login succedd')
           else:
            return HttpResponse('login failed')
    else:
        log=login()
        return render(request,'login.html',{'log':log})
def link(request):
     return render(request,'links.html')