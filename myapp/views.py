from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,HttpResponse
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from django.contrib.auth import logout

def landing_page(request):
    return render(request, 'landing_page.html')

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required #User requires login to submit request
def profile(request):
    user_name = request.user.username
    return render(request, 'profile.html', {'user_name': user_name})
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_submitted') 
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})


def track_request_status(request):
    # Retrieving  all service requests from the database
    #It will display the status 
    service_requests = ServiceRequest.objects.all()
    return render(request, 'track_request_status.html', {'service_requests': service_requests})

def request_submitted(request):
    return render(request, 'request_submitted.html')
def contact_view(request):
    return render(request, 'contact.html')
def logout_view(request):
    logout(request)
    return redirect('login') # redirects to loginpage when logout
