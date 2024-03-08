from django.urls import path
from django.views.generic import RedirectView
from user_app.views import register, user_login, home
urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    # other URL patterns
]
