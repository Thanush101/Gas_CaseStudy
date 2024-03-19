from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import submit_service_request
from .views import logout_view
from .views import contact_view

urlpatterns = [
    #path("", views.home, name="home"),  # Comma is added to separate URL patterns
    path('', views.landing_page, name='landing_page'),
    # URL patterns for user authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),  # Define the signup URL pattern
    path('accounts/profile/', views.profile, name='profile'),
    path('contact/', contact_view, name='contact'),
    # URL pattern for submitting service requests
    path('submit-request/', submit_service_request, name='submit_request'),
    path('request-submitted/', views.request_submitted, name='request_submitted'),
    path('track-status/', views.track_request_status, name='track_request_status'),
    path('logout/', logout_view, name='logout')
]
