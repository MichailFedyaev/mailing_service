from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views
app_name = 'users'

urlpatterns = [
    path("users/", views.UserListView.as_view(), name="users"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="mailing:index"), name="logout",),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("email-confirm/<str:token>/", views.email_verification, name="email-confirm"),
    path("users/<int:pk>/block", views.UserBlockView.as_view(), name="user_block"),
]
