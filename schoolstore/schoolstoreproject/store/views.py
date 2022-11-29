from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import Student_Form
from .models import Department,Course
from django.template import RequestContext




# Create your views here.
def index(request):
    return render(request,'index.html')

def order(request):
    form = Student_Form()
    if request.method == 'POST':
        form=Student_Form(request.POST)
        if form.is_valid():
            messages.success(request, "your order is place")
            form.save()
            return redirect('/')
    return render(request, 'home.html' , {'form':form})

def load_department(request):
    id = request.GET.get('id')
    department = Department.objects.filter(id=id).all()

    return render(request, 'department.html', {'department':department})


def load_course(request):
    department_id = request.GET.get('Department')
    course = Course.objects.filter(department_id=department_id).all()
    return render(request, 'coursedropdown.html', {'course': course})





# Create your views here.
def register(request):
    if request.method=='POST':
        u1=request.POST['username']
        f1= request.POST['firstname']
        l1 = request.POST['lastname']
        g1 = request.POST['email']
        p1 = request.POST['password']
        c1 = request.POST['cpassword']
        if p1==c1:
            if User.objects.filter(username=u1).exists():
              messages.info(request,"already used username")
              return redirect('register')
            elif User.objects.filter(email=g1).exists():
              messages.info(request,"already used email")
              return redirect('register')
            else:
                user=User.objects.create_user(username=u1,first_name=f1,last_name=l1,email=g1,password=p1)
                user.save();


        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def newform(request):
    return render(request,'newform.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('newform')
        else:
            messages.info(request, "Invalid")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')





