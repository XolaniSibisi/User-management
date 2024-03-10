from django.contrib.auth import authenticate, login, update_session_auth_hash, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
import logging

# Now you can use the logger
logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            temporary_password = get_user_model().objects.make_random_password()
            user.set_password(temporary_password)
            user.must_change_password = True
            user.temporary_password_expires = timezone.now() + timezone.timedelta(hours=1)
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
                request.session.modified = True
            else:
                request.session.set_expiry(0)
            
            # Check if the user needs to change their password and if the temporary password has expired
            if user.must_change_password and user.temporary_password_expires is not None and user.temporary_password_expires < timezone.now():
                messages.warning(request, 'Your temporary password has expired. Please change it.')
                return redirect('change_password')
            else:
                return redirect('home')
            
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials. Please try again.'})
    
    return render(request, 'login.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # Check if old password is different from new password
            if form.cleaned_data['old_password'] == form.cleaned_data['new_password']:
                return render(request, 'change_password.html', {'form': form, 'error': 'Old password cannot be the same as the new password.'})

            user = form.save()
            # Update must_change_password attribute only if it's True
            if request.user.must_change_password:
                request.user.must_change_password = False
                request.user.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

def home(request):
    return render(request, 'home.html')

@login_required
def user_logout(request):
    return render(request, 'logout.html')

class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('home')
