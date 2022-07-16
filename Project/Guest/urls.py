from django.urls.conf import path
from Guest import views

app_name="guest"
urlpatterns= [
    path('landingpage/',views.LandingPage,name="guest-landingpage"),
    path('newuser/',views.NewUserEntry,name="guest-newuser"),
    path('newseeker/',views.NewSeekerEntry,name="guest-newseeker"),
    path('login/',views.login,name="guest-login"),
]