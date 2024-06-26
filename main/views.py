from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Restaurant, Bookings, Image, Plate, Comment
from .forms import AddUser, LogUser
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import re
import qrcode
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def index(request):
    return render(request, 'main/index.html')
   
@login_required
def home(request):
    restaurants = Restaurant.objects.all()
    
    search_query = request.GET.get("search-query")
    location = request.GET.get("location")
    cuisine = request.GET.get("cuisine")
    # Searching
    if search_query != None:
        restaurants = list(Restaurant.objects.filter(name__contains=search_query))
    # Filtering
    if location == None:
        location = ""
    if cuisine == None:
        cuisine = ""
    if location != "" or cuisine != "":
        restaurants = list(Restaurant.objects.filter(province__contains=location, cuisine__contains=cuisine))
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
    bookings = Bookings.objects.filter(user=request.user)
    data = []
    for booking in bookings:
        data.append({
            "id": booking.id,
            "name": booking.name,
            "user": booking.user,
            "restaurant": booking.restaurant,
            "qr_code": str(booking.gr_code)[4:],
            "date": booking.date,
            
        })
    return render(request, 'main/profile.html', {'data': data})

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
        "images": [str(img.image)[4:] for img in list(Image.objects.filter(restaurant=restaurant))[1:]],
        
        "plates": [{"name": plate.name, "image": str(plate.image)[4:], "price": plate.price} for plate in Plate.objects.filter(restaurant=restaurant)],
        "comments": [comment for comment in Comment.objects.filter(restaurant=restaurant)],
    }
    if request.method == "POST":
        user = request.user
        content = request.POST.get("content")
        food = request.POST.get("food")
        hygene = request.POST.get("hygene")
        service = request.POST.get("service")
        atmosphere = request.POST.get("atmosphere")
        
        if content != None:
            Comment.objects.create(user=user, content=content, restaurant=restaurant)
        if food != None and hygene != None and service != None and atmosphere != None:
            new = int(((((int(food) + int(hygene) + int(service) + int(atmosphere)) * 2) / 4) + restaurant.rating) / 2)
            restaurant.rating = new
            restaurant.save()

    # if request.method == "POST":
        # name = request.POST.get("name")
        # clients = request.POST.get("clients")
        # salle = request.POST.get("salle")
        # table = request.POST.get("table")
        # datetime = request.POST.get("reserv-time")
        # data = f"""
                # username: {request.user}
                # name:   {name}
                # N° client:  {clients}
                # table:    {salle}{table}
                # date:    {datetime}
                # """
        # qr = qrcode.make(data)
        # qr.save(f"main/static/img/bookings/{hash(request.user.username)}.png")
        # Bookings.objects.create(user=request.user, name=name, restaurant=restaurant, gr_code=f"main/static/img/bookings/{hash(request.user.username)}.png", date=datetime)
        # messages.success(request,'تم الحجز بنجاح')
    return render(request, 'main/details.html', context) 

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Authentication
        try:
            user = User.objects.get(username=username)
            if user.password != password:
                messages.error(request,'كلمة السر خاطئة')
                return redirect("/login")
        except User.DoesNotExist:
            user = None
        #If authentication is successful Login
        if user is not None:
            auth_login(request, user)
            messages.success(request, f"{username} سجل الدخول بنجاح")
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
                        messages.success(request, "تم إنشاء الحساب بنجاح")
                    else:
                        messages.error(request, "كلمتي السر لا يتوافقان")
                else:
                    messages.error(request, "كلمة السر غير صالحة")
                    messages.info(request, "كلمة السر يجب أن تتكون من كلمات كبيرة/كلمات صغيرةّ/رموز")
            else:
                messages.error(request, "البريد الإلكتروني غير صالح")
                
        return redirect("/signup")
    else:
        form = AddUser()
    return render(request, 'main/signup.html', {'form': form})

@csrf_exempt
def cancelReservation(request, id):
    message = "canceled"
    booking = get_object_or_404(Bookings, pk=id)
    booking.delete()
    return JsonResponse(message, safe=False)