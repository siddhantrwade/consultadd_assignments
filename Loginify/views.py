'''
This file maintains all the views of the application
'''

#from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import SignupForm
from . import forms
from .models import UserDetails 
# from .forms import UserDetailsForm ####### this line of code was destabilizing the entire project





# Create your views here.

############# This is a test view to test if all modules are operating as expected
def hello_world(request):

    return HttpResponse('Hello World!')

############# Default Demo Home page
def home_view(request):
    return render(request, 'loginify/home.html')

############ Signup Page View
def signup_view(request): # this view worked perfectly, althoug there was an issue with document structure which was fixed
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Signup successful')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

############# Login Page view
def login_view(request):
    if request.method == 'Post':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # User Authentication code snippet
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user) # add a login successful message here later
            return redirect('home') # this redirect to home isn't working properly, debug later
        else:
            error_message = 'Please check username and password'
            return render(request, 'loginify/login.html'), {'error_message': error_message}
    
    return render(request, 'loginify/login.html')


''' ## unable to debug issue, field exception error
############################# View for adding user with view logic
def add_user_view(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/home')  # default redirect to home page
    else:
        form = UserDetailsForm()  # Create an empty form instance

    return render(request, 'add_user.html', {'form': form})
''' 


####### Full user data display view logic
'''
def user_list_view(request):
    users = UserDetails.objects.all()  # unable to resolve this issue with UserDetails showing no objects
    return render(request, 'user_list.html', {'users': users})
'''

'''
# below signup wasn't returing http request, instead returned none, attemtpting a more simpler view
def signup_view(request):

    if request.method == 'POST': 
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Congratulations! You have successfully signed up!')
    else:
        form = SignupForm()
'''

