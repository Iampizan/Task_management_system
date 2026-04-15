from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.sign_up, name="signup"),
    path('log_in/', LoginView.as_view(template_name="users/login.html"), name="login"),
    path('log_out/', LogoutView.as_view(), name="log_out"),
]