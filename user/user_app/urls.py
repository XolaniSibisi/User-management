from django.urls import path
from django.views.generic import RedirectView
from user_app.views import register, user_login, home, user_logout

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('home/', home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    # other URL patterns
]
