from django.shortcuts import render, redirect
from .models import User, Restaurant, Bookings, Image
from .forms import AddUser, LogUser
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import re

def index(request):
    return render(request, 'main/index.html')
   
# @login_required
def home(request):
    restaurants = Restaurant.objects.all()
    data = []
    for restaurant in restaurants:   
        data.append({
            "id": restaurant.id,
            "name": restaurant.name,
            "description": restaurant.description,
            "rating": restaurant.rating,
            "address": restaurant.address,
            "cuisine": restaurant.cuisine,
            "phone": restaurant.phone,
            "email": restaurant.email,
            "image": str(list(Image.objects.filter(restaurant=restaurant))[0].image)[4:],
        })
    return render(request, 'main/home.html', {'data': data})

def profile(request):
    return render(request, 'main/profile.html')

def logout(request):
    auth_logout(request)
    return render(request, 'main/logout.html')
     
def details(request, pk):
    restaurant = Restaurant.objects.get(id=pk)
    context = {
        "name": restaurant.name,
        "description": restaurant.description,
        "rating": restaurant.rating,
        "address": restaurant.address,
        "cuisine": restaurant.cuisine,
        "phone": restaurant.phone,
        "email": restaurant.email,
        "images": [str(img.image)[4:] for img in Image.objects.filter(restaurant=restaurant)],
    }
    return render(request, 'main/details.html', context) 

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Authentication
        try:
            user = User.objects.get(username=username)
            if user.password != password:
                messages.error(request,'Invalid password')
                return redirect("/login")
        except User.DoesNotExist:
            user = None
        #If authentication is successful Login
        if user is not None:
            auth_login(request, user)
            messages.success(request, f"{username} Logged In Successfully!")
            return redirect("home")
        else:
            messages.error(request, "Cannot Log In!")
            return redirect("/login")
    return render(request, 'main/login.html')

def signup(request):
    if request.method == "POST":
        form = AddUser(request.POST)
        if form.is_valid():
            # Get user data from the form
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            confirm = form.cleaned_data['confirm']
            # Check if email is valid
            email_pattern = re.compile(r'[a-z0-9_./]+@{1}[a-z0-9#]+.[a-z0-9]{2,5}')
            if re.fullmatch(email_pattern, email):
                #Check whether the password is valid
                password_pattern = re.compile(r'[A-Za-z0-9~`!@#$%^&*()_+={[}]|\:;"\'<,>.?/]+')
                if password_pattern.search(password) and len(password) >= 8:
                    #Check if the password is equal to the confirm  password
                    if password == confirm:
                        new = User(username=username, email=email, password=password)
                        new.save()
                        messages.success(request, "Account Created Successfully!")
                    else:
                        messages.error(request, "Passwords Don't match!")
                else:
                    messages.error(request, "Invalid password!")
                    messages.info(request, "Passwords should contain any of the four character types:   uppercase letters: (A-Z), lowercase letters: (a-z), numbers (0-9), and symbols (~`! @#$%^&*()_-+={[}]|\:;\"'<,>.?/)")
            else:
                messages.error(request, "Invalid Email!")
                messages.info(request,"Acceptable email prefix formats: Allowed characters: letters (a-z), numbers, underscores, periods, and dashes. Acceptable email domain formats Allowed characters: letters, numbers, dashes. The last portion of the domain must be at least two characters, for example: .com, .org, .cc")
        return redirect("/signup")
    else:
        form = AddUser()
    return render(request, 'main/signup.html', {'form': form})
