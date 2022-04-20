from django.urls import path
from django.contrib.auth import views as auth_view

from core.views import frontpage, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),

]
