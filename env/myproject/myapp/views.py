from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from.forms import patientForm,departmentForm,doctorForm,appointmentForm
from.models import Patient,Doctor,Appointment,Department,Login
# Create your views here.
def signup(request):
    return HttpResponse("login Success")
def drmodule(request):
    return render(request,'drmodule.html')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def appoinment(request):
    return render(request,'appoinment.html')
def contact(request):
    return render(request,'contact.html')
def department(request):
    return render(request,'department.html')
def drlist(request):
    return render(request,'drlist.html')
def registration(request):
    return render(request,'registration.html')
def drregister(request):
    return render(request,'drregister.html')
def login(request):
    return render(request,'login.html')
def deptregistration(request):
    return render(request,'deptregistration.html')
def adminmodule(request):
    return render(request,'adminmodule.html')
def adminmodule(request):
    return render(request,'adminmodule.html')
def viewpatient(request):
    return render(request,'viewpatient.html')
def usermodule(request):
    return render(request,'usermodule.html')
def adminapprove(request):
    return HttpResponse("<h2>Your Appoinment is Approved</h2>")



# Create your views here.

def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                #messages.info(request,"username taken")
                return redirect('registration')
                user = User.objects.create_user(username=username,password=password)
                user.save()
                print("user created")
        else:
            print("password not matched")
            return redirect('registration')
        return render(request,'index.html')
    else:
        return render(request,'registration.html')


def doctorregistration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                # messages.info(request,"username taken")
                return redirect('doctorregistration')
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("user created")
        else:
            print("password not matched")
            return redirect('doctorregistration')
        return render(request, 'home.html')
    else:
        return render(request, 'doctorregistration.html')

def appoinment(request):
    if request.method == "POST":
        form = appointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = appointmentForm()
    return render(request, 'appoinment.html')

def deptregistration(request):
    if request.method == "POST":
        form = departmentForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'index.html')
    else:
        form = departmentForm()
    return render(request, 'deptregistration.html')

def LoginFrm(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form['username'].valid()
            password=form['password'].valid()
            try:
                user=Login.objects.get(username=username,password=password)
                if user is not None:
                    return render(request,'index.html')
            except:
               pass
    else:
        return render(request, 'LoginFrm.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=Patient.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'usermodule.html')
            return render(request, 'login.html')
        except:
             pass
        try:
           user=Login.objects.get(username=username,password=password)
           if user is not None:
               print(user)
               return render(request, 'index.html')
           #return render(request,'Adminmodule.html')
        except:
            pass

        try:
            user=Doctor.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'drmodule.html')
            return render(request,'login.html')
        except:
             pass
    else:
        return render(request,'login.html')

