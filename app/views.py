from django.contrib.auth import login, logout, authenticate ,get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required


@never_cache
def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == 'POST':
        role = request.POST['role']
        firstname = request.POST['fname'] #
        email = request.POST['email'] #
        lastname = request.POST['lname'] 
        dob = request.POST['dob'] #
        password = request.POST['password']
        user = Usertable(first_name=firstname,last_name=lastname,role=role,dob=dob,email=email)
        user.set_password(password)
        user.save()
        return redirect('user_login')
    return render(request,"registration.html")


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index2')
        else:
            error_message = "Invalid credentials"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, "login.html")
    
def userLogout(request):
    logout(request)
    return redirect('index')

@login_required
def index2(request):
    return render(request, "index2.html")




# @login_required
# def index2(request):
#     return render(request, "index2.html")

# def about(request):
#     return render(request, "about.html")
# def contact(request):
#     return render(request,"contact.html")

def check_user_exists(request):
    email = request.GET.get('email')  # You can also use 'email' if you're checking by email
    data = {
        'exists': Usertable.objects.filter(email=email).exists()
    }
    return JsonResponse(data)

# def forgotPassword(request):
#     return HttpResponse("I HAVE ")

def adminreg(request):
    # Query all User objects (using the custom user model) from the database
    User = get_user_model()
    user_profiles = User.objects.all()
    
    # Pass the data to the template
    context = {'user_profiles': user_profiles}
    
    # Render the HTML template
    return render(request, 'adminreg.html', context)