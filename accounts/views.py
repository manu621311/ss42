from django.shortcuts import render
from .forms import SignForm
from accounts.models import signupModel
# Create your views here.
def signuppage(request):
    return render(request,'register.html',{'data':SignForm()})


def saveregistrationdetails(request):
    uname = request.POST.get('username')
    email = request.POST.get('email')
    upass = request.POST.get('password')
    upass2 = request.POST.get('password2')
    signupModel(username=uname,email=email,password=upass,password2=upass2).save()
    return render(request,'register.html',{'message':'register succssfully'})
