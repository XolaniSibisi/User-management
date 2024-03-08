from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import logging

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            temporary_password = get_user_model().objects.make_random_password()
            user.set_password(temporary_password)
            user.save()
            
            # Send email with temporary password
            subject = "Your Temporary Password"
            html_message = render_to_string('temp_password.html', {'user': user, 'temporary_password': temporary_password})
            plain_message = strip_tags(html_message) 
            
            try:
                send_mail(subject, plain_message, 'systemsprogramming@gmail.com', [user.email], html_message=html_message)
                logger.info(f"Email sent successfully to {user.email}")
            except Exception as e:
                logger.error(f"Failed to send email to {user.email}. Error: {str(e)}")
            
            messages.success(request, 'You have successfully registered. Please check your email for the temporary password.')
            
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(1209600)
                
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials. Please try again.'})
    
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')
