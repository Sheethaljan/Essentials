from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from ssapp.forms import DetailsForm
from ssapp.models import Course


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('new_page/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        cpassword = request.POST.get('password1', '').strip()
        if not username or not password or not cpassword:
            messages.info(request, 'Please fill all the fields')
            return redirect('/register')
        elif password != cpassword:
            messages.info(request, 'Password does not match')
            return redirect('/register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already used')
            return redirect('/register')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('/login')
    else:
        return render(request, 'register.html')


def new_page(request):
    return render(request, 'new_page.html')




def student_details(request):
    form = DetailsForm()
    courses = Course.objects.all()
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success/')
    return render(request, 'form.html', {'form': form, 'courses': courses})


def load_courses(request):
    department_id = request.GET.get('department_id')
    courcess = Course.objects.filter(department_id=department_id).order_by('course')
    return render(request, 'course_dropdown_list_options.html', {'courcess': courcess})


def success(request):
    return render(request, 'success.html')



def logout(request):
    auth.logout(request)
    return redirect('/')



