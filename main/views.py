from django.shortcuts import render
from .models import User



def index(request):
    return render(request, 'main/index.html')

def home(request):
    return render(request, 'main/home.html')

def login(request):
    # if request.method == "POST":
        # form = LogUser(request.POST)
        # if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # Authentication
            # try:
                # user = User.objects.get(username=username)
                # if user.password != password:
                    # messages.error(request,'Invalid password')
                    # return redirect("/login")
            # except User.DoesNotExist:
                # user = None
            # If authentication is successful Login
            # if user is not None:
                # auth_login(request, user)
                # messages.success(request, f"{username} Logged In Successfully!")
                # return redirect("home")
            # else:
                # messages.error(request, "Cannot Log In!")
                # return redirect("/login")
    # else:
        # form = LogUser()
    return render(request, 'main/login.html')

def signup(request):
    # if request.method == "POST":
        # form = AddUser(request.POST)
        # if form.is_valid():
            # Get user data from the form
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # confirm = form.cleaned_data['confirm']
            # Check if email is valid
            # email_pattern = re.compile(r'[a-z0-9_./]+@{1}[a-z0-9#]+.[a-z0-9]{2,5}')
            # if re.fullmatch(email_pattern, email):
                # Check whether the password is valid
                # password_pattern = re.compile(r'[A-Za-z0-9~`!@#$%^&*()_+={[}]|\:;"\'<,>.?/]+')
                # if password_pattern.search(password) and len(password) >= 8:
                    # Check if the password is equal to the confirm  password
                    # if password == confirm:
                        # new = User(username=username, email=email, password=password)
                        # new.save()
                        # messages.success(request, "Account Created Successfully!")
                    # else:
                        # messages.error(request, "Passwords Don't match!")
                # else:
                    # messages.error(request, "Invalid password!")
                    # messages.info(request, "Passwords should contain any of the four character types:   uppercase letters: (A-Z), lowercase letters: (a-z), numbers (0-9), and symbols (~`! @#$%^&*()_-+={[}]|\:;\"'<,>.?/)")
            # else:
                # messages.error(request, "Invalid Email!")
                # messages.info(request,"Acceptable email prefix formats: Allowed characters: letters (a-z), numbers, underscores, periods, and dashes. Acceptable email domain formats Allowed characters: letters, numbers, dashes. The last portion of the domain must be at least two characters, for example: .com, .org, .cc")
        # return redirect("/signup")
    # else:
        # form = AddUser()
    return render(request, 'main/signup.html')
