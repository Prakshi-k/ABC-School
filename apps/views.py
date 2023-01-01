from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import signupform
from .models import student,contactnow,kindergarten
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def vehicle(request):
    return render(request,'vehicle.html')

def teacher(request):
    return render(request,'teacher.html')       

def contact(request):
    return render(request,'contact.html')

def signup(request):
    return render(request,'signup.html')         


def register(request):
    if request.method=='POST':
        fm=signupform(request.POST)
        if fm.is_valid():
            fm.save()              
    else:
        fm=signupform()
    return render(request,'signup.html',{'form':fm})


# ----------------------------------------------------------------------

def user_login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            u=authenticate(username=uname,password=upass)
            # print(u)
            if u is not None:
                login(request,u)
                return redirect('/profile')

    
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'form':fm})


def user_profile(request):
    return render(request,'profile.html')



def user_logout(request):
    logout(request)
    return redirect('/login')

# ----------------------------------------------------------------------------------



def contactnow_form(request):
    if request.method=='POST':
        a=request.POST['name']
        b=request.POST['phone_number']
        c=request.POST['email']
        d=request.POST['message']

    c1=contactnow.object.create(name=a,phone_number=b,email=c,message=d)
        
    c1.save()

    return redirect('/')

# --------------------------------------------------------------------------------------------

def get_student_primary(request):
    content={}

    q1=Q(std=1)
    q2=Q(std=2)
    q3=Q(std=3)
    q4=Q(std=4)
    content['data']=student.stud_manager.filter(q1|q2|q3|q4)
    return render(request,'student_rec_p.html',content)


def get_student_secondary(request):
    content={}

    q5=Q(std=5)
    q6=Q(std=6)
    q7=Q(std=7)
    q8=Q(std=8)
    q9=Q(std=9)
    q10=Q(std=10)
    content['data']=student.objects.filter(q5|q6|q7|q8|q9|q10)

    return render(request,'student_rec_s.html',content)

def get_student_kindergarten(request):
    content={}

    content['data']=kindergarten.object_kg.all()

    return render(request,'student_rec_kg.html',content)




# -----------------------------------------------------------------------------


def juniorkg_std(request):
    content={}
    content['data']=kindergarten.object_kg.filter(section="Jr")
    return render(request,'student_rec_kg.html',content)

def seniorkg_std(request):
    content={}
    content['data']=kindergarten.object_kg.filter(section="Sr")
    return render(request,'student_rec_kg.html',content)


# -------------------------------------------------------------------

def first_std(request):
    content={}
    content['data']=student.objects.filter(std=1)
    return render(request,'student_rec_p.html',content)

def second_std(request):
    content={}
    content['data']=student.objects.filter(std=2)
    return render(request,'student_rec_p.html',content)

def third_std(request):
    content={}
    content['data']=student.objects.filter(std=3)
    return render(request,'student_rec_p.html',content)

def fourth_std(request):
    content={}
    content['data']=student.objects.filter(std=4)
    return render(request,'student_rec_p.html',content)

def fifth_std(request):
    content={}
    content['data']=student.objects.filter(std=5)
    return render(request,'student_rec_s.html',content)

def sixth_std(request):
    content={}
    content['data']=student.objects.filter(std=6)
    return render(request,'student_rec_s.html',content)

def seventh_std(request):
    content={}
    content['data']=student.objects.filter(std=7)
    return render(request,'student_rec_s.html',content)

def eighth_std(request):
    content={}
    content['data']=student.objects.filter(std=8)
    return render(request,'student_rec_s.html',content)

def ninth_std(request):
    content={}
    content['data']=student.objects.filter(std=9)
    return render(request,'student_rec_s.html',content)

def tenth_std(request):
    content={}
    content['data']=student.objects.filter(std=10)
    return render(request,'student_rec_s.html',content)


# ---------------------------------------------------------------------------------------------


def user_login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            u=authenticate(username=uname,password=upass)
            # print(u)
            if u is not None:
                login(request,u)
                return redirect('/profile')

    
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'form':fm})

